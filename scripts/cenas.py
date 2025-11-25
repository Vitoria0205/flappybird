import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto  # Importando texto

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = 'menu'
    
    def atualizar(self):
        self.estado = 'menu'
        self.titulo.desenhar()
        
        return self.estado


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "FlappyBird", 100, 20, (255, 255, 255), 50)
        self.estado = 'menu'  # Estado atual da partida, indicando se está no jogo ou no menu
    
    def atualizar(self):
        self.estado = 'menu'  # Redefinimos todo o estado para "partida" a cada atualização
        self.titulo.desenhar()
        
        return self.estado