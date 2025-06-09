import pygame 
import random

class Ob:

    def __init__(self, end_imagem, largura, altura):
        
        #config tamanho da figura
        self.largura = largura
        self.altura = altura

        #carregando imagem
        self.imagem = pygame.image.load(end_imagem)
        self.imagem = pygame.transform.scale(self.imagem,(self.largura, self.altura))
        self.mascara = pygame.mask.from_surface(self.imagem)

        #Posião do obstaculo

        self.lista_faixass = [600, 650, 200, 400, 800, 1000, 50, 300, 850, 1100]
        self.pos_x = random.choice(self.lista_faixass)
        #x
        self.pos_inicial_y = -100
        self.pos_y = self.pos_inicial_y

        #y

        self.numero = random.randint(10, 12)

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x, self.pos_y))

    def movimentar(self):
        self.pos_y += self.numero
        if self.pos_y > 900:
            self.pos_y = self.pos_inicial_y
            self.pos_x = random.choice(self.lista_faixass)
            self.numero = random.randint(1, 10)
            numero = random.random()
