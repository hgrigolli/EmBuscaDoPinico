from math import *
import time
import turtle

height = 480
width = 854

def tela():
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgpic("images/Fundo.png")

    return screen

def mostrarLua():

    lua = turtle.Turtle()
    terra = turtle.Turtle()
    screen = tela()

    lua.penup()

    screen.addshape("images/Lua.gif")
    lua.shape("images/Lua.gif")

    screen.addshape("images/Terra.gif")
    terra.shape("images/Terra.gif")
    dt = 0
    for i in range (500):
        x = 150*cos(dt)
        y = 150*sin(dt)
        lua.setpos( x, y )
        dt += 0.025
        screen.listen()

    turtle.bye()
    turtle.TurtleScreen._RUNNING = True


	
def movimentoTerra():

    sol = turtle.Turtle()
    terra = turtle.Turtle()
    screen = tela()

    terra.penup()

    screen.addshape("images/Sol.gif")
    sol.shape("images/Sol.gif")

    screen.addshape("images/Terra.gif")
    terra.shape("images/Terra.gif")
    dt = 0
    for i in range (500):
        x = 175*cos(dt)
        y = 185*sin(dt)
        terra.setpos( x, y )
        dt += 0.025
        screen.listen()

    turtle.bye()
    turtle.TurtleScreen._RUNNING = True
	
def sistemaSolar():

    screen = tela()
    
    sol = turtle.Turtle()
    mercurio = turtle.Turtle()
    venus = turtle.Turtle()
    terra = turtle.Turtle()
    marte = turtle.Turtle()
    jupiter = turtle.Turtle()
    saturno = turtle.Turtle()
    urano = turtle.Turtle()
    netuno = turtle.Turtle()
    plutao = turtle.Turtle()

    

    astros = [sol, mercurio, venus, terra, marte, jupiter, saturno, urano, netuno, plutao]
    for astro in astros:
        astro.penup()

    screen.addshape("images/Sol.gif")
    screen.addshape("images/Mercurio.gif")
    screen.addshape("images/Venus.gif")
    screen.addshape("images/Terra.gif")
    screen.addshape("images/Marte.gif")
    screen.addshape("images/Jupiter.gif")
    screen.addshape("images/Saturno.gif")
    screen.addshape("images/Urano.gif")
    screen.addshape("images/Netuno.gif")
    screen.addshape("images/Plutao.gif")
    
    sol.shape("images/Sol.gif")
    mercurio.shape("images/Mercurio.gif")
    venus.shape("images/Venus.gif")
    terra.shape("images/Terra.gif")
    marte.shape("images/Marte.gif")
    jupiter.shape("images/Jupiter.gif")
    saturno.shape("images/Saturno.gif")
    urano.shape("images/Urano.gif")
    netuno.shape("images/Netuno.gif")
    plutao.shape("images/Plutao.gif")

    sol.setpos(-width/2, 0)
    mercurio.setpos(-width/2 + 85, 0)
    venus.setpos(-width/2 + 85*2, 0)
    terra.setpos(-width/2 + 85*3, 0)
    marte.setpos(-width/2 + 85*4, 0)
    jupiter.setpos(20, 0)
    saturno.setpos(85*1.5, 0)
    urano.setpos(85*2.7, 0)
    netuno.setpos(85*3.8, 0)
    plutao.setpos(85.4*4.8, 0)

    time.sleep(10)
    
    
    turtle.bye()
    turtle.TurtleScreen._RUNNING = True



