import pygame, model


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
