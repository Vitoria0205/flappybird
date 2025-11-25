import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho
        
        # pygame.font.init() - Inicialização de fonte para utilizarmos
        pygame.font.init()
        self.fonte = pygame.font.Font(None, self.tamanho)  # Cria uma fonte para utilizarmos passando o tipo de fonte que não temos e o tamanho dela
        # False serve para o pygame deixar as bordas mais suaves, porém não utilizaremos essa recurso
        self.imagemTexto = self.fonte.render(self.texto, False, self.cor)
    
    def desenhar(self):
        # Função blit serve para desenhar uma imagem na tela, note que o 2 desenhar que desenha a cena e o jogador
        self.tela.blit(self.imagemTexto, self.posicao)
    
    def atualizarTexto(self, novoTexto):
        # Atualiza o texto e renderiza a imagem com o novo texto
        self.texto = novoTexto
        self.imagemTexto = self.fonte.render(self.texto, False, self.cor)