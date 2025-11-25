import pygame
from scripts.cenas import Partida
from scripts.cenas import Menu  # Importamos a cena 'Menu'

pygame.init()

tamanhoTela = [600, 400]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("FlappyBird Clone")
relogio = pygame.time.Clock()
corFundo = (86, 140, 214)

# Dicionário que associa uma string (texto, indicado por "") com uma classe que no caso é Partida
listaCenas = {
    'partida': Partida(tela),
    'menu': Menu(tela)  # Adicionamos o menu na cena
}

cenaAtual = 'menu'  # Mudamos para menu

# Loop principal do jogo
while True:
    # Captura eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Chamamos o dicionário listaCenas[cenaAtual] para acessar 'cenaAtual': que no caso é partida, e chamamos a função para
    # atualizar devolvendo um valor indicando a cena nova, então pegamos esse valor e atribuímos a variável 'cenaAtual'
    cenaAtual = listaCenas[cenaAtual].atualizar()
    
    # Preenche o fundo com a cor definida
    tela.fill(corFundo)
    
    # Desenha a cena atual
    listaCenas[cenaAtual].desenhar()
    
    # Atualiza a tela
    relogio.tick(60)
    pygame.display.flip()