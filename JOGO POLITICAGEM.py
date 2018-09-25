
##JOGO POLITICAGEM
##
##
##GRUPO: Henrique Nóbrega Grigolli     - 41621661
##       Salomon Asher Motoryn         - 41825128
##       Larissa Teixeira dos Santos   - 31802486
##




### IMPORTS ###

from tkinter import *
from math import *
from random import *

### FIM DOS IMPORTS ###

root = Tk()
root.title("Jogo Politicagem")

### INICIALIZAR VARIAVEIS ###

nome = None
cidade = None
sexo = None
votos = None
partEsc = None
resposta = None
popularidade = None
ehCandidato = None
ehProcurado = None
bordao = None
respJulg = None

#############################


### FUNÇÕES ###
def create_manual():
    window = Toplevel(root)
    msg = Message(window, text="""Manual do candidato:\n
Neste jogo você deve tomar decisões para subir de cargo na carreira política.\n
No começo você cria seu personagem com nome, sexo e cidade inicial.\n
Irão surgir decisões e baseadas nelas serão atribuídas seus votos ( pontos ).\n
Ganha o jogo assim que conseguir chegar a presidência.\n""").pack()


def comecar(frame):
    frame.tkraise()

def endgame(frame):
    root.destroy()

  
    #### FRAME PARTIDO
def prox_frame_part(frame):
    global cidade
    global nome
    global sexo
    global votos

    


    lbl_part = Label(frame, text=("Olá " + nome.get()))      
    lbl_part.pack()

    votos.set(70)
    
    aleat = random()
    if(aleat <= 0.2):
        Label(frame, text="O Prefeito da sua cidade é filiado ao PSDB e ele não gostou de você").pack()
        
    elif(aleat <= 0.4):
       Label(frame, text="O Prefeito da sua cidade é filiado ao PSDB e ele foi com a sua cara mas ainda desconfia de você.").pack()
        
    else:
        Label(frame, text="O Prefeito da sua cidade é filiado ao PSDB e ele gostou de você e quer que você se junte a campanha dele.").pack()

    Label(frame, text="Qual partido você gostaria de se filiar?")

    Radiobutton(frame, text="Partido dos Trabalhadores - PT", padx=20, variable=partEsc, value="PT").pack()
    Radiobutton(frame, text="Partido Verde - PV", padx=20, variable=partEsc, value="PV").pack()
    Radiobutton(frame, text="Partido da Social Democracia Brasileira - PSDB", padx=20, variable=partEsc, value="PSDB").pack()
    Button(frame, text="Avançar", command=lambda:prox_frame_veread1(veread1)).pack()
    ######
    frame.tkraise()


def prox_frame_veread1(frame):

    global partEsc


    
    Label(frame, text=("Você se filiou ao " + partEsc.get())).pack()
    Label(frame, text=("Sua primeira missão agora é ganhar votos e se tornar vereador da cidade: " + cidade.get())).pack()
    Label(frame, text=("""Você foi convidado a participar do jantar de seu partido. Isso pode te ajudar a ter apoio dos líderes do seu partido porém os outros candidatos
                         podem fazer com que você receba menos votos futuramente.\nVocê gostaria de ir ao jantar?""")).pack()
    Radiobutton(frame, text="SIM", padx=20, indicatoron=0, variable=resposta, value=1, command=lambda:prox_frame_veread2(veread2)).pack()
    Radiobutton(frame, text="NÃO", padx=20, indicatoron=0, variable=resposta, value=0, command=lambda:prox_frame_veread2(veread2)).pack()
    frame.tkraise()


