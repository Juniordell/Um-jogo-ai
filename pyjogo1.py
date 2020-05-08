from time import sleep

import pygame
from random import randint


def main():
    global alet
    score = 0
    pygame.init()
    screen = pygame.display.set_mode([700, 560])
    pygame.display.set_caption('Iniciando com o pygame')
    relogio = pygame.time.Clock()
    white = (255, 255, 255)
    blue = (18, 85, 241)
    verde = (18, 216, 53)

    sup = pygame.Surface((700, 560))
    sup.fill(blue)
    # sup2 = pygame.Surface((50, 50))
    # sup2.fill(verde)
    ret = pygame.Rect(10, 10, 30, 30)
    ret2 = pygame.Rect(0, 50, 660, 20)
    ret3 = pygame.Rect(580, 450, 30, 30)
    ret4 = pygame.Rect(200, 110, 500, 20)
    ret5 = pygame.Rect(0, 110, 150, 20)
    ret6 = pygame.Rect(20, 180, 165, 20)
    ret7 = pygame.Rect(265, 180, 420, 20)
    ret8 = pygame.Rect(180, 180, 20, 190)
    ret9 = pygame.Rect(250, 180, 20, 260)
    ret10 = pygame.Rect(110, 420, 160, 20)
    ret11 = pygame.Rect(100, 240, 20, 200)
    square = pygame.Rect(20, 140, 30, 30)
    bar1 = pygame.Rect(0, 50, 20, 560)
    bar2 = pygame.Rect(680, 110, 20, 450)
    suport1 = pygame.Rect(0, 0, 45, 5)
    suport2 = pygame.Rect(0, 40, 45, 5)
    bars = [bar1, bar2]
    velocidade = 1
    sair = False
    alet = (randint(0, 255), randint(0, 255), randint(0, 255))
    alet2 = (randint(0, 255), randint(0, 255), randint(0, 255))
    font = pygame.font.get_default_font()
    ganhou = pygame.font.SysFont(font, 45)
    perdeu = pygame.font.SysFont(font, 30)
    scoretext = pygame.font.SysFont(font, 30)
    pygame.font.init()
    acerto = pygame.mixer.Sound('acerto.ogg')
    explosao = pygame.mixer.Sound('explosão.ogg')
    while not sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(15, 23)

            # if event.type == pygame.MOUSEMOTION:
            #     ret = ret.move(-1, -2)
            #
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         ret.move_ip(-10, 0)
            #
            #     if event.key == pygame.K_RIGHT:
            #         ret.move_ip(10, 0)
            #
            #     if event.key == pygame.K_DOWN:
            #         ret.move_ip(0, 10)
            #
            #     if event.key == pygame.K_UP:
            #         ret.move_ip(0, -10)

        time = relogio.tick(60)
        screen.fill(white)
        screen.blit(sup, [0, 0])
        square.move_ip(velocidade * time, 0)
        # screen.blit(sup2, [125, 125])
        if square.collidelist(bars) >= 0:
            velocidade = -velocidade

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= int(ret.width / 2)
        ret.top -= int(ret.height / 2)

        if ret.colliderect(ret2) or ret.colliderect(ret4) or ret.colliderect(ret5) or ret.colliderect(bar1) or ret.colliderect(bar2) or ret.colliderect(square):
            text = perdeu.render('Colidiu!', 1, white)
            score = 0
            explosao.play()
            pygame.mouse.set_pos(15, 23)
            explosao.set_volume(1)
            screen.blit(text, (150, 150))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(suport1) or ret.colliderect(suport2):
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret3):
            score += 1
            acerto.play()
            pygame.mouse.set_pos(15, 23)
            (ret.left, ret.top) = (xant, yant)

        text2 = scoretext.render(f'Score: {score}', 1, verde)
        pygame.mouse.set_visible(False)
        pygame.draw.rect(screen, alet, ret)
        pygame.draw.rect(screen, alet2, ret2)
        pygame.draw.rect(screen, verde, ret3)
        pygame.draw.rect(screen, alet2, ret4)
        pygame.draw.rect(screen, alet2, ret5)
        pygame.draw.rect(screen, alet2, square)
        pygame.draw.rect(screen, alet2, bar1)
        pygame.draw.rect(screen, alet2, bar2)
        pygame.draw.rect(screen, alet2, ret6)
        pygame.draw.rect(screen, alet2, ret7)
        pygame.draw.rect(screen, alet2, ret8)
        pygame.draw.rect(screen, alet2, ret9)
        pygame.draw.rect(screen, alet2, ret10)
        pygame.draw.rect(screen, alet2, ret11)
        pygame.draw.rect(screen, white, suport1)
        pygame.draw.rect(screen, white, suport2)
        screen.blit(text2, (550, 500))
        pygame.display.update()

    pygame.quit()


main()
