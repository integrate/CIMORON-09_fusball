import pygame
pygame.init()
schet_ochkov_poymaneh_kakashek = pygame.font.SysFont("arial", 25, True, False)

def izmeni_kartinku(kartinka, shirina, visota, uberi_cvet, porog):
    kartinka = pygame.transform.scale(kartinka, [shirina, visota])
    kartinka = kartinka.convert()
    m1 = pygame.mask.from_threshold(kartinka, uberi_cvet, [porog, porog, porog])
    m1.invert()
    q2 = kartinka.copy()
    q2.fill([0, 0, 0, 0])
    m1.to_surface(q2, kartinka, None, None, None)
    # q2.set_colorkey([0, 0, 0])
    return q2





# def schet_ochkov(screen, color, shet, raund):
#     ert = str(raund)
#     qwer = str(shet)
#     poi = "  РАУНД: " + ert + " " + qwer + " Забитые голы "
#     schet_ochkov_poymaneh_kakashek_kartinka = schet_ochkov_poymaneh_kakashek.render(poi, True, color)
#
#     screen.blit(schet_ochkov_poymaneh_kakashek_kartinka, [0, 0])
