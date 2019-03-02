from random import randint

def initJogo():
    print("Henrique Nóbrega Grigolli - 41821661 - 02N11")
    matrizJogo = matrizInicial()
    imprimeMatriz(matrizJogo)
    k = 0
    flag = False
    while(k < 5):
        p1 = jogadorO()
        p1i = p1[0]
        p1j = p1[1]
        if(verificaCasa(p1i,p1j,matrizJogo)):
            insereO(p1i,p1j,matrizJogo)
        else:
                while(not verificaCasa(p1i,p1j,matrizJogo)):
                    print("Casa ocupada, escolha outra casa")
                    p1 = jogadorO()
                    p1i = p1[0]
                    p1j = p1[1]
                insereO(p1i,p1j,matrizJogo)

        imprimeMatriz(matrizJogo)

        if(verificaGanhador(matrizJogo,'O')):
            flag = True
            print("O jogador O é o vencedor!")
            break

        #Como são 9 jogadas e cada iteração possui duas jogadas, 
        # na iteração k = 4 restará uma ultima casa e então deve-se dar um break 
        # e sair do loop depois que o jogador O jogar

        if(k == 4):
            break

        p2 = jogadorX()
        p2i = p2[0]
        p2j = p2[1]
        if(verificaCasa(p2i,p2j,matrizJogo)):
            insereX(p2i,p2j,matrizJogo)
        else:
            while(not verificaCasa(p2i,p2j,matrizJogo)):
                print("Casa ocupada, escolha outra casa")
                p2 = jogadorX()
                p2i = p2[0]
                p2j = p2[1]
            insereX(p2i,p2j,matrizJogo)

        imprimeMatriz(matrizJogo)

        k += 1

        if(verificaGanhador(matrizJogo,'X')):
            flag = True
            print("O jogador X é o vencedor!")
            break

    if(not flag):
        print("Deu velha!!")


def matrizInicial():
    linhaLen = 3
    colunaLen = 3
    matrizJogo = []
  
    for i in range(linhaLen):
        linha = []
        for j in range(colunaLen):
            linha = linha + ["*"]
        matrizJogo = matrizJogo + [linha]

    return matrizJogo


def verificaCasa(i,j,matriz):
    if(matriz[i][j] == '*'):
        return True
    else:
        return False
  
def insereX(i, j, matriz):
    matriz[i][j] = 'X'
  
def insereO(i, j, matriz):
    matriz[i][j] = 'O'
  

def imprimeMatriz(matriz):
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='')
        print()
    print()

def verificaDiagPrincipal(matriz, jogador):
    count = 0
    for i in range(len(matriz)):
        if(matriz[i][i] == jogador):
            count += 1
        if(count == 3):
            return True

    return False

      
def verificaDiagSecundaria(matriz, jogador):
    count = 0
    j = len(matriz)-1
    for i in range(len(matriz)):
        if(matriz[i][j-i] == jogador):
            count += 1
        if(count == 3):
            return True
  
    return False
      
def verificaLinha(matriz, jogador):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(len(matriz)):
        if(matriz[0][i] == jogador):
            count0 += 1
        if(matriz[1][i] == jogador):
            count1 += 1
        if(matriz[2][i] == jogador):
            count2 += 1           
        if(count0 == 3 or count1 == 3 or count2 == 3):
            return True
          
    return False

def verificaColuna(matriz, jogador):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(len(matriz)):
        if(matriz[i][0] == jogador):
            count0 += 1
        if(matriz[i][1] == jogador):
            count1 += 1
        if(matriz[i][2] == jogador):
            count2 += 1           
        if(count0 == 3 or count1 == 3 or count2 == 3):
            return True
          
    return False

def verificaGanhador(matriz, jogador):
    return (verificaDiagPrincipal(matriz, jogador) 
        or verificaDiagSecundaria(matriz, jogador) 
        or verificaLinha(matriz, jogador) 
        or verificaColuna(matriz, jogador) )

def jogadorO():
    print("Vez do jogador O")
    i = int(input("Qual posição deseja jogar? (i): "))
    if(i > 2 or i < 0):
        print("Valor invalido")
        i = int(input("Qual posição deseja jogar? (i): "))
      
    j = int(input("Qual posição deseja jogar? (j): "))
    if(j > 2 or j < 0):
        print("Valor invalido")
        j = int(input("Qual posição deseja jogar? (j): "))
    print()

    ## Comentar as linhas de cima e descomentar as de baixo para preencher automaticamente
    #i = randint(0, 2)
    #j = randint(0, 2)
    
    return [i,j]

def jogadorX():
    print("Vez do jogador X")
  
    i = int(input("Qual posição deseja jogar? (i): "))
    if(i > 2 or i < 0):
        print("Valor invalido")
        i = int(input("Qual posição deseja jogar? (i): "))

    j = int(input("Qual posição deseja jogar? (j): "))
    if(j > 2 or j < 0):
        print("Valor invalido")
        j = int(input("Qual posição deseja jogar? (j): "))

    ## Comentar as linhas de cima e descomentar as de baixo para preencher automaticamente
    #i = randint(0, 2)
    #j = randint(0, 2)

    return [i,j]



initJogo()