def sistemaSolarHeliocentrico():

    screen = tela()
    
    sol = turtle.Turtle()
    mercurio = turtle.Turtle()
    venus = turtle.Turtle()
    terra = turtle.Turtle()
    marte = turtle.Turtle()
    jupiter = turtle.Turtle()
    saturno = turtle.Turtle()
    urano = turtle.Turtle()
    netuno = turtle.Turtle()
    plutao = turtle.Turtle()

    

    astros = [sol, mercurio, venus, terra, marte, jupiter, saturno, urano, netuno, plutao]
    for astro in astros:
        astro.penup()

    screen.addshape("images/Sol.gif")
    screen.addshape("images/Mercurio.gif")
    screen.addshape("images/Venus.gif")
    screen.addshape("images/Terra.gif")
    screen.addshape("images/Marte.gif")
    screen.addshape("images/Jupiter.gif")
    screen.addshape("images/Saturno.gif")
    screen.addshape("images/Urano.gif")
    screen.addshape("images/Netuno.gif")
    screen.addshape("images/Plutao.gif")
    
    sol.shape("images/Sol.gif")
    mercurio.shape("images/Mercurio.gif")
    venus.shape("images/Venus.gif")
    terra.shape("images/Terra.gif")
    marte.shape("images/Marte.gif")
    jupiter.shape("images/Jupiter.gif")
    saturno.shape("images/Saturno.gif")
    urano.shape("images/Urano.gif")
    netuno.shape("images/Netuno.gif")
    plutao.shape("images/Plutao.gif")


    sol.setpos(0, 0)
    dt = 0
    amp = 85
    for i in range (150):
        x = amp*cos(dt)
        y = amp*sin(dt)
    
        mercurio.setpos( amp*0.5*cos(dt), amp*0.5*sin(dt) )
        venus.setpos( amp*cos(dt+2), amp*sin(dt+2))
        terra.setpos(   amp*1.5*cos(dt+4), amp*1.5*sin(dt+4)  )
        marte.setpos(   amp*2*cos(dt+6), amp*2*sin(dt+6) )
        jupiter.setpos(  amp*2.5*cos(dt+5), amp*2.5*sin(dt+5) )
        saturno.setpos(  amp*3*cos(dt+12), amp*3*sin(dt+12) )
        urano.setpos(   amp*3.5*cos(dt+9), amp*3.5*sin(dt+9)  )
        netuno.setpos(  amp*4*cos(dt+14), amp*4*sin(dt+14)  )
        plutao.setpos(  amp*4.5*cos(dt+7), amp*3.5*sin(dt+7)  )
        
        dt += 0.025
        screen.listen()
        
    
    
    turtle.bye()
    turtle.TurtleScreen._RUNNING = True

def eclipseSolar():

    screen = tela()
    
    sol = turtle.Turtle()
    lua = turtle.Turtle()
    terra = turtle.Turtle()

    

    astros = [sol, terra, lua]
    for astro in astros:
        astro.penup()

    screen.addshape("images/Sol.gif")
    screen.addshape("images/Lua.gif")
    screen.addshape("images/Terra.gif")
    
    sol.shape("images/Sol.gif")
    lua.shape("images/Lua.gif")
    terra.shape("images/Terra.gif")

    sol.setpos(-200, 0)
    lua.setpos(0, 0)
    terra.setpos(200, 0)

    time.sleep(10)
    
    
    turtle.bye()
    turtle.TurtleScreen._RUNNING = True

	
def eclipseLunar():

    screen = tela()
    
    sol = turtle.Turtle()
    lua = turtle.Turtle()
    terra = turtle.Turtle()

    

    astros = [sol, terra, lua]
    for astro in astros:
        astro.penup()

    screen.addshape("images/Sol.gif")
    screen.addshape("images/Lua.gif")
    screen.addshape("images/Terra.gif")
    
    sol.shape("images/Sol.gif")
    lua.shape("images/Lua.gif")
    terra.shape("images/Terra.gif")

    sol.setpos(-200, 0)
    lua.setpos(200, 0)
    terra.setpos(0, 0)

    time.sleep(10)
    
    
    turtle.bye()
    turtle.TurtleScreen._RUNNING = True

