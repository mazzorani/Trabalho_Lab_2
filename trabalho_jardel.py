import pygame
import random

# Definição das constantes
LARGURA_JANELA = 800
ALTURA_JANELA = 600
COR_FUNDO = (255, 255, 255)
COR_CARTA_VIRADA = (200, 200, 200)
COR_CARTA_ACERTADA = (0, 255, 0)
COR_TEXTO = (0, 0, 0)
TAMANHO_CARTA = 100
ESPAÇO_ENTRE_CARTAS = 10
LINHAS = 4
COLUNAS = 4
PONTUAÇÃO_ACERTO = 0
PONTUAÇÃO_ERRO = 50

# Inicialização do Pygame
pygame.init()
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Jogo da Memória")

# Carregamento das imagens
imagens = [pygame.image.load(f'{i}.png') for i in range(1, 9)]
random.shuffle(imagens)
imagens = imagens[:LINHAS * COLUNAS // 2] * 2
random.shuffle(imagens)

# Criação do tabuleiro
tabuleiro = [[(imagens[i * COLUNAS + j], False) for j in range(COLUNAS)] for i in range(LINHAS)]
cartas_viradas = []
cartas_acertadas = []
pontuação = 1000

# Função para exibir o tabuleiro
def exibir_tabuleiro():
    janela.fill(COR_FUNDO)
    for i in range(LINHAS):
        for j in range(COLUNAS):
            x = j * (TAMANHO_CARTA + ESPAÇO_ENTRE_CARTAS) + ESPAÇO_ENTRE_CARTAS
            y = i * (TAMANHO_CARTA + ESPAÇO_ENTRE_CARTAS) + ESPAÇO_ENTRE_CARTAS
            carta, virada = tabuleiro[i][j]
            if virada:
                pygame.draw.rect(janela, COR_CARTA_VIRADA, (x, y, TAMANHO_CARTA, TAMANHO_CARTA))
                janela.blit(carta, (x, y))
            else:
                pygame.draw.rect(janela, COR_CARTA_ACERTADA, (x, y, TAMANHO_CARTA, TAMANHO_CARTA))
    pygame.display.update()

# Função para verificar se as duas cartas viradas são iguais
def verificar_cartas():
    carta1 = None
    carta2 = None
    
    for i in range(LINHAS):
        for j in range(COLUNAS):
            carta, virada = tabuleiro[i][j]
            if virada:
                if carta1 is None:
                    carta1 = (carta, i, j)
                else:
                    carta2 = (carta, i, j)
    
    if carta1 is not None and carta2 is not None:
        if carta1[0] == carta2[0]:
            cartas_acertadas.append(carta1)
            cartas_acertadas.append(carta2)
            return True
        else:
            return False

# Função para aguardar um tempo antes de virar as cartas
def aguardar_virar_cartas():
    pygame.time.wait(1000)
    for i in range(LINHAS):
        for j in range(COLUNAS):
            carta, virada = tabuleiro[i][j]
            if virada:
                tabuleiro[i][j] = (carta, False)

# Função para exibir a pontuação na tela
def exibir_pontuação():
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(f"Pontuação: {pontuação}", True, COR_TEXTO)
    janela.blit(texto, (10, ALTURA_JANELA - 40))
    pygame.display.update()

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and len(cartas_viradas) < 2:
            pos_x, pos_y = pygame.mouse.get_pos()
            i = pos_y // (TAMANHO_CARTA + ESPAÇO_ENTRE_CARTAS)
            j = pos_x // (TAMANHO_CARTA + ESPAÇO_ENTRE_CARTAS)
            carta, virada = tabuleiro[i][j]
            if not virada and (i, j) not in cartas_acertadas:
                tabuleiro[i][j] = (carta, True)
                cartas_viradas.append((i, j))
                if len(cartas_viradas) == 2:
                    if verificar_cartas():
                        cartas_viradas.clear()
                        pontuação += PONTUAÇÃO_ACERTO
                    else:
                        aguardar_virar_cartas()
                        cartas_viradas.clear()
                        pontuação -= PONTUAÇÃO_ERRO
    exibir_tabuleiro()
    exibir_pontuação()
("trocamos de platano")
pygame.quit()
("olaaaaaaaaaaaaaaaa")