import pygame, random, upravlaem

sopernik = pygame.Rect((300, 100, 225, 55))
platforma = pygame.Rect(0, 555, 225, 55)
krug = pygame.Rect(0, 555, 40, 40)
speedx = 2
speedy = 2
vorota_1 = pygame.Rect(200, 0, 200, 30)
vorota_2 = pygame.Rect(200, 770, 200, 30)
skorost_sopernika = random.randint(1, 5)


def dvizhenie():
    global speedy, speedx, skorost_sopernika
    sopernik.x = sopernik.x + skorost_sopernika
    # Они не дают прямоугольнику выйти за с границы окна
    if platforma.y < 0:
        platforma.y = 0

    if platforma.x < 0:
        platforma.x = 0

    if platforma.right > 600:
        platforma.right = 600

    if platforma.bottom > 800:
        platforma.bottom = 800
    # Они не дают прямоугольнику выйти за с границы окна
    if sopernik.y < 0:
        sopernik.y = 0

    if sopernik.x < 0:
        sopernik.x = 0
        skorost_sopernika = -skorost_sopernika

    if sopernik.right > 600:
        sopernik.right = 600
        skorost_sopernika = -skorost_sopernika

    if sopernik.bottom > 800:
        sopernik.bottom = 800
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

    ll = krug.colliderect(sopernik)
    if ll == 1 and speedy < 0:
        speedy = +15
        krug.y = sopernik.bottom

    tyu = vorota_1.colliderect(krug)
    if tyu == 1 and speedy > 0:
        speedy = 0
        speedx = 0
        print("голь варота 1")
        upravlaem.zapusk_timer()

    rey = vorota_2.colliderect(krug)
    if rey == 1 and speedy > 0:
        speedy = 0
        speedx = 0
        print("голь варота 2")
        upravlaem.zapusk_timer()
def restart():
    global speedy,speedx
    tiwq = random.choice([-10, +10])
    speedy = tiwq
    speedx = tiwq
    krug.x = 300
    krug.y = 400