def luaCrescente():

    screen = tela()
    
    sol = turtle.Turtle()
    lua = turtle.Turtle()
    terra = turtle.Turtle()

    

    astros = [sol, terra, lua]
    for astro in astros:
        astro.penup()

    screen.addshape("images/Sol.gif")
    screen.addshape("images/Lua.gif")
    screen.addshape("images/Terra.gif")
    
    sol.shape("images/Sol.gif")
    lua.shape("images/Lua.gif")
    terra.shape("images/Terra.gif")

    sol.setpos(-200, 0)
    lua.setpos(0, 150)
    terra.setpos(0, 0)

    time.sleep(10)
    
    
    turtle.bye()
    turtle.TurtleScreen._RUNNING = True
	
def mostraGasosos():

    screen = tela()
    
    jupiter = turtle.Turtle()
    saturno = turtle.Turtle()
    urano = turtle.Turtle()
    netuno = turtle.Turtle()

    

    astros = [jupiter, saturno, urano, netuno]
    for astro in astros:
        astro.penup()

    screen.addshape("images/Jupiter.gif")
    screen.addshape("images/Saturno.gif")
    screen.addshape("images/Urano.gif")
    screen.addshape("images/Netuno.gif")
    

    jupiter.shape("images/Jupiter.gif")
    saturno.shape("images/Saturno.gif")
    urano.shape("images/Urano.gif")
    netuno.shape("images/Netuno.gif")


    jupiter.setpos(-150, 150)
    saturno.setpos(150, 150)
    urano.setpos(-150, -150)
    netuno.setpos(150, -150)
	
    screen.listen()
        
    time.sleep(10)
    
    
    turtle.bye()
    turtle.TurtleScreen._RUNNING = True


def mostraVenus():

    screen = tela()
    
    sol = turtle.Turtle()
    venus = turtle.Turtle()

    astros = [sol, venus]
    for astro in astros:
        astro.penup()

    screen.addshape("images/Sol.gif")
    screen.addshape("images/Venus.gif")
    
    sol.shape("images/Sol.gif")
    venus.shape("images/Venus.gif")

    sol.setpos(0, 0)
    dt = 0
    amp = 85
	
    for i in range (500):
        x = amp*cos(dt)
        y = amp*sin(dt)
		
        venus.setpos( amp*cos(dt+2), amp*sin(dt+2))

        dt += 0.025
        screen.listen()

    turtle.bye()
    turtle.TurtleScreen._RUNNING = True

def mensagem():
    print("BEM VINDO AO JOGO ASTRONOMIA & CIA!")
    print("Jogo desenvolvido por Henrique Grigolli e Salomon Asher")
	
def acertos(pontos):

    if(pontos == 300):
        print("Parabéns! Você acertou todas as perguntas!")
    elif(pontos == 200):
        print("Bom! Você acertou duas perguntas de três.")
    elif(pontos == 100):
        print("Razoavel. Você acertou uma perguntas de três.")
    else:
        print("Que pena! Você não acertou nenhuma pergunta :( ")
	
    print("Pontos: ", pontos)
	
def verificacao(pergunta):
    item = [1,2,3]
    print(pergunta)
    n = int(input())
    while(n not in item):
        print(pergunta)
        n = int(input())
    return n

def escolheDificuldade():
    pergunta = "Dificuldades:\n1 - Facil\n2 - Medio\n3 - Dificil\nEscolha a dificuldade: "
    n = verificacao(pergunta)
    return n

def espacos():
    for i in range(10):
        print("\n")

