import pygame
import random
from jogador import Jogador 
from obstaculos import Obstaculos
from ob import Ob
import time

#configurações iniciais 
pygame.init()
clock = pygame.time.Clock()

pygame.mixer.music.load("sons/musica_do_jogo.mp3")

pygame.mixer.music.play(-1)

#Ciar Tela 
tela = pygame.display.set_mode((1200,700)) #RES da tela

pygame.display.set_caption("Jogo Pegue as Frutas - [EXECUTANDO]") #Nome da janela 

#Criando Personagem
personagem = Jogador("imagens/personagem.png",250, 190, 450, 540,"sons/comendo.mp3")
personagem2 = Jogador("imagens/personagem.png",150, 100, 300, 590,"sons/no.mp3")
personagem3 = Jogador("imagens/personagem.png",150, 100, 300, 590,"sons/vitoria.mp3")
inicial = Jogador("imagens/detalhes.png",150, 100, 300, 590,"sons/vitoria.mp3")
som = Jogador("imagens/detalhes.png",150, 100, 300, 590,"sons/vitoria.mp3")

trofeu = pygame.image.load("imagens/trofeu.png")
trofeu = pygame.transform.scale(trofeu, (100, 100)) 

estrela = pygame.image.load("imagens/estrela.png")
estrela = pygame.transform.scale(estrela, (100, 100)) 

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
            Ob("imagens/raio.png",110,100),
            Ob("imagens/snake.png",75,75),
            Ob("imagens/bomb.png",75,75),
            Ob("imagens/raio.png",75,75),
            Ob("imagens/snake.png",75,75),
            Ob("imagens/bomb.png",75,75)]

inicial = pygame.image.load("imagens/detalhes.png")
inicial = pygame.transform.scale(inicial, (1200, 700))

fonte = pygame.font.SysFont("Berlin Sans FB Demi",50,True,False)  # Fonte do placar
fonte2 = pygame.font.SysFont("Berlin Sans FB Demi",50,True,False)  # Fonte do placar

#Criando fundo
fundo = pygame.image.load("imagens/floresta.png")  # Importando Imagem
fundo = pygame.transform.scale(fundo, (1200, 700))  # Ajustando o tamanho da imagem para caber na tela

estado = "DETALHES"
estado2 = False
rodando = True
jogo_rodando = False
poder = False
poder_usos = 3
contador_tempo = 0

while rodando: # A variavel rodando ira controlar o tempo de jogo 
    for evento in pygame.event.get(): # Pega a lista de eventos feito e percorre
        if evento.type == pygame.QUIT: #Quado quiser sair do jogo, botão de fechar 
            rodando = False
        if evento.type == pygame.KEYDOWN:
             if evento.key == pygame.K_RETURN:
                  estado = "JOGANDO"

        if evento.type == pygame.KEYDOWN: #Vau ver se alguma tecla foi pressionada  
            if evento.key == pygame.K_SPACE and poder_usos > 0:  #Se foi confere se foi o enter e se for o poder usos diminui 1
                 poder = True
                 poder_usos -= 1  


    if estado == "DETALHES":
        tela.blit(inicial,(0,0))

    if estado == "JOGANDO":
        tela.fill((255,0,0))

        tela.blit(fundo,(0,0))
        tela.blit(personagem.imagem,(personagem.pos_x,personagem.pos_y))#Selecionando a imagem que ira até a cordenada 

        tela.blit(trofeu,(16, 30)) 
        tela.blit(estrela,(1075, 29))
        
        personagem.movimentar(pygame.K_RIGHT,
                                pygame.K_LEFT,)
        if poder == True:
             contador_tempo += 1 

             if contador_tempo >= 195:
                  poder = False
                  contador_tempo = 0 
  
                  
                #inimigo
        for obstaculo in lista_obstaculo:
                if poder == False:
                    obstaculo.movimentar()
                obstaculo.desenhar(tela)

                if personagem.mascara.overlap(obstaculo.mascara, (obstaculo.pos_x-personagem.pos_x,obstaculo.pos_y-personagem.pos_y)):
                    obstaculo.pos_y = obstaculo.pos_inicial_y
                    personagem.pontuacao += 1
                    personagem.som.play()

        for obs in lista_ob:
                if poder == False:
                    obs.movimentar()
                obs.desenhar(tela)

                if personagem.mascara.overlap(obs.mascara, (obs.pos_x-personagem.pos_x,obs.pos_y- personagem.pos_y)):
                    obs.pos_y = obs.pos_inicial_y
                    personagem.pontuacao -= 1 
                    personagem2.som.play()

                #Placar homem
                placar_cara = fonte.render(f"{personagem.pontuacao}", True, (255,255,255))
                tela.blit(placar_cara,(120,60))

                placar_poder = fonte2.render(f"{poder_usos}", True, (255,255,255))
                tela.blit(placar_poder,(1050,60))
            
                if personagem.pontuacao == 10:
                    estado = "FIM DE JOGO"

                if personagem.pontuacao == -10:
                    estado = True

    elif estado == "FIM DE JOGO":
            vitoria = pygame.image.load("imagens/win.png")
            vitoria = pygame.transform.scale(vitoria,(1200,700)) #Tamanho que a imagem sera mostrada 
            tela.blit(vitoria,(0,0))
            personagem3.som.play()

    elif estado == True:
        vitoria2 = pygame.image.load("imagens/derrota.png")
        vitoria2 = pygame.transform.scale(vitoria2,(1200,700)) #Tamanho que a imagem sera mostrada 
        tela.blit(vitoria2,(0,0))


    pygame.display.update()

    clock.tick(65)







    
