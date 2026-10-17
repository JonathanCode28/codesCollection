import pygame
import random

# initializing game
pygame.init()

# creating a game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("paint game")

# white background
screen.fill((255, 255, 255))
color = (0, 0, 0)
brush_color = (0, 0, 0)

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

brush_size = 1

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                brush_size += 1
            elif event.button == 3 and brush_size > 1:
                brush_size -=1
                print("Brash size decreased:", brush_size)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                brush_color = (255, 0, 0) #red color in rgb
                print("color is red")

            elif event.key == pygame.K_g:
                brush_color = (0, 255, 0) #green color in rgb
                print("color is green")

            elif event.key == pygame.K_b:
                brush_color = (0, 0, 255) #blue color in rgb
                print("color is blue")

            elif event.key == pygame.K_s:
                print("saving...")
                pygame.image.save(screen, "/Users/yonatanostrovsky/Desktop/python/paintImage.jpeg")
                print("save as paintImage.jpeg")

            elif event.key == pygame.K_UP:
                print("ok", pygame.K_UP)
                brush_size += 1

            elif event.key == pygame.K_DOWN:
                print("ok", pygame.K_DOWN)
                brush_size -= 1

    if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
        mouse_position = pygame.mouse.get_pos()
        pygame.draw.circle(screen, brush_color, mouse_position, brush_size)

        color = get_random_color()

    pygame.display.update()