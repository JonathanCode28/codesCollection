import pygame

pygame.init()

scr = pygame.display.set_mode((700, 700))
pygame.display.set_caption("collide session")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

rect1 = pygame.Rect(300, 200, 200, 100)
scr.fill(WHITE)

pygame.draw.rect(scr, RED, rect1)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(f"mouse clicked at: {mouse_pos}")

            if rect1.collidepoint(mouse_pos):
                print("Rectangle clicked!!")
                pygame.draw.rect(scr, GREEN, rect1)

    pygame.display.update()

pygame.quit()