import pygame
import random

pygame.init()
pygame.key.set_repeat(100, 50)

WIDTH, HEIGHT = 800, 600
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bone Catching Simulator 1.0")


WHITE = (255, 255, 255)
DOG_COLOR = (150, 75, 0) #browm
BALL_COLOR = (255, 0, 0)
FPS = 60
SPEED = 5

dog_size = 50
dog_rect = pygame.Rect(WIDTH//2, HEIGHT//2, dog_size, dog_size)
dog_speed = 5

ball_size = 25
ball_rect = pygame.Rect(random.randint(0, WIDTH-ball_size), random.randint(0, HEIGHT-ball_size), ball_size, ball_size)

clck = pygame.time.Clock()

score = 0
font = pygame.font.Font(None, 36)

#new player
multi = True
ball_spd = 4

run = True
while run:
    scr.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dog_rect.x -= dog_speed
        if keys[pygame.K_RIGHT]:
            dog_rect.x += dog_speed
        if keys[pygame.K_UP]:
            dog_rect.y -= dog_speed
        if keys[pygame.K_DOWN]:
            dog_rect.y += dog_speed
    dog_rect.x = max(0, min(WIDTH-dog_size, dog_rect.x))
    dog_rect.y = max(0, min(HEIGHT-dog_size, dog_rect.y))

    if multi:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ball_rect.x -= ball_spd
        if keys[pygame.K_d]:
            ball_rect.x += ball_spd
        if keys[pygame.K_w]:
            ball_rect.y -= ball_spd
        if keys[pygame.K_s]:
            ball_rect.y += ball_spd
    ball_rect.x = max(0, min(WIDTH - ball_size, ball_rect.x))
    ball_rect.y = max(0, min(HEIGHT - ball_size, ball_rect.y))
    if dog_rect.colliderect(ball_rect):
        score += 1
        ball_rect.x = random.randint(0, WIDTH-ball_size)
        ball_rect.y = random.randint(0, WIDTH - ball_size)
    pygame.draw.rect(scr, DOG_COLOR, dog_rect)
    pygame.draw.ellipse(scr, BALL_COLOR, ball_rect)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    scr.blit(score_text, (10, 10))
    pygame.display.update()
    clck.tick(FPS)
pygame.quit()