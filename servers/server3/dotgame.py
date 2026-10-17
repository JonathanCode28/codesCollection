import pygame
import keyboard
import pickle
pygame.init()

WIDTH, HEIGHT = 900, 500
scr = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

players = {
    "player1x": 200,
    "player1y": 250,
    "player2x": 700,
    "player2y": 250
}

running = True
while running:
    keys = pygame.key.get_pressed()
    scr.fill("black")
    player1 = pygame.draw.circle(scr, "cyan", (players["player1x"], players["player1y"]), 25, 5)
    player2 = pygame.draw.circle(scr, "yellow", (players["player2x"], players["player2y"]), 25, 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_w]: # player1 movement
        players["player1y"] += -10
    elif keys[pygame.K_s]:
        players["player1y"] += 10
    elif keys[pygame.K_a]:
        players["player1x"] += -10
    elif keys[pygame.K_d]:
        players["player1x"] += 10
    if keys[pygame.K_UP]: # player2 movement
        players["player2y"] += -10
    elif keys[pygame.K_DOWN]:
        players["player2y"] += 10
    elif keys[pygame.K_LEFT]:
        players["player2x"] += -10
    elif keys[pygame.K_RIGHT]:
        players["player2x"] += 10

    if players["player1x"] > WIDTH: # player1 limits
        players["player1x"] -= 10
    if players["player1x"] < 0:
        players["player1x"] += 10

    if players["player1y"] > HEIGHT:
        players["player1y"] -= 10
    if players["player1y"] < 0:
        players["player1y"] += 10

    if players["player2x"] > WIDTH: # player2 limits
        players["player2x"] -= 10
    if players["player2x"] < 0:
        players["player2x"] += 10

    if players["player2y"] > HEIGHT:
        players["player2y"] -= 10
    if players["player2y"] < 0:
        players["player2y"] += 10

    pygame.display.update()
    clock.tick(60)

pygame.quit()