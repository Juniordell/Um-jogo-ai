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
    ret4 = pygame.Rect(200, 110, 500, 20)
    ret5 = pygame.Rect(0, 110, 150, 20)
    ret6 = pygame.Rect(20, 180, 165, 20)
    square = pygame.Rect(20, 140, 30, 30)
    bar1 = pygame.Rect(0, 50, 20, 560)
    bar2 = pygame.Rect(680, 110, 20, 450)
    bars = [bar1, bar2]
    sair = False
    alet = (randint(0, 255), randint(0, 255), randint(0, 255))
    alet2 = (randint(0, 255), randint(0, 255), randint(0, 255))
    font = pygame.font.get_default_font()
    scoretext = pygame.font.SysFont(font, 30)
    pygame.font.init()
    acerto = pygame.mixer.Sound('acerto.ogg')
    explosao = pygame.mixer.Sound('explosão.ogg')
    velocidade = 1

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
        square.move_ip(velocidade * time, 0)
        if square.collidelist(bars) >= 0:
            velocidade = -velocidade

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= int(ret.width / 2)
        ret.top -= int(ret.height / 2)

        if ret.colliderect(ret2):
            score = 0
            explosao.play()
            pygame.mouse.set_pos(15, 23)
            explosao.set_volume(1)
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret3):
            score += 1
            pygame.mouse.set_pos(15, 23)
            acerto.play()
            (ret.left, ret.top) = (xant, yant)

        text2 = scoretext.render(f'Score: {score}', 1, green)
        pygame.mouse.set_visible(False)
        pygame.draw.rect(screen, alet, ret)
        pygame.draw.rect(screen, alet2, ret2)
        pygame.draw.rect(screen, green, ret3)
        pygame.draw.rect(screen, alet2, ret4)
        pygame.draw.rect(screen, alet2, ret5)
        pygame.draw.rect(screen, alet2, square)
        pygame.draw.rect(screen, alet2, bar1)
        pygame.draw.rect(screen, alet2, bar2)
        pygame.draw.rect(screen, alet2, ret6)
        screen.blit(text2, (550, 500))
        pygame.display.update()

    pygame.quit()


main()
