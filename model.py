import pygame
sopernik=pygame.Rect((300, 300, 225, 55))
platforma = pygame.Rect(0, 555, 225, 55)
krug = pygame.Rect(0, 555, 40, 40)
speedx = 50
speedy = 50
vorota1=pygame.Rect(200,0,200,30)
vorota2=pygame.Rect(200, 770, 200, 30)

def dvizhenie():
    global speedy, speedx
    # Они не дают прямоугольнику выйти за с границы окна
    if platforma.y < 0:
        platforma.y = 0

    if platforma.x < 0:
        platforma.x = 0

    if platforma.right > 600:
        platforma.right = 600

    if platforma.bottom > 800:
        platforma.bottom = 800

    # движение маленького прямоугольника
    krug.x = krug.x + speedx

    if krug.right > 600:
        speedx = -6
        krug.right = 600
    if krug.x < 0:
        speedx = 6
        krug.x = 0

    krug.y = krug.y + speedy

    if krug.bottom > 800:
        speedy = -6
        krug.bottom = 800
    if krug.y < 0:
        speedy = 6
        krug.y = 0

    ll = krug.colliderect(platforma)
    if ll == 1 and speedy > 0:
        speedy = -15
        krug.bottom = platforma.y

    tyu = vorota1.colliderect(krug)
    if tyu == 1 and speedy > 0:
        speedy=0
        speedx=0
        print("голь варота 1")

    rey = vorota2.colliderect(krug)
    if rey == 1 and speedy > 0:
        speedy = 0
        speedx = 0

        print("голь варота 2")