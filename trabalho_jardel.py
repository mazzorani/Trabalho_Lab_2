import random
import time

 # aqui criamos o tabuleiro pela tamanho fornecido pelo usuario
def criar_tabuleiro(altura, largura):
    total_pares = (altura * largura) // 2
    numeros = list(range(1, total_pares + 1)) * 2
    random.shuffle(numeros)
    tabuleiro = []
    for i in range(altura):
        linha = []
        for j in range(largura):
            if numeros:
                linha.append(numeros.pop())
        tabuleiro.append(linha)
    return tabuleiro

 # aqui faz a impresao do tabuleiro 
def imprimir_tabuleiro(tabuleiro, mostrados):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if (i, j) in mostrados:
                print(tabuleiro[i][j], end='\t')
            else:
                print('?', end='\t')
        print()

# aui comeca o jogo 
def jogar():
    nome = input("Digite seu nome: ")
    score = 1000
    reiniciar = True

    while reiniciar:
        print("Bem-vindo, {}! Vamos jogar!".format(nome))
        print("Pontuação inicial: {}".format(score))
        print("")
        
        #pergunta tamanho do tabuleiro

        tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro (um número divisível por 2): "))
        altura = largura = tamanho_tabuleiro

        # se nao for divisivel por 2 nao passa

        if altura % 2 != 0:
            print("O tamanho do tabuleiro deve ser um número divisível por 2.")
            continue

        tabuleiro = criar_tabuleiro(altura, largura)
        mostrados = set()
        total_pares = (altura * largura) // 2
        pares_encontrados = 0
        tentativas = 0

        # mostrar o tabueiro virado para a pessoa ver os pares
        print("Pares de números:")
        imprimir_tabuleiro(tabuleiro, {(i, j) for i in range(altura) for j in range(largura)})
        print("")

        # aqui mostra 5 segundos do tabuleiro virado para mostrar pros 6
        print("Aguarde 5 segundos...")
        time.sleep(5)
        print("")

        # desvirar ele 
        imprimir_tabuleiro(tabuleiro, mostrados)
        print("")

        while pares_encontrados < total_pares and score > 0:
            print("Pontuação atual: {}".format(score))
            print("")

            linha1 = int(input("Escolha uma linha (1 a {}): ".format(altura)))
            coluna1 = int(input("Escolha uma coluna (1 a {}): ".format(largura)))

            primeira_escolha = (linha1 - 1, coluna1 - 1)

            if primeira_escolha in mostrados:
                print("Essa posição já foi revelada!")
                imprimir_tabuleiro(tabuleiro, mostrados)
                continue

            if linha1 < 1 or coluna1 < 1 or linha1 > altura or coluna1 > largura:
                print("Posição inválida!")
                continue

            numero1 = tabuleiro[linha1 - 1][coluna1 - 1]
            mostrados.add(primeira_escolha)

            # carta virada 1
            imprimir_tabuleiro(tabuleiro, mostrados)
            print("")

            linha2 = int(input("Escolha outra linha (1 a {}): ".format(altura)))
            coluna2 = int(input("Escolha outra coluna (1 a {}): ".format(largura)))

            segunda_escolha = (linha2 - 1, coluna2 - 1)

            if segunda_escolha in mostrados:
                print("Essa posição já foi revelada!")
                imprimir_tabuleiro(tabuleiro, mostrados)
                continue

            if linha2 < 1 or coluna2 < 1 or linha2 > altura or coluna2 > largura:
                print("Posição inválida!")
                continue

            numero2 = tabuleiro[linha2 - 1][coluna2 - 1]
            mostrados.add(segunda_escolha)

            # carta virada 2
            imprimir_tabuleiro(tabuleiro, mostrados)
            print("")

            tentativas += 1

            if numero1 == numero2:
                print("Par encontrado!")
                pares_encontrados += 1
            else:
                score -= 50
                print("Os números não são iguais. -50 pontos!")

                # Desvirar as cartas
                mostrados.remove(primeira_escolha)
                mostrados.remove(segunda_escolha)

        # verificar se o jogador venceu ou perdeu
        if score <= 0:
            print("Pontuação final: {}".format(score))
            print("Você perdeu! Tente novamente.")
        elif pares_encontrados == total_pares:
            print("Parabéns, {}! Você venceu!".format(nome))

        # colocar o nome e pontuação no arquivo
        ranking = {}
        try:
            with open("ranking.txt", "r") as file:
                for linha in file:
                    nome_pontuacao = linha.strip().split(": ")
                    ranking[nome_pontuacao[0]] = int(nome_pontuacao[1])
        except FileNotFoundError:
            pass

        if nome in ranking and ranking[nome] >= score:
            print("Sua pontuação não é alta o suficiente para entrar no ranking.")
        else:
            ranking[nome] = score
            with open("ranking.txt", "w") as file:
                for nome, pontuacao in ranking.items():
                    file.write("{}: {}\n".format(nome, pontuacao))

        reiniciar_jogo = input("Deseja jogar novamente? (s/n): ")
        if reiniciar_jogo.lower() != 's':
            reiniciar = False

    exibir_ranking()


def exibir_ranking():
    try:
        with open("ranking.txt", "r") as file:
            ranking = [linha.strip() for linha in file]
            if ranking:
                print("Ranking:")
                for linha in ranking:
                    print(linha)
            else:
                print("Ainda não há pontuações registradas.")
    except FileNotFoundError:
        print("Ainda não há pontuações registradas.")

    # Esperar pela entrada do usuário para voltar ao menu principal
    input("Pressione Enter para voltar ao menu...")
    main()

 # menu do jogo
def main():
    while True:
        print("Jogo da Memória Tche")
        print("Escolha uma opção:")
        print("1. Jogar")
        print("2. Exibir ranking")
        print("3. Sair")

        opcao = input("Opção: ")
        if opcao == '1':
            jogar()
        elif opcao == '2':
            exibir_ranking()
        elif opcao == '3':
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


main()
