from random import randint
from string import ascii_lowercase as al

class Embarcacao:
    atingido = 0
    naufragado = False
       
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

PORTA_AVIOES = Embarcacao("PORTA AVIÕES",5)
ENCOURACADO = Embarcacao("ENCOURAÇADO",4)
CRUZADOR = Embarcacao("CRUZADOR",3)
SUBMARINO = Embarcacao("SUBMARINO",2)

navios = [PORTA_AVIOES, ENCOURACADO, CRUZADOR, SUBMARINO]


def initJogo():
    print("Henrique Nóbrega Grigolli - 41821661 - 02N11")
    print("\n\tBatalha Naval!")
    matrizJogo = matrizInicial()
    imprimeMatriz(matrizJogo)
    posicionarNavios(matrizJogo)
    n = 40
    naufragados = 0
    for k in range(1,n+1):
        print(k)
        flag = False
        posicao = [0,0]
        while(not flag):
            i = 0
            print("Escolha para atirar!!\n")
            posicao[0] = input("Digite a linha (a - j): ")
            while(posicao[0] not in al[0:11]):
                 print("Posição inválida")
                 posicao[0] = input("Digite a linha (a - j): ")
            for c in al:
                 i += 1
                 if(c == posicao[0]):
                        posicao[0] = i
                        
            posicao[1] = int(input("Digite a coluna (1-10): "))
            while(posicao[1] < 1 or posicao[1] > 10):
                 print("Posição inválida")
                 posicao[1] = int(input("Digite a coluna (1-10): "))
            print("\n\nFogo!!!\n\n")
            flag = atirar(matrizJogo, posicao)
            for navio in navios:
                if(navio.naufragado):
                    naufragados += 1
                    
            if(naufragados == 4):
                print("Todos os navios foram naufragados!!!")
                break
            
            imprimeMatriz(matrizJogo)
            chances = n-k
            print("\nVocê tem {} chances restantes...\n".format(chances))


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
            print()
            print("Posição Inválida para o ", navio.nome)
            print()
            return True
        else:
            for i in range(navio.tamanho):
                matriz[posicao[0] + i][posicao[1]] = " " + navio.nome[0] + " "
            return False
    else:
        if(verificaPosicao(matriz, navio, posicao, isVertical)):
            print()
            print("Posição Inválida para o ", navio.nome)
            print()
            return True
        else:
            for j in range(navio.tamanho):
                matriz[posicao[0]][posicao[1] + j] = " " + navio.nome[0] + " "
            return False

def verificaPosicao(matriz, navio, posicao, isVertical):
    if(isVertical):
        if(posicao[0] + navio.tamanho > 11):
            return True
        else:
            for i in range(navio.tamanho):
                if(matriz[posicao[0] + i][posicao[1]] != " . "):
                    return True
    else:
        if(posicao[1] + navio.tamanho > 11):
            return True
        else:
            for j in range(navio.tamanho):
                if(matriz[posicao[0]][posicao[1] + j] != " . "):
                    return True
    return False


def atirar(matriz, posicao):
       if(not verificaPosicaoComTiro(matriz,posicao)):
              if(verificaPosicaoComAgua(matriz,posicao)):
                     matriz[posicao[0]][posicao[1]] = " x "
              else:
                     for navio in navios:
                            if(matriz[posicao[0]][posicao[1]] == " " + navio.nome[0] + " "):
                                   navio.atingido += 1         
                            if(navio.atingido == navio.tamanho):
                                   navio.naufragrado = True
                                   print("{} afundou!".format(navio.nome))   
                     matriz[posicao[0]][posicao[1]] = " X "
              return True
       else:
              print("Posição de tiro {} já escolhida".format(posicao))
              return False

def verificaPosicaoComTiro(matriz,posicao):
       #Retorna True se posicao já foi escolhida
       if( matriz[posicao[0]][posicao[1]] == " x " or matriz[posicao[0]][posicao[1]] == " X "):
              return True
       else:
              return False

def verificaPosicaoComAgua(matriz,posicao):
       #Retorna True se posição tem água
       if( matriz[posicao[0]][posicao[1]] == " . "):
              return True
       else:
              return False


def posicionarNavios(matriz):

    for navio in navios:
        flag = True
        posicao = [1,1]
        isVertical = False
        while(flag):
            i = 0
            print("Posicionando a Embarcação: {}".format(navio.nome))
            posicao[0] = input("Digite a linha (a - j): ")
            while(posicao[0] not in al[0:11]):
                 print("Posição inválida")
                 posicao[0] = input("Digite a linha (a - j): ")
            for c in al:
                 i += 1
                 if(c == posicao[0]):
                        posicao[0] = i
                        
            posicao[1] = int(input("Digite a coluna (1-10): "))
            while(posicao[1] < 1 or posicao[1] > 10):
                 print("Posição inválida")
                 posicao[1] = int(input("Digite a coluna (1-10): "))

                 
            isVertical = input("Digite V para posição Vertical ou H para Horizontal: ")
            while(isVertical.upper() != "V" and isVertical.upper() != "H"):
                 print("Direção inválida")
                 print(isVertical.upper() != "V" and isVertical.upper() != "H")
                 isVertical = input("Digite V para posição Vertical ou H para Horizontal: ")

            if(isVertical.upper() == "V"):
                 isVertical = True
                 flag = insereNavio(matriz, navio, posicao, isVertical)
            else:
                 isVertical = False
                 flag = insereNavio(matriz, navio, posicao, isVertical)
            print(navio.nome)

        imprimeMatriz(matriz)




initJogo()
