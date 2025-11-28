import pygame
from script.cenas import Menu

pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("FlappyBird Clone")
relogio = pygame.time.Clock()
cor_fundo = (86, 148, 214)

cena_atual = "menu"
menu = Menu(tela)
partida = None  # será criada quando necessário

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    if cena_atual == "menu":
        cena_atual = menu.atualizar()
        if cena_atual == "partida":
            # Cria uma nova partida ao clicar em "Jogar"
            from script.cenas import Partida
            partida = Partida(tela)
    elif cena_atual == "partida":
        cena_atual = partida.atualizar()

    tela.fill(cor_fundo)

    if cena_atual == "menu":
        menu.desenhar()
    elif cena_atual == "partida":
        partida.desenhar()

    pygame.display.flip()
    relogio.tick(60)