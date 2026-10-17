import pygame
import random

pygame.init()
pygame.key.set_repeat(100, 50)

WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
FPS = 60
SPEED = 5

scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving the image")
scr.fill((BLACK))

pygame.mixer.init()
coll_sound = pygame.mixer.Sound("punch_sound.mp3")

player_img = pygame.image.load("paintImage.jpeg")
player_img = pygame.transform.scale(player_img, (100, 100))
player_rect = player_img.get_rect(topleft=(WIDTH // 2, HEIGHT // 2))

obst_img = pygame.image.load("spaceBG.jpeg")
obst_img = pygame.transform.scale(obst_img, (100, 100))
obst_rect = obst_img.get_rect(topleft=(220, 220))


run = True
while run:
    scr.fill(BLACK)
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= 5
            if event.key == pygame.K_RIGHT:
                player_rect.x += 5
            if event.key == pygame.K_UP:
                player_rect.y -= 5
            if event.key == pygame.K_DOWN:
                player_rect.y += 5
    if player_rect.x < 0:
        player_rect.x = 0
    if player_rect.x > WIDTH - player_rect.width:
        player_rect.x = WIDTH - player_rect.width
    if player_rect.y < 0:
        player_rect.y = 0
    if player_rect.y > HEIGHT - player_rect.height:
        player_rect.y = HEIGHT - player_rect.height

    if player_rect.colliderect(obst_rect):
        coll_sound.play()
        print("collision detected")
        player_rect.x = WIDTH//2
        player_rect.y = HEIGHT//2
        obst_rect.x = random.randint(70, WIDTH)
        obst_rect.y = random.randint(70, HEIGHT)

    scr.blit(player_img, player_rect)
    scr.blit(obst_img, obst_rect)
    pygame.display.update()

pygame.quit()