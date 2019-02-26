from random import randint
from string import ascii_lowercase as al

class Embarcacao:
       def __init__(self, nome, tamanho):
           self.nome = nome
           self.tamanho = tamanho

PORTA_AVIOES = Embarcacao("PORTA AVIÕES",5)
ENCOURACADO = Embarcacao("ENCOURAÇADO",4)
CRUZADOR = Embarcacao("CRUZADOR",3)
SUBMARINO = Embarcacao("SUBMARINO",2)

def initJogo():
    print("Henrique Nóbrega Grigolli - 41821661 - 02N11")
    print("\n\tBatalha Naval!")
    matrizJogo = matrizInicial()
    imprimeMatriz(matrizJogo)
    insereNavio(matrizJogo, PORTA_AVIOES, [1,10], True)
    insereNavio(matrizJogo, ENCOURACADO, [2,7], False)
    imprimeMatriz(matrizJogo)


def matrizInicial():
    linhaLen = 11
    colunaLen = 11
    matrizJogo = []

    linha = [" "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "," 10 "]
    matrizJogo = matrizJogo + [linha]
    for i in range(1,linhaLen):
        linha = [al[i-1]]
        for j in range(1,colunaLen):
            linha = linha + [" . "]
        matrizJogo = matrizJogo + [linha]

    return matrizJogo

def imprimeMatriz(matriz):
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(" " + matriz[i][j] + " ", end='')
        print()
    print()


def insereNavio(matriz, navio, posicao, isVertical):
    if(isVertical):
        if(verificaPosicao(matriz, navio, posicao, isVertical)):
            print("Posição Inválida para o ", navio.nome)
        else:
            for i in range(navio.tamanho):
                matriz[posicao[0] + i][posicao[1]] = " " + navio.nome[0] + " "
    else:
        if(verificaPosicao(matriz, navio, posicao, isVertical)):
            print("Posição Inválida para o ", navio.nome)
        else:
            for j in range(navio.tamanho):
                matriz[posicao[0]][posicao[1] + j] = " " + navio.nome[0] + " "

def verificaPosicao(matriz, navio, posicao, isVertical):
    
    if(isVertical):
        if(posicao[0] + navio.tamanho > 10):
            return True
        else:
            for i in range(navio.tamanho):
                if(matriz[posicao[0] + i][posicao[1]] != " . "):
                    return True
    else:
        if(posicao[1] + navio.tamanho > 10):
            return True
        else:
            for j in range(navio.tamanho):
                   if(matriz[posicao[0]][posicao[1] + j] != " . "):
                       return True
    return False

initJogo()
