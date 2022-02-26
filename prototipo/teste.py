import pygame
import sys
from pygame.locals import *
from InimigoPessoa import InimigoPessoa
from InimigoObstaculo import InimigoObstaculo
from Coordenada import Coordenada
from Tamanho import Tamanho
import time

pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((640, 480))

pygame.display.set_caption("TESTE")

carinha = InimigoPessoa(Coordenada(20, 30), 100, 100)
carrinho = InimigoObstaculo([Coordenada(100, 50), Coordenada(
    10, 20), Coordenada(90, 400)])

timer_font = pygame.font.Font("freesansbold.ttf", 38)
timer_sec = 60
timer_text = timer_font.render("01:00", True, (255, 255, 255))
timer_rect = timer_text.get_rect()

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1000)

while True:
    DISPLAYSURF.fill((0, 0, 0))

    carinha.desenhar(DISPLAYSURF)
    carrinho.desenhar(DISPLAYSURF)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == timer:    # checks for timer event
            if timer_sec > 0:
                timer_sec -= 1
                timer_text = timer_font.render(time.strftime(
                    '%M:%S', time.gmtime(timer_sec)), True, (255, 255, 255))
            else:
                pygame.time.set_timer(timer, 0)

    DISPLAYSURF.blit(timer_text, (300, 20))
    pygame.display.update()
    FramePerSec.tick(FPS)


# clock
timer_font = pygame.font.Font("04B_19__.ttf", 38)
timer_sec = 60
timer_text = timer_font.render("01:00", True, (255, 255, 255))

timer = pygame.USEREVENT + 1
# sets timer with USEREVENT and delay in milliseconds
pygame.time.set_timer(timer, 1000)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == timer:    # checks for timer event
            if timer_sec > 0:
                timer_sec -= 1
                timer_text = timer_font.render(
                    "00:%02d" % timer_sec, True, (255, 255, 255))
            else:
                pygame.time.set_timer(timer, 0)    # turns off timer event

# add another "if timer_sec > 0" here if you want the timer to disappear after reaching 0
    screen.blit(timer_text, (300, 20))
