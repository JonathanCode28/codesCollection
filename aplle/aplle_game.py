import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
score = 0
num_of_tomatoes = 4
tomatoes = []
smash = pygame.mixer.Sound("smash.mp3")


clk = pygame.time.Clock()
scr = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("smash game")

tomato_img = pygame.image.load("tomato.png")
tomato_img = pygame.transform.scale_by(tomato_img, 0.5)
tomato_rect = tomato_img.get_rect()

basket_img = pygame.image.load("basket.png")
basket_rect = basket_img.get_rect(midbottom=(WIDTH // 2, HEIGHT-50))

def new_tomato():
    tomato_rect.y = random.randint(-200, 0)
    tomato_rect.x = random.randint(0, WIDTH - tomato_rect.width)
for i in range(num_of_tomatoes):
        tomato_rect = tomato_img.get_rect()
        new_tomato()
        tomatoes.append(tomato_rect)
run = True
while run:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    basket_rect.centerx = mouse_x
    scr.fill((24, 240, 215))
    tomato_rect.y += 10
    scr.blit(tomato_img, tomato_rect)
    scr.blit(basket_img, basket_rect)
    for tomato in tomatoes:
        scr.blit(tomato_img, tomato)
        tomato.y += 10
        if tomato.y > HEIGHT:
            new_tomato()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if tomato_rect.y > HEIGHT:
        new_tomato()
    if tomato_rect.colliderect(basket_rect):
        score += 1
        new_tomato()
        smash.play()

    font = pygame.font.SysFont(None, 70)
    score_txt = font.render(f"Score: {score}", True, (0, 0, 0))
    scr.blit(score_txt, (10, 10))
    pygame.display.update()
    clk.tick(FPS)
pygame.quit()
