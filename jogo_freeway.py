import pygame
import random
from jogador import Jogador 
from obstaculos import Obstaculos
from ob import Ob

#configurações iniciais 
pygame.init()
clock = pygame.time.Clock()

#Ciar Tela 
tela = pygame.display.set_mode((1200,700)) #RES da tela

pygame.display.set_caption("Jogo Pegue as Frutas - [EXECUTANDO]") #Nome da janela 

#Criando Personagem
personagem = Jogador("imagens/personagem.png",150, 100, 300, 590,"sons/comendo.mp3")
personagem2 = Jogador("imagens/personagem.png",150, 100, 300, 590,"sons/no.mp3")

#Criando Obstaculos
lista_obstaculo = [Obstaculos("imagens/fruta1.png",70,70),
                   Obstaculos("imagens/fruta2.png",90,90),
                   Obstaculos("imagens/fruta3.png",90,90),
                   Obstaculos("imagens/fruta4.png",110,110),
                   Obstaculos("imagens/fruta5.png",90,90),
                   Obstaculos("imagens/fruta1.png",70,70),
                   Obstaculos("imagens/fruta2.png",90,90),
                   Obstaculos("imagens/fruta3.png",90,90)]

lista_ob = [Ob("imagens/raio.png",75,75),
            Ob("imagens/snake.png",75,75),
            Ob("imagens/bomb.png",75,75),
            Ob("imagens/raio.png",75,75),
            Ob("imagens/snake.png",75,75),
            Ob("imagens/bomb.png",75,75)]

fonte = pygame.font.SysFont("Berlin Sans FB Demi",30,True,False)  # Fonte do placar
fonte2 = pygame.font.SysFont("Berlin Sans FB Demi",50,True,False)  # Fonte do placar

#Criando fundo
fundo = pygame.image.load("imagens/floresta.png")  # Importando Imagem
fundo = pygame.transform.scale(fundo, (1200, 700))  # Ajustando o tamanho da imagem para caber na tela

rodando = True
while rodando: # A variavel rodando ira controlar o tempo de jogo 
    for evento in pygame.event.get(): # Pega a lista de eventos feito e percorre
        if evento.type == pygame.QUIT: #Quado quiser sair do jogo, botão de fechar 
            rodando = False

    tela.blit(fundo,(0,0))

    for obstaculo in lista_obstaculo:
        obstaculo.movimentar()
        obstaculo.desenhar(tela)

    for Obs in lista_ob:
        Obs.movimentar()
        Obs.desenhar(tela)

    tela.blit(personagem.imagem,(personagem.pos_x,personagem.pos_y))#Selecionando a imagem que ira até a cordenada 

    personagem.movimentar(pygame.K_RIGHT,
                          pygame.K_LEFT,)
    
           #inimigo
    for obstaculo in lista_obstaculo:
        obstaculo.movimentar()
        obstaculo.desenhar(tela)

        if personagem.mascara.overlap(personagem.mascara, (personagem.pos_x-obstaculo.pos_x,personagem.pos_y-obstaculo.pos_y)):
           obstaculo.pos_y = obstaculo.pos_inicial_y
           personagem.pontuacao =- 1
           personagem.som.play()
        


        if personagem2.mascara.overlap(personagem2.mascara, (personagem2.pos_x-Obs.pos_x,personagem2.pos_y-Obs.pos_y)):
           Obs.pos_y = Obs.pos_inicial_y
           personagem.pontuacao =+ 1 
           personagem2.som.play()

        #Placar homem
        placar_cara = fonte.render(f"PONTOS: {personagem.pontuacao}", True, (255,255,255), (69,69,69))
        tela.blit(placar_cara,(10,10))

    
    pygame.display.update()

    clock.tick(60)







        
