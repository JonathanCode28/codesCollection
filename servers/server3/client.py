import socket
import pickle
import pygame
import keyboard

pygame.init()

WIDTH, HEIGHT = 900, 500
scr = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("172.104.202.26", 2433))
client.connect(("localhost", 2433))

font = pygame.font.SysFont("impact", 50)

players = {
    "player1x": 200,
    "player1y": 250,
    "player1score": 0,

    "player2x": 700,
    "player2y": 250,
    "player2score": 0,

    "winner": 0
}

try:
    my_text = font.render(f"Score: {players['player2score']}", True, "white")
    my_text2 = font.render(f"Score: {players['player1score']}", True, "white")
    init_data = pickle.loads(client.recv(1024))
    my_id = init_data["player_id"]
    players = init_data["players"]
    my_x_key = f"player{my_id}x"
    my_y_key = f"player{my_id}y"
    while True:
        data = pickle.dumps(players)
        client.send(data)

        players = pickle.loads(client.recv(1024))

        keys = pygame.key.get_pressed()
        scr.fill("black")
        player1 = pygame.draw.circle(scr, "cyan", (players["player1x"], players["player1y"]), 25, 5)
        player1_score = 0
        player2 = pygame.draw.circle(scr, "yellow", (players["player2x"], players["player2y"]), 25, 5)
        player2_score = 0
        goal_width = 15
        goal_height = 120
        goal_y = (HEIGHT-goal_height)//2
        goal1 = pygame.draw.rect(scr, (255, 255, 255), (0, goal_y, goal_width, goal_height))
        goal2 = pygame.draw.rect(scr, (255, 255, 255), (900, goal_y, goal_width, goal_height))

        scr.blit(my_text, (0, 0))
        scr.blit(my_text2, (600, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_w]:  # player1 movement
            players[my_y_key] += -10
        elif keys[pygame.K_s]:
            players[my_y_key] += 10
        elif keys[pygame.K_a]:
            players[my_x_key] += -10
        elif keys[pygame.K_d]:
            players[my_x_key] += 10
        if keys[pygame.K_UP]:  # player2 movement
            players[my_y_key] += -10
        elif keys[pygame.K_DOWN]:
            players[my_y_key] += 10
        elif keys[pygame.K_LEFT]:
            players[my_x_key] += -10
        elif keys[pygame.K_RIGHT]:
            players[my_y_key] += 10

        if players[my_x_key] > WIDTH:  # player1 limits
            players[my_x_key] -= 10
        if players[my_x_key] < 0:
            players[my_x_key] += 10

        if players[my_y_key] > HEIGHT:
            players[my_y_key] -= 10
        if players[my_y_key] < 0:
            players[my_y_key] += 10

        if players[my_x_key] > WIDTH:  # player2 limits
            players[my_x_key] -= 10
        if players[my_x_key] < 0:
            players[my_x_key] += 10

        if players[my_y_key] > HEIGHT:
            players[my_y_key] -= 10
        if players[my_y_key] < 0:
            players[my_y_key] += 10
        #
        # if player1.colliderect(goal1 or goal2):
        #     player2_score += 1
        # if player2.colliderect(goal1 or goal2):
        #     player1_score += 1

        if players["winner"] != 0:
            win_text = font.render(f"winner is player {players['winner']}",  True, "gold")
            scr.blit(win_text, (WIDTH//2, HEIGHT//2))
        pygame.display.update()
        #clock.tick(FPS)
finally:
    client.close()