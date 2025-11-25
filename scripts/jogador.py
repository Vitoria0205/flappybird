import pygame

# Classe Jogador
class Jogador:
    def __init__(self, tela, x, y):
        # Posição inicial do jogador
        self.posicao = [x, y]

        # Tamanho do jogador (largura, altura)
        self.tamanho = [32, 32]

        # Retângulo de colisão
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        # Variável para controlar a troca das imagens (animação)
        self.contador = 0

        # Índice da imagem atual
        self.imagemAtual = 0

        # Tela onde o jogador será desenhado
        self.tela = tela

        # Lista que vai guardar as imagens do jogador
        self.listaImagens = []

        # Carrega e armazena 3 imagens na lista
        for i in range(3):
            imagem = pygame.image.load(f'assets/passaro-{i}.png')
            imagem = pygame.transform.scale(imagem, self.tamanho)
            self.listaImagens.append(imagem)

        # Variáveis de física do jogador
        self.velocidadeAtual = 0
        self.gravidade = 1 / 60 * 10
        self.velocidadeMaxima = 1 / 60 * 100

    # Desenha o jogador na tela
    def desenhar(self):
        # Controle da velocidade da animação
        self.contador += 1
        if self.contador > 5:          # Troca de frame a cada 6 updates
            self.contador = 0
            self.imagemAtual = (self.imagemAtual + 1) % 3  # Alterna entre 0, 1 e 2

        # Desenha a imagem atual na tela
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    # Atualiza posição, gravidade e pulo
    def atualizar(self):
        # Aplicar gravidade (limitada por velocidade máxima)
        self.velocidadeAtual = min(
            self.velocidadeAtual + self.gravidade,
            self.velocidadeMaxima
        )

        # Atualizar posição vertical
        self.posicao = [
            self.posicao[0],
            self.posicao[1] + self.velocidadeAtual
        ]

        # Atualizar rect para colisão
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        # Verificar tecla de pulo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:          # Se apertou espaço
            self.velocidadeAtual = -self.velocidadeMaxima / 2  # Faz subir

    # Retorna o rect para colisão
    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)
