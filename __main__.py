import pygame, time, help, upravlaem, model, risovanie

pygame.init()
pygame.key.set_repeat(50)

while 1 == 1:
    time.sleep(1 / 60)

    upravlaem.obrabotka_sobitiy()
    model.dvizhenie()

    risovanie.risuem_kadr()
