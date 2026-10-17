import pygame
pygame.init()

WIDTH, HEIGHT = 900, 500
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

img_archer = pygame.image.load("archer_standing.png")
img_archer = pygame.transform.scale_by(img_archer, 0.2)
img_archer_right = img_archer
img_archer_left = pygame.transform.flip(img_archer, True, False)
rect_archer = img_archer.get_rect()
facing_right = True

img_golem = pygame.image.load("golem_standing.png")
img_golem = pygame.transform.scale_by(img_golem, 0.2)
img_golem_right = img_golem
img_golem_left = pygame.transform.flip(img_golem, True, False)
rect_golem = img_archer.get_rect()

physics = {
    "gravity": 1,
    "velocity_y": 0,
    "jump_power": -15,
}

platform_rect = pygame.Rect(50, 400, 150, 10)

running = True
while running:
    on_ground = False
    screen.fill("black")
    keys = pygame.key.get_pressed()

    prev_rect = rect_archer.copy()

    physics["velocity_y"] += physics["gravity"]
    rect_archer.y += physics["velocity_y"]

    if rect_archer.colliderect(platform_rect) and physics["velocity_y"] > 0:
        if prev_rect.bottom <= platform_rect.top:
            rect_archer.bottom = platform_rect.top
            velocity_y = 0
            on_ground = True
    pygame.draw.rect(screen, (23, 124, 211), platform_rect)

    if facing_right:
        screen.blit(img_archer, rect_archer)
        screen.blit(img_golem, rect_golem)
    else:
        screen.blit(img_archer_left, rect_archer)
        screen.blit(img_golem_left, rect_golem)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if rect_archer.bottom >= HEIGHT:
        rect_archer.bottom = HEIGHT
        physics["velocity_y"] = 0
        on_ground = True

    if keys[pygame.K_SPACE] and on_ground == True:
        physics["velocity_y"] = physics["jump_power"]

    if keys[pygame.K_d]:
        rect_archer.x += 5
        facing_right = True
    if keys[pygame.K_a]:
        rect_archer.x -= 5
        facing_right = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()