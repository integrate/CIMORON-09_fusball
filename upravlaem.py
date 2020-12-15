import pygame, model

TIMER_ID=pygame.event.custom_type()
def obrabotka_sobitiy():
    # обработка событий
    lodka = pygame.event.get()
    for did in lodka:
        if did.type == pygame.QUIT:
            exit()

        if did.type == pygame.KEYDOWN:

            if did.key == pygame.K_a:
                model.platforma.x = model.platforma.x - 10

            if did.key == pygame.K_d:
                model.platforma.x = model.platforma.x + 10
        if did.type==TIMER_ID:
            print("5u74457747")
def zapusk_timer ():
    pygame.time.set_timer(TIMER_ID,5000,True)