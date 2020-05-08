from time import sleep

import pygame
from random import randint


def main():
    pygame.init()
    score = 0
    screen = pygame.display.set_mode([700, 560])
    pygame.display.set_caption('Iniciando com o pygame')
    relogio = pygame.time.Clock()
    white = (255, 255, 255)
    blue = (18, 85, 241)
    green = (18, 216, 53)

    sup = pygame.Surface((700, 560))
    sup.fill(blue)
    ret = pygame.Rect(10, 10, 30, 30)
    ret2 = pygame.Rect(0, 50, 660, 20)
    ret3 = pygame.Rect(580, 450, 30, 30)

    sair = False
    alet = (randint(0, 255), randint(0, 255), randint(0, 255))
    alet2 = (randint(0, 255), randint(0, 255), randint(0, 255))
    font = pygame.font.get_default_font()
    scoretext = pygame.font.SysFont(font, 30)
    pygame.font.init()

    while not sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(15, 23)

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         ret.move_ip(-10, 0)

        time = relogio.tick(60)
        screen.fill(white)
        screen.blit(sup, [0, 0])

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= int(ret.width / 2)
        ret.top -= int(ret.height / 2)

        if ret.colliderect(ret2):
            score = 0
            pygame.mouse.set_pos(15, 23)
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret3):
            score += 1
            pygame.mouse.set_pos(15, 23)
            (ret.left, ret.top) = (xant, yant)

        text2 = scoretext.render(f'Score: {score}', 1, green)
        pygame.mouse.set_visible(False)
        pygame.draw.rect(screen, alet, ret)
        pygame.draw.rect(screen, alet2, ret2)
        pygame.draw.rect(screen, green, ret3)

        screen.blit(text2, (550, 500))
        pygame.display.update()

    pygame.quit()


main()
