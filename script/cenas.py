from script.cano import Cano
from script.jogador import Jogador
from script.interfaces import Texto, Botao

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "FlappyBird", 100, 20, (255, 255, 255), 50)
        self.estado = "menu"
        self.botao_jogar = Botao(tela, "Jogar", 100, 100, 30, (0, 150, 0))

    def atualizar(self):
        if self.botao_jogar.get_click():
            self.estado = "partida"
        return self.estado

    def desenhar(self):
        self.titulo.desenhar()
        self.botao_jogar.desenhar()


class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = "partida"
        self.pontos_valor = 0
        self.contador = 0
        self.pontos_texto = Texto(tela, "0", 10, 10, (255, 255, 255), 30)

    def atualizar(self):
        self.jogador.atualizar()
        self.cano.atualizar()

        self.contador += 1
        if self.contador > 60:
            self.pontos_valor += 1
            self.contador = 0
            self.pontos_texto.atualizar_texto(str(self.pontos_valor))

        if self.cano.detectar_colisao(self.jogador.get_rect()):
            self.estado = "menu"
            self.jogador.posicao = [100, 100]
            self.cano.x = self.tela.get_width() + 50
            self.pontos_valor = 0
            self.pontos_texto.atualizar_texto("0")

        return self.estado

    def desenhar(self):
        self.jogador.desenhar()
        self.cano.desenhar()
        self.pontos_texto.desenhar()