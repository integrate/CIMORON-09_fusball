import pygame, model, help

screen = pygame.display.set_mode([600, 800])
fon = pygame.image.load("kartinki/fon.jpg")
qwer = pygame.image.load("kartinki/platforma.jpg")
qwer = help.izmeni_kartinku(qwer, 225, 55, [255, 255, 255], 20)

ball = pygame.image.load("kartinki/ball.jpg")
ball = help.izmeni_kartinku(ball, 40, 40, [255, 255, 255], 1)


def risuem_kadr():
    # Рисуем кадр
    screen.blit(fon, [0, 0])
    eboe=[132,22,0]

    cvet_sopernika=[63,22,0]
    oe = [132, 2, 0]

    screen.blit(fon, [0, 0])
    screen.blit(ball, [model.krug.x, model.krug.y])
    screen.blit(qwer, [model.platforma.x, model.platforma.y])
    pygame.draw.rect(screen,eboe,model.vorota1)
    pygame.draw.rect(screen,oe,model.vorota2)
    pygame.draw.rect(screen,cvet_sopernika, model.sopernik)
    pygame.display.flip()
