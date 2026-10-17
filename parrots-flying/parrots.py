import pygame

pygame.init()

WIDTH = 800

HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

class Parrot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.sprites = []
        self.current_sprite = 0
        self.animation_speed = 0.17

        for i in range(1, 16):
            self.image = pygame.image.load(f"Asset {i}.png")
            self.sprites.append(self.image)

        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        self.current_sprite += self.animation_speed
        self.image = self.sprites[int(self.current_sprite)]

moving_parrots = pygame.sprite.Group()
parrot = Parrot(200, 200)
moving_parrots.add(parrot)

running = True
while running:
    screen.fill("skyblue")
    moving_parrots.draw(screen)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    clock.tick(60)

pygame.quit()