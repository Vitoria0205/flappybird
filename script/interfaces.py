import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho

        if not pygame.font.get_init():
            pygame.font.init()

        self.fonte = pygame.font.Font(None, self.tamanho)
        self.imagem_texto = self.fonte.render(self.texto, True, self.cor)

    def desenhar(self):
        self.tela.blit(self.imagem_texto, self.posicao)

    def atualizar_texto(self, novo_texto):
        self.texto = novo_texto
        self.imagem_texto = self.fonte.render(self.texto, True, self.cor)


class Botao:
    def __init__(self, tela, texto, x, y, tamanho, cor_fundo):
        self.tela = tela
        self.texto_objeto = Texto(tela, texto, x, y, (255, 255, 255), tamanho)
        self.cor_fundo = cor_fundo

        largura = self.texto_objeto.imagem_texto.get_width() + 20
        altura = self.texto_objeto.imagem_texto.get_height() + 10
        self.rect = pygame.Rect(x, y, largura, altura)

    def desenhar(self):
        pygame.draw.rect(self.tela, self.cor_fundo, self.rect)
        self.texto_objeto.desenhar()

    def get_click(self):
        posicao_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(posicao_mouse) and pygame.mouse.get_pressed()[0]:
            return True
        return False