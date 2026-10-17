import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star collection game")
FPS = 60

def load_img(path, size, color_key):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, size)
    image.set_colorkey(color_key)
    return image

shuttle_img = load_img("shuttle.png", (60, 100), WHITE)
asteroid_img = load_img("asteroid.png", (90, 90), WHITE)
iss_img = load_img("iss.png", (100, 50), WHITE)
BG_img = pygame.image.load("spaceBG2.png")
BG_img = pygame.transform.scale(BG_img, (WIDTH, HEIGHT))

#creating a rocket's class
class SpaceCraft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = shuttle_img
        self.rect = self.image.get_rect(midbottom = (WIDTH//2, HEIGHT-10))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.shield = False
        self.shield_timer = 0

    def update(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if self.shield:
            self.shield_timer -= 1
            if self.shield_timer <= 0:
                self.shield_timer = False

    def reset_pos(self):
        self.rect.midbottom = (WIDTH//2, HEIGHT-10)
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = asteroid_img
        self.rect = self.image.get_rect(topleft = (random.randint(WIDTH, WIDTH+100), random.randint(0, HEIGHT-100)))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = random.randint(4, 8)
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH+100)
            self.rect.y = random.randint(0, HEIGHT-100)

class Iss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = iss_img
        self.rect = self.image.get_rect(topleft=(random.randint(WIDTH, WIDTH+100), random.randint(0, HEIGHT+40)))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = random.randint(4, 8)
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH+100)
            self.rect.y = random.randint(0, HEIGHT-40)
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill((33, 255, 100))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = -10
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

#creating game's objects
spacecraft = SpaceCraft()
iss2 = pygame.sprite.Group(Iss() for _ in range(3))
asteroids = pygame.sprite.Group(Asteroid() for _ in range(5))
lasers = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(spacecraft, *asteroids, *iss2)

#creating a game's clock for FPS count management
clk = pygame.time.Clock()
score = 0
lives = 5
game_over = False

run = True
while run:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            run = False
       if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
           laser = Laser(spacecraft.rect.centerx, spacecraft.rect.top)
           lasers.add(laser)
           all_sprites.add(laser)

    if not game_over:
        keys = pygame.key.get_pressed()
        spacecraft.update(keys)
        asteroids.update()
        iss2.update()
        lasers.update()

    if spacecraft.rect.top <= 0:
        spacecraft.reset_pos()
        score += 1

    for asteroid in asteroids:
        if not game_over and pygame.sprite.collide_mask(spacecraft, asteroid):
            if not spacecraft.shield:
                asteroid.kill()
                score -= 2
                lives -= 1
                if lives <= 0:
                    game_over = True
                else:
                    spacecraft.reset_pos()

    for iss in iss2:
        if pygame.sprite.collide_mask(spacecraft, iss):
            score += 3
            spacecraft.shield = True
            spacecraft.shield_timer = 180
            iss.rect.x = random.randint(WIDTH, WIDTH+100)
            iss.rect.y = random.randint(0, HEIGHT-40)

    for laser in lasers:
        hit_asteroids = pygame.sprite.spritecollide(laser, asteroids, True, pygame.sprite.collide_mask)
        if hit_asteroids:
            score += 2
            laser.kill()
            new_asteroid = Asteroid()
            asteroids.add(new_asteroid)
            all_sprites.add(new_asteroid)

    scr.blit(BG_img, (0, 0))
    #scr.blit(spacecraft.image, spacecraft.rect)
    all_sprites.draw(scr)

    #font = pygame.font.SysFont('Bitcount Grid Double', 55)
    font = pygame.font.SysFont(None, 55)
    score_txt = font.render(f"Score: {score}", True, (34, 240, 177))
    lives_txt = font.render(f"Lives: {lives}", True, (255, 0,0))
    scr.blit(score_txt, (10, 10))
    scr.blit(lives_txt, (10, 60))
    if game_over:
        game_over_font = pygame.font.SysFont(None, 150)
        game_over_txt = game_over_font.render("GAME OVER", True, (255, 0, 0))
        scr.blit(game_over_txt, (WIDTH//2 - game_over_txt.get_width()//2, HEIGHT//2 - game_over_txt.get_height()//2))

        score_font = pygame.font.SysFont(None, 80)
        score_font_txt = score_font.render(f"Final score: {score}", True, (200, 44, 189))
        scr.blit(score_font_txt, (WIDTH//2 - score_font_txt.get_width()//2, HEIGHT//2 - score_font_txt.get_height() +100))
    if spacecraft.shield:
        pulse_size = 5+ int(5* math.sin(pygame.time.get_ticks()*0.01))
        aura_surface = pygame.Surface((spacecraft.rect.width + pulse_size, spacecraft.rect.height + pulse_size), pygame.SRCALPHA)

        pygame.draw.ellipse(aura_surface, (23, 177, 200, 100), aura_surface.get_rect())
        scr.blit(aura_surface, (spacecraft.rect.x-pulse_size //2, spacecraft.rect.y-pulse_size //2))

    pygame.display.update()
    clk.tick(FPS)
pygame.quit()