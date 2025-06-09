import pygame

class Jogador: 

    def __init__(self, end_imagem, largura, altura,x_inicial, y_inicial, end_som):
            self.imagem = pygame.image.load(end_imagem)
            self.imagem = pygame.transform.scale(self.imagem,(largura, altura))
            self.mascara = pygame.mask.from_surface(self.imagem)

            self.x_inicial = x_inicial
            self.y_inicial = y_inicial

            self.pos_x = x_inicial
            self.pos_y = y_inicial

            self.largura = largura
            self.altura = altura

            #carregando o som de atropelamento
            self.som = pygame.mixer.Sound(end_som)

            #Pontuação
            self.pontuacao = 0

    def movimentar(self,tecla_direita,
                   tecla_esquerda,):
        
        teclas = pygame.key.get_pressed()

        if teclas [tecla_esquerda]:
            if self.pos_x > -100:
                self.pos_x =  self.pos_x - 5 

        if teclas [tecla_direita]:
            if self.pos_x < 1300 - self.largura:
                self.pos_x =  self.pos_x + 5
