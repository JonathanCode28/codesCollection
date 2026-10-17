import pygame
import random

pygame.init()

scr = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Image handeling in Pygame")
#load image
loaded_image = pygame.image.load("image-loader.jpeg")
#resize image
loaded_image = pygame.transform.scale(loaded_image, (150, 150))

pygame.draw.rect(scr, (166, 230, 98), (50, 50, 100, 100))
pygame.draw.circle(scr, (255, 0, 0), (200, 200), 50)
pygame.draw.ellipse(scr, (0, 0, 255), (300, 100, 150, 75))
pygame.draw.line(scr, (255, 255, 0), (400, 300), (500, 400), 10)
pygame.draw.lines(scr, (255, 0, 255), True, [(655, 200), (450, 500), (300, 250)], 3)
pygame.draw.polygon(scr, (0, 255, 255), [(250, 250), (300, 350), (200, 350)])
pygame.draw.arc(scr, (255, 165, 0), (100, 400, 150, 75), 0, 3.14, 10)

image1 = pygame.image.load("image-loader.jpeg")
image2 = pygame.image.load("paintImage.jpeg")

image1 = pygame.transform.scale(image1, (100, 100))
image2 = pygame.transform.scale(image2, (75, 75))

#random images function
def place_random_images():
    x1 = random.randint(100, 600)
    y1 = random.randint(100, 600)

    x2 = random.randint(200, 400)
    y2 = random.randint(200, 400)

    scr.fill((120, 120, 120))
    scr.blit(image1, (x1, y1))
    scr.blit(image2, (x2, y2))

    pygame.display.update()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(scr, "image-loader.jpeg")
                print("painting is saved")
            elif event.key == pygame.K_u:
                scr.fill((255, 255, 255))
                random_x = random.randint(100, 600)
                random_y = random.randint(100, 600)
                scr.blit(loaded_image, (random_x, random_y))
            elif event.key == pygame.K_r:
                place_random_images()

    pygame.display.update()
pygame.quit()