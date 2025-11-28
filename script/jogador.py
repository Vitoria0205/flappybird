import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = [32, 32]

        self.contador = 0
        self.imagem_atual = 0
        self.lista_imagens = []

        for i in range(3):
            try:
                imagem = pygame.image.load(f'assets/passaro-{i}.png')
                imagem = pygame.transform.scale(imagem, self.tamanho)
                self.lista_imagens.append(imagem)
            except Exception as e:
                print(f"Erro ao carregar assets/passaro-{i}.png: {e}")
                fallback = pygame.Surface(self.tamanho)
                fallback.fill((255, 0, 0))
                self.lista_imagens.append(fallback)

        self.velocidade_atual = 0
        self.gravidade = 0.25
        self.velocidade_maxima = 8

    def desenhar(self):
        self.contador += 1
        if self.contador > 5:
            self.contador = 0
            self.imagem_atual = (self.imagem_atual + 1) % 3
        self.tela.blit(self.lista_imagens[self.imagem_atual], self.posicao)

    def atualizar(self):
        self.velocidade_atual += self.gravidade
        self.velocidade_atual = min(self.velocidade_atual, self.velocidade_maxima)
        self.posicao[1] += self.velocidade_atual

        # Limita na tela
        altura_tela = self.tela.get_height()
        if self.posicao[1] < 0:
            self.posicao[1] = 0
            self.velocidade_atual = 0
        if self.posicao[1] > altura_tela - self.tamanho[1]:
            self.posicao[1] = altura_tela - self.tamanho[1]
            self.velocidade_atual = 0

        # Pulo com ESPAÇO
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            self.velocidade_atual = -self.velocidade_maxima

    def get_rect(self):
        return pygame.Rect(self.posicao[0], self.posicao[1], self.tamanho[0], self.tamanho[1])