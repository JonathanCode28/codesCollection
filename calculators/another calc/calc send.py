import pygame

pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("inkfree", 60)

Zero = pygame.image.load("0.png")
Zero_rect = Zero.get_rect(topleft=(300, 700))

One = pygame.image.load("1.png")
One_rect = One.get_rect(topleft=(150, 600))

Two = pygame.image.load("2.png")
Two_rect = Two.get_rect(topleft=(300, 600))

Three = pygame.image.load("3.png")
Three_rect = Three.get_rect(topleft=(450, 600))

Four = pygame.image.load("4.png")
Four_rect = Four.get_rect(topleft=(150, 500))

Five = pygame.image.load("5.png")
Five_rect = Five.get_rect(topleft=(300, 500))

Six = pygame.image.load("6.png")
Six_rect = Six.get_rect(topleft=(450, 500))

Seven = pygame.image.load("7.png")
Seven_rect = Seven.get_rect(topleft=(150, 400))

Eight = pygame.image.load("8.png")
Eight_rect = Eight.get_rect(topleft=(300, 400))

Nine = pygame.image.load("9.png")
Nine_rect = Nine.get_rect(topleft=(450, 400))

Plus = pygame.image.load("plus.png")
Plus_rect = Plus.get_rect(topleft=(600, 400))

Equal = pygame.image.load("equal.png")
Equal_rect = Equal.get_rect(topleft=(150, 700))

current_value = ""
def button(rect, num):
    global current_value
    place = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if rect.collidepoint(place):
            if num == "=":
                print("sum")
            else:
                current_value += num
                print(num)

run = True
while run:
    screen.fill("black")
    calc = font.render(f"{current_value}", True, "tomato")
    screen.blit(calc, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button(Zero_rect, "0")
            button(One_rect, "1")
            button(Two_rect, "2")
            button(Three_rect, "3")
            button(Four_rect, "4")
            button(Five_rect, "5")
            button(Six_rect, "6")
            button(Seven_rect, "7")
            button(Eight_rect, "8")
            button(Nine_rect, "9")
            button(Equal_rect, "=")
            button(Plus_rect, "+")

    screen.blit(Zero, Zero_rect)
    screen.blit(One, One_rect)
    screen.blit(Two, Two_rect)
    screen.blit(Three, Three_rect)
    screen.blit(Four, Four_rect)
    screen.blit(Five, Five_rect)
    screen.blit(Six, Six_rect)
    screen.blit(Seven, Seven_rect)
    screen.blit(Eight, Eight_rect)
    screen.blit(Nine, Nine_rect)
    screen.blit(Plus, Plus_rect)
    screen.blit(Equal, Equal_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