def prox_frame_veread2(frame):
    
    global resposta
    global ehCandidato
    global ehProcurado
    global popularidade
    global respJulg

    
    if(resposta.get() == 1):
        aleat = random()
        if(aleat <= 0.7):
            Label(frame, text=("""Você fez uma boa apresentação e os lideres gostaram de você.\nVocê se tornou um candidato a vereador pelo """ + partEsc.get())).pack()
            popularidade.set(1)
            ehCandidato.set(1)
            votos.set(votos.get() + 10) 
        else:
            Label(frame, text="Você gerou brigas e confusões. Está mais difícil para se tornar um candidato.").pack()
            popularidade.set(-1)
            ehProcurado.set(3)
            ehCandidato.set(0)
            votos.set(votos.get() - 10)
    else:
        Label(frame, text="Você não foi ao jantar e não recebeu apoio. Porém você foi a quermesse da cidade e ganhou apoio popular.").pack()
        popularidade.set(10)
        votos.set(votos.get() + 10)

    if(ehCandidato.get() == 0 and ehProcurado.get() == 0):
        Label(frame, text="Alguns membros do " + partEsc.get() + " também estavam na quermesse viram sua atitude e após conversas em seu partido você se tornou um cadidato a vereador").pack()
        ehCandidato.set(1)
    elif(ehCandidato.get() == 0):
        Label(frame, text="Você se desculpa pela confusão e convence os membros de seu partido a te colocarem como candidato a vereador").pack()
        ehCandidato.set(1)
    else:
        pass

    Label(frame, text="Agora, você precisa criar sua campanha. Digite uma frase ou um bordão que você gostaria de usar: ").pack()
    en_bord = Entry(frame, textvariable=bordao)
    en_bord.pack()
    
    Button(frame, text="Avançar", command=lambda:prox_frame_res(resultado1)).pack()
    frame.tkraise()

def prox_frame_res(frame):
    
    global bordao

    Label(frame, text="Muito bem! Ano de eleição é corrido e você se esforçou em sua camapanha, agora veremos o seu resultado: ").pack()

    if( len(bordao.get()) <= 20 ):
        votos.set(votos.get() + 5)
    elif(len(bordao.get()) <= 30): 
        votos.set(votos.get() + 10)
    else:
        votos.set(votos.get() + 15)

    if(votos.get() <= 65):
        Label(frame, text="Seu histórico de confusão e uma  camapanha fraca gerou poucos votos e você não conseguiu se eleger.").pack()
        Label(frame, text="Fim de Jogo").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    else:
        Label(frame, text="Parabénss!!! Você foi eleito vereador!!! Com %d votos!!" % (votos.get()*100) ).pack()
        Button(frame, text="Avançar", command=lambda:frame_fun_vereador(funVereador)).pack()
    
    frame.tkraise()

### FRAME VEREADOR ###

def frame_fun_vereador(frame):

    global r1
    global r2
    bordao.set("")
    
    Label(frame, text="Como vereador você deve escolher alguns de seus deveres: ").pack()
    
    r1 = Radiobutton(frame, text="Apresentar propostas de emenda à Lei do Municipio", indicatoron=0, variable=resposta, value=1, command=lambda:ativ_veread(frame))
    r1.pack()
    r2 = Radiobutton(frame, text="Julgar as contas do Prefeito", indicatoron=0, variable=resposta, value=0, command=lambda:ativ_veread(frame))
    r2.pack()
    frame.tkraise()

def ativ_veread(frame):
    global r3
    global r4
    
    r1.config(state = DISABLED)
    r2.config(state = DISABLED)
    
    if(resposta.get() == 1):
        aleat = random()
        if(aleat <= 0.5):
            Label(frame, text = "Você sugeriu propostas que não foram bem aceitas.").pack()
            votos.set(votos.get() - 10)
        else:
            Label(frame, text = "Suas propostas fizeram muito sucesso!").pack()
            votos.set(votos.get() + 10)
            
        Button(frame, text="Avançar", command=lambda:elei_dep(deputado)).pack()

    else:
        Label(frame, text="Você julgou as contas do Prefeito e descobriu que ele está fazendo um caixa 2 particular.\nO que você faz?").pack() 
        r3 = Radiobutton(frame, text="Não fala nada e conversa com o prefeito para participar do esquema.", indicatoron = 0, variable=respJulg, value = 1, command=lambda:julgamento(frame))
        r3.pack()
        r4 = Radiobutton(frame, text="Denuncia o Prefeito porque isso mais tarde pode afetar em sua carreia política.", indicatoron = 0 ,variable=respJulg, value = 0, command=lambda:julgamento(frame))
        r4.pack()
        
    frame.tkraise()
        
