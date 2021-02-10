import pygame, model, help

screen = pygame.display.set_mode([600, 800])

fon = pygame.image.load("kartinki/pole_igr.jpg")
fon=pygame.transform.scale(fon,[600,800])

vorota_1 = pygame.image.load("kartinki/vorota_igr.jpg")
vorota_1=pygame.transform.scale(vorota_1,[60,100])

vorota_2 = pygame.image.load("kartinki/vorota_igr.jpg")
vorota_2=pygame.transform.scale(vorota_2,[60,100])

kartinka_sopernika = pygame.image.load("kartinki/platforma.jpg")
kartinka_sopernika = help.izmeni_kartinku(kartinka_sopernika, 225, 55, [255, 255, 255], 20)
kartinka_sopernika = pygame.transform.flip(kartinka_sopernika, False, True)
qwer = pygame.image.load("kartinki/platforma.jpg")
qwer = help.izmeni_kartinku(qwer, 225, 55, [255, 255, 255], 20)

ball = pygame.image.load("kartinki/ball.jpg")
ball = help.izmeni_kartinku(ball, 40, 40, [255, 255, 255], 1)


def risuem_kadr():
    # Рисуем кадр
    screen.blit(fon, [0, 0])
    screen.blit(vorota_1,model.vorota_1)
    screen.blit(vorota_2,model.vorota_2)

    screen.blit(ball, [model.krug.x, model.krug.y])
    screen.blit(qwer, [model.platforma.x, model.platforma.y])
    screen.blit(kartinka_sopernika, [model.sopernik.x, model.sopernik.y])
    pygame.draw.rect(screen,[255,0,0], model.vorota_1,2)
    pygame.draw.rect(screen,[255,0,0], model.vorota_2,2)
    # pygame.draw.rect(screen,cvet_sopernika, model.sopernik)
    pygame.display.flip()