def dificuldadeFacil():
    pontos = 0
    print("A Lua é o satélite natural da Terra e sua gravidade influencia nas marés dos oceanos.")
    print("Ela também teve influência para a criação dos calendários, já que cada fase sua leva em torno de 7 dias")
    print("Veja a seguinte simulação e responda a primeira pergunta:")
    input("Pressione Enter para continuar...")
    mostrarLua()
    print("O ciclo de fase da Lua leva em média, quanto tempo?")
    p1 = verificacao("1 - 28 dias\n2 - 34 dias\n3 - 17 dias")
    if(p1 == 1):
        print("Isso mesmo! Os meses foram criados baseados nas fases da Lua: Crescente, Minguante, Nova e Cheia")
        pontos += 100
    else:
        print("Putss! Está errado. Os meses foram criados baseados nas fases da Lua: Crescente, Minguante, Nova e Cheia, possuindo assim uma média de 28 dias")

    print("Pontos: ", pontos)
    espacos()
    
    print("Você já ouviu falar no sistema solar? Se não, saiba que existem 8 planetas no nosso Sistema Solar.")
    print("São eles: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno.")
    print("Até 2006, Plutão foi considero o nono planeta do Sistema Solar. Hoje ele é considerado um planeta-anão")
    input("\nPressione Enter para continuar...\n")
    sistemaSolar()

    print("Agora que você observou os astros do nosso Sistema Solar, saberia dizer qual deles é uma estrela?")
    p2 = verificacao("1 - Terra\n2 - Sol\n3 - Júpiter")
    if(p2 == 2):
        pontos += 100
        print("Isso mesmo! O Sol é a estrela que esquenta nosso planeta!")
    else:
        print("Putss! Está errado. O Sol é uma estrela e é ele que esquenta nosso planeta.")
        
    print("Pontos: ", pontos)
    espacos()

    print("Você sabia que até o século XVI d.C. as pessoas acreditavam que a Terra era o centro do Sistema Solar?")
    print("Foi Nicolau Copérnico que mudou este conceito e desenvolveu a teoria Heliocêntrica.")

    input("\nPressione Enter para continuar...\n")
    sistemaSolarHeliocentrico()

    print("Com base no movimento que você acabou de ver, responda:")
    print("Qual é o planeta mais afastado do Sistema Solar?")

    p3 = verificacao("1 - Plutão\n2 - Urano\n3 - Netuno")


    if(p3 == 1):
        print("Errou! O Plutão deixou de ser um planeta em 2006. Hoje ele é um planeta-anão")
    elif(p3 == 3):
        pontos += 100
        print("Isso mesmo! Netuno está a 4.5 bilhões de km do Sol!")
        print("Para se ter uma ideia, a Terra está a aproximadamente 150 milhões de km do Sol")
    else:
        print("Errou! Netuno está a 4.5 bilhões de km do Sol!U Urano está a 2.8 bilhões de km do Sol")


    acertos(pontos)
    
def dificuldadeMedia():
    pontos = 0
	
    print("Cada planeta possui sua atmosfera e elas são muito diferentes de um planeta para outro.")
    print("A temperatura média do planeta Terra é de 14°C")
    print("Você saberia dizer qual o planeta mais quente do Sistema Solar? ")
    p1 = verificacao("1 - Vênus\n2 - Mercúrio\n3 - Júpiter")
	
    if(p1 == 1):
        pontos += 100
        print("Isso mesmo! O planeta mais quente é Vênus, o segundo mais próximo do Sol. A razão é que Vênus possui uma atmosfera muito densa, que retém o calor e faz com que a temperatura média no planeta seja aproximadamende 450°C.")
    else:
        print("Putss! Está errado. O planeta mais quente é Vênus, o segundo mais próximo do Sol. A razão é que Vênus possui uma atmosfera muito densa, que retém o calor e faz com que a temperatura média no planeta seja aproximadamende 450°C.")
	
    input("\nPressione Enter para continuar...\n")
    mostraVenus()
	
    espacos()
	
    print("Os planetas são classificados em dois tipos: Planetas Telúricos e Planetas Gasosos.")
    print("Você saberia dizer quais sãos os planetas gasosos do Sistema Solar?")
    p2 = verificacao("1 - Júpiter, Saturno, Urano, Netuno\n2 - Júpiter, Saturno, Netuno, Vênus\n3 - Mercúrio, Vênus, Júpiter, Saturno")
	
    if(p2 == 1):
        pontos += 100
        print("Isso mesmo! Muito bem!")
    else:
        print("Errou!! Os planetas gasosos são: Júpiter, Saturno, Urano e Netuno")
		
    input("\nPressione Enter para continuar...\n")
    mostraGasosos()
	
    espacos()
	
    print("Observe a animação a seguir:")
    input("\nPressione Enter para continuar...\n")
	
    movimentoTerra()
	
    print("Baseado no movimento da Terra que você observou, responda:")
    print("Qual o nome do movimento feito pela Terra?")
            
    p3 = verificacao("1 - Rotaçãoão\n2 - Precessão\n3 - Translação")

    if(p3 == 3):
        pontos += 100
        print("Isso mesmo! Muito bem!")
    else:
        print("Errou!!")
		
    print("A rotação é o movimento que a Terra realiza em torno de seu próprio eixo, é como se ela estivesse “rodando” em volta de si mesma.")
    print("A translação é o movimento que a Terra realiza em torno do Sol, sendo que ela demora 365 dias, 4 horas e alguns minutos para completá-lo.")
	
    acertos(pontos)
	