def julgamento(frame):
    r3.config(state = DISABLED)
    r4.config(state = DISABLED)
    
    if(respJulg.get() == 1):
        Label(frame, text="O Prefeito te colocou no esquema dele, sua verba para a campanha está garantida").pack()
        ehProcurado.set( ehProcurado.get() + 1 )

    else:
        Label(frame, text="A Polícia Federal fez a busca na conta do Prefeito e ele foi preso. Você é visto como justo pelo povo brasileiro e os partidos estão de olho em você").pack()
        votos.set(votos.get() + 20)
        popularidade.set( popularidade.get() + 10 )

    Button(frame, text="Avançar", command=lambda:elei_dep(deputado)).pack()

    frame.tkraise()

##### FRAME DEPUTADO ####
def elei_dep(frame):
    global r5
    global r6
    
    Label(frame, text="""Já se passou mais de um ano da última eleição e você conseguiu executar algumas propostas prometidas na campanha.\n
        O %s sugere que você se candidate a Deputado Federal. Você aceita?""" % (partEsc.get()) ).pack()
    r5 = Radiobutton(frame, text="SIM", padx=20, indicatoron=0, variable=resposta, value=1, command=lambda:acc_dep(frame))
    r5.pack()
    r6 = Radiobutton(frame, text="NÃO", padx=20, indicatoron=0, variable=resposta, value=0, command=lambda:rej_dep(frame))
    r6.pack()
    
    frame.tkraise()

def acc_dep(frame):
    r5.config(state = DISABLED)
    r6.config(state = DISABLED)
    
    Label(frame, text="Você é candidato a deputado federal pelo seu estado e está liderando as pesquisas.\nMas uma boa propaganda na TV pode fazer toda a diferença.\nEscreva o texto da sua propaganda política.").pack()
    Entry(frame, textvariable=bordao).pack()
    Button(frame, text="Avançar", command=lambda:res_dep(resulDeputado)).pack()
    frame.tkraise()


def rej_dep(frame):
     
    if(ehProcurado.get() > 0):
        Label(frame, text="Você não teve escolha e foi chantageado por algo que você fez em seu passado.\nAgora você é candidato a Deputado Federal").pack()
        Button(frame, text="Avançar", command=lambda:res_dep(resulDeputado)).pack()
    else:
        Label(frame, text="Você gosta da vida boa e quer o melhor para a sua cidade. Prefere se manter como vereador e não se juntar a sujeira política").pack()
        Label(frame, text="Você chegou ao cargo de Vereador. Fim de Jogo").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
        
    frame.tkraise()

def res_dep(frame):

    if( len(bordao.get()) <= 20 ):
        votos.set(votos.get() - 5)
    elif(len(bordao.get()) <= 30): 
        votos.set(votos.get() + 5)
    else:
        votos.set(votos.get() + 10)

    if(votos.get() <= 65):
        Label(frame, text="Você precisa se esforçar mais para ganhar as eleições").pack()
        Label(frame, text="Fim de Jogo").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    else:
        Label(frame, text="Parabénss!!! Você foi eleito Deputado Federal!!! Com %d votos!!" % (votos.get()*100) ).pack()
        Button(frame, text="Avançar", command=lambda:frame_dep_fed(funDepFed)).pack()    

    frame.tkraise()

