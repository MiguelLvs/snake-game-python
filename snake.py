import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERDE_ESCURO = (0, 155, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Tamanho do bloco
tamanho_bloco = 20

# FPS
relogio = pygame.time.Clock()
velocidade = 10

# Fonte para pontuação
fonte = pygame.font.SysFont('Arial', 20)

# Função para desenhar a cobrinha


def desenhar_cobra(cobra):
    for i, pos in enumerate(cobra):
        cor = VERDE if i == 0 else VERDE_ESCURO
        pygame.draw.rect(tela, cor, pygame.Rect(
            pos[0], pos[1], tamanho_bloco, tamanho_bloco))

# Gera comida aleatória


def gerar_comida():
    x = random.randint(0, (largura - tamanho_bloco) //
                       tamanho_bloco) * tamanho_bloco
    y = random.randint(0, (altura - tamanho_bloco) //
                       tamanho_bloco) * tamanho_bloco
    return (x, y)

# Função principal


def jogo():
    cobra = [(100, 100)]
    direcao = (tamanho_bloco, 0)
    comida = gerar_comida()
    pontuacao = 0

    while True:
        tela.fill(PRETO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao[1] == 0:
                    direcao = (0, -tamanho_bloco)
                elif evento.key == pygame.K_DOWN and direcao[1] == 0:
                    direcao = (0, tamanho_bloco)
                elif evento.key == pygame.K_LEFT and direcao[0] == 0:
                    direcao = (-tamanho_bloco, 0)
                elif evento.key == pygame.K_RIGHT and direcao[0] == 0:
                    direcao = (tamanho_bloco, 0)

        # Atualiza posição da cabeça
        nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])

        # Verifica colisões
        if (nova_cabeca in cobra or
            nova_cabeca[0] < 0 or nova_cabeca[0] >= largura or
                nova_cabeca[1] < 0 or nova_cabeca[1] >= altura):
            texto = fonte.render("Game Over! Pontuação: " +
                                 str(pontuacao), True, BRANCO)
            tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            jogo()  # Reinicia o jogo

        cobra.insert(0, nova_cabeca)

        if nova_cabeca == comida:
            pontuacao += 1
            comida = gerar_comida()
        else:
            cobra.pop()

        desenhar_cobra(cobra)
        pygame.draw.rect(tela, VERMELHO, pygame.Rect(
            comida[0], comida[1], tamanho_bloco, tamanho_bloco))

        texto = fonte.render("Pontuação: " + str(pontuacao), True, BRANCO)
        tela.blit(texto, (10, 10))

        pygame.display.update()
        relogio.tick(velocidade)


jogo()
