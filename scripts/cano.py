import pygame
import random   # usado para gerar alturas aleatórias

# Classe que representa os canos do jogo
class Canos:
    def __init__(self, tela):
        self.tela = tela

        # Carrega a imagem do cano
        self.imagem = pygame.image.load('assets/cano.png')

        # Distância entre o cano de cima e o cano de baixo
        self.distancia = 100

        # Altura onde vai ficar a abertura por onde o jogador passa
        self.altura_base = random.randint(100, 300)

        # Posição inicial do cano (começa fora da tela, à direita)
        self.x = 600

        # Calcula a posição do cano superior
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia

        # Calcula a posição do cano inferior
        self.cano_baixo = self.altura_base + self.distancia

    # Redefine a altura dos canos quando eles saem da tela
    def reset_altura(self):
        self.altura_base = random.randint(100, 300)
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        self.cano_baixo = self.altura_base + self.distancia
