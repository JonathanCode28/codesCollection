import random
import pygame, socket, pickle, math

pygame.init()

WIDTH, HEIGHT = 900, 500
WORLD_WIDTH = 5000

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#ADDR = "localhost"
ADDR = "194.36.89.237"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ADDR, 2433))

init_data = pickle.loads(client.recv(4096))
player_id = init_data["player_id"]
data = init_data["data"]

player_key = f"player{player_id}"

clock = pygame.time.Clock()

img_archer = pygame.image.load("archer_standing.png")
img_archer = pygame.transform.scale_by(img_archer, 0.2)

img_archer_right = img_archer
img_archer_left = pygame.transform.flip(img_archer, True, False)
rect_archer = img_archer.get_rect()

img_arrow = pygame.image.load("arrow.png")

img_platform = pygame.image.load("platform.png")


class Platform:
    def __init__(self, x, y, width, height, color, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

        if image is not None:
        #קודם היה image.get_height()
        # זה גרם לפלטפורמות להיות בגובה לא מתאים
        # עכשיו משתמשים בגובה שקבענו לפלטפורמה
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = None

    def draw(self, win, camera_x):
        camera_rect = pygame.Rect(
        self.rect.x - camera_x,
        self.rect.y,
        self.rect.width,
        self.rect.height
        )

        if self.image is not None:
            win.blit(self.image, camera_rect)
        else:
            pygame.draw.rect(win, self.color, camera_rect)


platforms = []

# קודם הפלטפורמות היו רנדומליות בכל קליינט
# זה אומר שכל מחשב יכול לראות עולם אחר
# seed גורם לכך שכל המחשבים יקבלו את אותן פלטפורמות
random.seed(1)
for i in range(25):
    x = random.randint(0, WORLD_WIDTH - 150)
    y = random.randint(100, HEIGHT - 100)

platform_width = random.randint(80, 150)
platform_height = 20
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

platforms.append(
Platform(x, y, platform_width, platform_height, color, image=img_platform)
)


class Arrow:
    def __init__(self, arrow_data):
        self.data = arrow_data

    def move(self):
        self.data["x"] += self.data["speed"] * math.cos(self.data["angle"])
        self.data["y"] += self.data["speed"] * math.sin(self.data["angle"])

    def make_img_angle(self):
        rotated_arrow = pygame.transform.rotate(
        img_arrow,
        -math.degrees(self.data["angle"])
        )
        return rotated_arrow

    def get_rect(self):
        # בדיקת פגיעה במיקום עולם
        return self.make_img_angle().get_rect(
        center=(self.data["x"], self.data["y"])
        )

    def get_draw_rect(self, camera_x):
        # בציור בלבד מורידים camera_x
        return self.make_img_angle().get_rect(
        center=(self.data["x"] - camera_x, self.data["y"])
        )

    def show(self, win, camera_x):
        win.blit(self.make_img_angle(), self.get_draw_rect(camera_x))

    def target(self, target_key):
        self.data["hit"] = target_key


run = True

while run:
    screen.fill("black")
    keys = pygame.key.get_pressed()

    camera_x = data[player_key]["x"] - WIDTH // 2
    camera_x = max(0, camera_x)
    camera_x = min(camera_x, WORLD_WIDTH - WIDTH)

    rect_archer.x = data[player_key]["x"]
    rect_archer.y = data[player_key]["y"]

    prev_rect = rect_archer.copy()

    data[player_key]["on_ground"] = False

    data[player_key]["velocity_y"] += data[player_key]["gravity"]
    data[player_key]["y"] += data[player_key]["velocity_y"]
    rect_archer.y = data[player_key]["y"]

    for platform in platforms:
        platform.draw(screen, camera_x)

        if rect_archer.colliderect(platform.rect) and data[player_key]["velocity_y"] > 0:
            if prev_rect.bottom <= platform.rect.top:
                rect_archer.bottom = platform.rect.top
                data[player_key]["y"] = rect_archer.y
                data[player_key]["velocity_y"] = 0
                data[player_key]["on_ground"] = True

        if rect_archer.bottom >= HEIGHT:
            rect_archer.bottom = HEIGHT
            data[player_key]["y"] = rect_archer.y
            data[player_key]["velocity_y"] = 0
            data[player_key]["on_ground"] = True

        if keys[pygame.K_SPACE] and data[player_key]["on_ground"] == True:
            data[player_key]["velocity_y"] = data[player_key]["jump_power"]

    # קודם היה רק D לימין ורק A לשמאל
    # אם משחקים עם החצים, שמאלה לא עבד
    # עכשיו גם החצים וגם A D עובדים
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            data[player_key]["direction"] = "right"
            data[player_key]["x"] += data[player_key]["speed"]

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            data[player_key]["direction"] = "left"
            data[player_key]["x"] -= data[player_key]["speed"]

        if data[player_key]["x"] < 0:
            data[player_key]["x"] = 0

        if data[player_key]["x"] > WORLD_WIDTH - rect_archer.width:
            data[player_key]["x"] = WORLD_WIDTH - rect_archer.width

    for key, player_data in data.items():
        rect_player = img_archer.get_rect()

        rect_player.x = data[key]["x"]
        rect_player.y = data[key]["y"]

    # קודם hp שימש ישירות כרוחב
    # אם hp הוא 100, הפס היה רחב מדי ביחס לשחקן
    # עכשיו הרוחב מחושב לפי רוחב השחקן
    hp_width = int(rect_player.width * data[key]["hp"] / 100)

    hp_bar = pygame.Rect(
    rect_player.x - camera_x,
    rect_player.y - 10,
    hp_width,
    8
    )
    pygame.draw.rect(screen, "green", hp_bar)

    if data[key]["direction"] == "right":
        img = img_archer_right
    else:
        img = img_archer_left

    screen.blit(img, (rect_player.x - camera_x, rect_player.y))

    for arrow in player_data["arrows"][:]:
        current_arrow = Arrow(arrow)

        # חץ לא פעיל כבר לא זז ולא מצויר
        if arrow["active"]:
            current_arrow.move()
            current_arrow.show(screen, camera_x)

    if key != player_key:
        for my_arrow in data[player_key]["arrows"][:]:
            my_current_arrow = Arrow(my_arrow)

    if (
        my_current_arrow.get_rect().colliderect(rect_player)
    and my_arrow["active"] == True
    ):
        my_arrow["active"] = False
        my_current_arrow.target(key)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

    # העכבר במיקום מסך והשחקן במיקום עולם
    # לכן מוסיפים camera_x
        mouse_world_x = mouse_x + camera_x

    arrow_angle = math.atan2(
    mouse_y - rect_archer.centery,
    mouse_world_x - rect_archer.centerx
    )

    new_arrow = {
    "x": rect_archer.centerx,
    "y": rect_archer.centery,
    "speed": 10,
    "active": True,
    "angle": arrow_angle,
    "hit": None,
    }

    data[player_key]["arrows"].append(new_arrow)

    if data[player_key]["winner"] == 1:
        font = pygame.font.SysFont(None, 90)
        game_over_txt = font.render(
        f"player {player_key} is the winner",
        True,
        (255, 0, 0)
        )
        screen.blit(
        game_over_txt,
        (
        WIDTH // 2 - game_over_txt.get_width() // 2,
        HEIGHT // 2 - game_over_txt.get_height() // 2
        )
        )

    pygame.display.update()
    clock.tick(60)

    try:
        client.send(pickle.dumps(data[player_key]))
        data = pickle.loads(client.recv(4096))

    except Exception as e:
        print("Disconnected from server")
        print(e)
        break

client.close()
pygame.quit