def dificuldadeDificil():
	pontos = 0
	
	print("Na Antiguidade, o eclipse era visto como um sinal do fim do mundo.\nHoje sabemos que trata de um fenômeno natural.")
	print("O eclipse nada mais é que um fenômeno em que um astro deixa de ser visto parcial ou totalmente devido a presença de outro astro.")
	print("Esse fenômeno é comumente conhecido aqui na Terra por ocorrer entra o Sol e a Lua.")
	print("Quando a luz do astro que estamos observando é interrompida, dizemos que ocorreu um eclipse deste astro.")
	print("Veja a figura a seguir:")
	input("\nPressione Enter para continuar...\n")

	eclipseSolar()
	print("Qual foi o eclipse observado?")
	p1 = verificacao("1 - Eclipse Solar\n2 - Eclipse Lunar\n3 - Eclipse Terrestre")
    
	if(p1 == 1):
	    pontos += 100
	    print("Isso mesmo! Muito bem!")
	else:
	    print("Errou!!")
		
	print("Nesse caso, o astro que estamos observado é o Sol e a Lua tampou a luz dele.")
	
	espacos()
	
	print("Veja a figura a seguir:")
	input("\nPressione Enter para continuar...\n")
	eclipseLunar()
	print("Qual foi o eclipse observado?")
	p2 = verificacao("1 - Eclipse Solar\n2 - Eclipse Lunar\n3 - Eclipse Terrestre")
    
	if(p2 == 2):
	    pontos += 100
	    print("Isso mesmo! Muito bem!")
	else:
	    print("Errou!!")
		
	print("Nesse caso, o astro que estamos observado é a Lua e a Terra tampou a luz dela.")
	
	espacos()
	
	print("As fases da Lua são: Nova, Crescente, Cheia, Minguante")
	print("As fases depende da posição da Lua e, devido a isto, a forma como o Sol ilumina ela.")
	print("Veja a figura a seguir:")
	input("\nPressione Enter para continuar...\n")
	luaCrescente()
	print("Em que fase estava a Lua?")
            
	p3 = verificacao("1 - Cheia\n2 - Crescente\n3 - Minguante")
    
	if(p3 == 2):
	    pontos += 100
	    print("Isso mesmo! Muito bem!")
	else:
	    print("Errou!!")
		
	print("A Lua está em fase Crescente, pois, a luz do Sol está atingindo a Lua parcialmente e, a próxima fase é a Cheia, quando a luz atingia a Lua em toda sua face. ")
	
	acertos(pontos)
	
	
def main():
    mensagem()
    dificuldade = escolheDificuldade()
    
    if(dificuldade == 1):
        dificuldadeFacil()
    elif(dificuldade == 2):
        dificuldadeMedia()
    else:
        dificuldadeDificil()

    print("Obrigado por jogar o nosso jogo!")
    
main()