def frame_dep_fed(frame):
    global r7
    global r8
    
    Label(frame, text="3 anos já se passaram e acessores de uma empreitera te ofereceram 20 milhões de dólares para dar concessão a uma obra de trem conectando várias cidades.\nVocê, sabendo que se for pego, pega anos prisão, está na dúvida se aceita a proposta eles estão lhe pressionando cada vez mais.\nSe aceitar, além de se tornar um milionário, isso lhe daria enormes chances de ser o principal candidato ao governo do seu estado.\nCaso não aceite, não corre risco de prisão porém, sua carreira política pode acabar já nas próximas eleições.").pack()
    r7 = Radiobutton(frame, text="Aceito a proposta", padx=20, indicatoron=0, variable=resposta, value=1, command=lambda:acc_dep1(frame))
    r7.pack()
    r8 = Radiobutton(frame, text="Não aceito a proposta", padx=20, indicatoron=0, variable=resposta, value=0, command=lambda:rej_dep1(frame))
    r8.pack()
    frame.tkraise()

def acc_dep1(frame):
    r7.config(state = DISABLED)
    r8.config(state = DISABLED)
    ehProcurado.set(ehProcurado.get() + 2)
    Label(frame, text="Você se tornou um milionário e comprou enormes mansões, apartamentos no exterior e vários carros importados.\nPor isso, a polícia começou a desconfiar um pouco de você, mas eles não tem provas, então você continua ostentando sem se preocupar.\nAlém disso, as eleições para governador se aproximam e a vitória está praticamente garantida.").pack()
    votos.set(votos.get() + 5)
    Button(frame, text="Avançar", command=lambda:elei_sen(eleiSen)).pack()
    frame.tkraise()

def rej_dep1(frame):
    r7.config(state = DISABLED)
    r8.config(state = DISABLED)
    
    if(popularidade.get() >= 10):
        Label(frame, text="Você não aceitou o dinheiro, mas isso causou intrigas com a máfica do seu partido e eles estão tentando te tirar das as próximas eleições.\nPorém, como você é popular você ainda continua no jogo político").pack()
        votos.set(votos.get() + 10)
        Button(frame, text="Avançar", command=lambda:elei_sen(eleiSen)).pack()
    else:
        Label(frame, text="Sua popularidade não foi suficiente para o seu partido querer te manter nele.\nVocê chegou ao cargo de Deputado Federal").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()

    frame.tkraise()
    
##### FRAME SENADOR #####
def elei_sen(frame):

    global r9
    global r10
    
    if(popularidade.get() >= 10):
        Label(frame, text="Surge a oportunidade de ser candidato a Senador pelo %s.\nVocê está tendo um bom mandato e é popular.\nSão boas as chances de se tornar Senador." % (partEsc.get())).pack()
        Label(frame, text="Você aceita a ser candidato a Senador?").pack()
    elif(ehProcurado.get() > 2):
        Label(frame, text="Apesar de não ser tão popular, o %s quer que você se candidate a Senador devido a suas influências políticas.").pack()
        Label(frame, text="Você aceita a ser candidato a Senador?").pack()
    else:
        Label(frame, text="Você não é popular e nem influente. Ainda assim há a oportunidade de se candidatar a Senador.").pack()
        Label(frame, text="Você aceita a ser candidato a Senador?").pack()

    r9 = Radiobutton(frame, text="Quero me candidatar", padx=20, indicatoron=0, variable=resposta, value=1, command=lambda:acc_sen(frame))
    r9.pack()
    r10 = Radiobutton(frame, text="Não quero me candidatar", padx=20, indicatoron=0, variable=resposta, value=0, command=lambda:rej_sen(frame))
    r10.pack()
    frame.tkraise()

def acc_sen(frame): 
    r9.config(state = DISABLED)
    r10.config(state = DISABLED)
    
    if(popularidade.get() >= 10):
        Label(frame, text="O povo clama pela sua candidatura!").pack()
    else:
        Label(frame, text="O %s está confiante e todos acreditam no seu potencial" % (partEsc.get()) ).pack()

    Button(frame, text="Avançar", command=lambda:resul_sen(resulSen)).pack()
    frame.tkraise()

