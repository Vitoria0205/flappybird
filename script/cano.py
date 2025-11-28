import pygame
import random

class Cano:
    def __init__(self, tela):
        self.tela = tela
        self.imagem = pygame.image.load('assets/cano.png')
        self.imagem = pygame.transform.scale(self.imagem, (60, 400))
        self.x = tela.get_width() + 50  # começa fora da tela
        self.distancia = 180
        self.velocidade = 2

        self.y_baixo = random.randint(200, self.tela.get_height() - 50)
        self.y_cima = self.y_baixo - self.distancia - self.imagem.get_height()

    def atualizar(self):
        self.x -= self.velocidade
        if self.x < -self.imagem.get_width():
            self.x = self.tela.get_width() + 50
            self.y_baixo = random.randint(200, self.tela.get_height() - 50)
            self.y_cima = self.y_baixo - self.distancia - self.imagem.get_height()

    def desenhar(self):
        imagem_invertida = pygame.transform.flip(self.imagem, False, True)
        self.tela.blit(imagem_invertida, (self.x, self.y_cima))
        self.tela.blit(self.imagem, (self.x, self.y_baixo))

    def detectar_colisao(self, rect_jogador):
        rect_cima = pygame.Rect(self.x, self.y_cima, self.imagem.get_width(), self.imagem.get_height())
        rect_baixo = pygame.Rect(self.x, self.y_baixo, self.imagem.get_width(), self.imagem.get_height())
        return rect_jogador.colliderect(rect_cima) or rect_jogador.colliderect(rect_baixo)