def rej_sen(frame):
    r9.config(state = DISABLED)
    r10.config(state = DISABLED)
    Label(frame, text="O Senado não é para você. A sua preferência é permanecer como Deputado Federal e quem sabe aumentar sua influencia futuramente.").pack()
    Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    frame.tkraise()

def resul_sen(frame):

    if(votos.get() >= 110):
        Label(frame, text="Parabénss!!! Você foi eleito Senador!!! Com %d votos!!" % (votos.get()*100) ).pack()
        Button(frame, text="Avançar", command=lambda:fun_sen(funSen)).pack()
    elif(popularidade >= 10):
        Label(frame, text="Mesmo sendo popular você não conseguiu a quantidade de votos suficiente.").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    elif(ehProcurado > 2):
        Label(frame, text="Mesmo sendo influente você não conseguiu a quantidade de votos suficiente.").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    else:
        Label(frame, text="Você não conseguiu se eleger. Faltou carisma e influência").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()

    frame.tkraise()

def fun_sen(frame):

    global r11
    global r12
    
    Label(frame, text="Surgiu um novo esquema que você pode entrar.\nDessa vez, o diretor da Caixa Econômica Federal lhe ofereceu mais de 150 milhões de dólares para você convencer o presidente do Tribunal Superior Eleitoral para burlar as próximas eleições presidenciais e dar a vitória a alguém do seu partido.\nCaso você aceite a proposta, pode ser o seu nome o do próximo presidente do Brasil. Porém, se alguém abrir a boca, sua vida já era.").pack()

    r11 = Radiobutton(frame, text="Aceito a proposta", padx=20, indicatoron=0, variable=resposta, value=1, command=lambda:acc_sen1(frame))
    r11.pack()
    r12 = Radiobutton(frame, text="Não aceito a proposta", padx=20, indicatoron=0, variable=resposta, value=0, command=lambda:rej_sen1(frame))
    r12.pack()

    frame.tkraise()

def acc_sen1(frame):
    r11.config(state = DISABLED)
    r12.config(state = DISABLED)   
    ehProcurado.set(ehProcurado.get() + 2)

    if(ehProcurado.get() >= 4):
        Label(frame, text="NÃO ABUSE DA SORTE! VOCÊ FOI PRESO!").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    else:
        Label(frame, text="Você tentou a sorte conseguiu entrar no esquema. Está fácil para se tornar o novo Presidente do Brasil").pack()
        votos.set(votos.get() + 10)
        Button(frame, text="Avançar", command=lambda:elei_pres(funSen)).pack()

def rej_sen1(frame):
    
    bordao.set("")
    
    r11.config(state = DISABLED)
    r12.config(state = DISABLED)

    if(popularidade.get() >= 10):
        Label(frame, text="Você foi justo. O seu partido está querendo te por para fora mas a pressão popular que5r te manter no poder").pack()
        votos.set(votos.get() + 15)
        Button(frame, text="Avançar", command=lambda:elei_pres(funSen)).pack()
    elif(ehProcurado.get() < 2):
        Label(frame, text="Você foi justo. Porém, isso não foi bom pra você. As próximas eleições estão chegando e nenhum partido quer você para nada.").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack() 
    else:
        Label(frame, text="Você foi justo. Porém, isso não foi bom pra você. As próximas eleições estão chegando e nenhum partido nem o povo te quer.").pack()
        Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()

def elei_pres(frame):
    Label(frame, text="ATENÇÃO ATENÇÃO - ELEIÇÕES PRESIDENCIAIS CHEGANDO!!!").pack()
    Label(frame, text="Neste ponto automaticamente você é candidato a Presidência pelo %s . " % (partEsc.get())  ).pack()
    Label(frame, text="Você deve se esforçar bastante agora em sua campanha para conseguir a maior quantidade de votos. Escreva sua campanha: ").pack()
    Entry(frame, textvariable=bordao).pack()
    Button(frame, text="Resultado das eleições Presidenciais", command=lambda:res_pres(resPres)).pack()

def res_pres(frame):
    if(len(bordao.get()) <= 40):
        votos.set(votos.get() - 10)
        popularidade.set(popularidade.get() - 5)
    elif( len(bordao.get()) <= 50):
        votos.set(votos.get() + 5)
    else:
        votos.set(votos.get() + 10)
        popularidade.set(popularidade.get() + 5)

    if(votos.get() >= 150 and popularidade.get() >= 15):
         Label(frame, text="PARABÉNS!!! VOCÊ FOI ELEITO PRESIDENTE!!!!")
         Label(frame, text="Você obteve: %d" % (votos.get()*100) )
         Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    elif(votos.get() >= 150):
         Label(frame, text="QUASEEE!! Você não foi eleito Presidente por muito pouco. O povo não te considerou popular.")
         Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
    else:
         Label(frame, text="Você não foi eleito Presidente. Faltaram votos e popularidade")
         Button(frame, text="FIM", fg="red", command=lambda:endgame(menu)).pack()
         
    
    
    



## INICIA OS FRAMES ##
menu = Frame(root)
start = Frame(root)
manual = Frame(root)
sair = Frame(root)

partido = Frame(root)

veread1 = Frame(root)
veread2 = Frame(root)
resultado1 = Frame(root)
funVereador = Frame(root)

deputado = Frame(root)
resulDeputado = Frame(root)
funDepFed = Frame(root)

eleiSen = Frame(root)
resulSen = Frame(root)
funSen = Frame(root)

eleiPres = Frame(root)
resPres = Frame(root)

#### STARTA O MENU ####
comecar(menu)

##### PREPARA OS FRAMES ####
frames = [ menu, start, manual, sair, partido, veread1, veread2, resultado1, funVereador, deputado, resulDeputado, funDepFed, eleiSen, funSen, resulSen, eleiPres, resPres ]
for frame in frames:
    frame.grid(row=0, column=0, sticky='news')

##### MENU #####
Label(menu, text="Jogo Politicagem").pack()
Label(menu, text="Grupo:\nHenrique Nóbrega Grigolli - 41621661\nSalomon Asher Motoryn - 41825128\nLarissa Teixeira dos Santos - 31802486\n").pack()
Button(menu, text="Iniciar", command=lambda:comecar(start)).pack()
Button(menu, text="Manual", command=create_manual).pack()
Button(menu, text="Sair", fg="red", command=lambda:endgame(menu)).pack()



### SETA OS TIPOS DAS VARIAVEIS
nome = StringVar()
cidade = StringVar()
sexo = StringVar()
votos = IntVar()
partEsc = StringVar()
resposta = BooleanVar()
respJulg = BooleanVar()
ehCandidato = BooleanVar()
popularidade = IntVar()
ehProcurado = IntVar()
bordao = StringVar()

### FRAME START ######
Label(start, text="Qual seu nome?").grid(row=0)

nome_ent = Entry(start, textvariable=nome)
nome_ent.focus_set()
nome_ent.grid(row=0,column=1)

Label(start, text="Escolha seu sexo: ").grid(row=1)
Radiobutton(start, text="Feminino", padx=20,variable=sexo,value="Feminino").grid(row = 2, sticky='w')
Radiobutton(start, text="Masculino", padx=20,variable=sexo,value="Masculino").grid(row = 3, sticky='w')
Label(start, text="Escolha sua cidade: ").grid(row=4)

cidades = ["São Paulo", "Rio de Janeiro", "Fortaleza", "Porto Alegre", "Brasilia", "Manaus", "Tangamandápio"]
for c in cidades:
    Radiobutton(start, text=c, padx=20, variable=cidade, value=c).grid(sticky='w')

   
Button(start, text="Avançar", command=lambda:prox_frame_part(partido)).grid(sticky='e')

###### MANTEM O LOOP DO JOGO #######
root.mainloop()
