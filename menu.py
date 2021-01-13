import csv
from collections import namedtuple
from datetime import datetime
#def gettime():
    #print(dateTimeObj)
    # Access the member variables of datetime object to print date & time information
    #print(dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
    #print(dateTimeObj.hour, ':', dateTimeObj.minute)

def diasDaSemana():
    
    dateTimeObj = datetime.now()
    diaSemana = dateTimeObj.today().weekday()       # 0 segunda, 1 terca, 2 quarta, 3 quinta, 4 sexta, 5 sabado, 6 domingo
    hora = dateTimeObj.hour
    
    if (diaSemana >= 0 and diaSemana <=4):          # dia de semana
        if (hora >= 9 and hora < 20):
            menu_estacionar()
        else:
            print("Fora do Horario de estacionamento, pagamento apenas entre as 9h-20h")
    elif(diaSemana == 5):
        if( hora >= 9 or hora < 14):
            menu_estacionar()
        else:
            print("Fora do Horario de estacionamento, pagamento apenas entre as 9h-14h")
    else:
        print("Fora do Horario de estacionamento, domingos e feriados estacionamento gratuito")

    
def menu_principal():
    dateTimeObj = datetime.now()
    
    print("-------------------------------")
    print("-----      Bem Vindo      -----")
    print("----- Sistema Parquimetro -----")
    print("      Dia:",dateTimeObj.day,'/', dateTimeObj.month,'/', dateTimeObj.year)
    print("      Hora:",dateTimeObj.hour,'H' ,':', dateTimeObj.minute,"M")
    print("")
    print("1. Administrador")
    print("2. Cliente")
    print("3. Opções")
    print("0. Sair")
    print("")
    print("-------------------------------")
    print("")
    opcaoMP=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMP==1):
        menu_administrador()
        
    elif(opcaoMP==2):
        menu_cliente()
        
    elif(opcaoMP==3):
        menu_opcoes()
        
    elif(opcaoMP==0):
        exit
        


def menu_administrador():
    print("-----------------------------------")
    print("-----      Administrador      -----")
    print("")
    print("1. Ver Zonas")
    print("2. Ver Maquinas")
    print("3. Ver Historico")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("-----------------------------------")
    print("")
    opcaoMA=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMA==1):
        menu_zonas()
        
    elif(opcaoMA==2):
        menu_maquinas()#Possivelmente melhor em ficheiro
        
    elif(opcaoMA==3):
        #EXTRA
        menu_historicoADMIN()#Ficheiro e é extra para fazer
        
    elif(opcaoMA==4):
        menu_principal()
            
    elif(opcaoMA==0):
        exit

def menu_zonas():
    print("---------------------------")
    print("-----      Zonas      -----")
    print("")
    print("Zona 1: ")
    print("Zona 2: ")
    print("Zona 3: ")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("----------------------------")
    print("")
    opcaoMZ=int(input("Escolha a opção pretendida -> "))
        
    if(opcaoMZ==4):
        menu_administrador()
            
    elif(opcaoMZ==0):
        exit

def menu_maquinas():
    print("------------------------------")
    print("-----      Maquinas      -----")
    print("")
    print()#NOME DO FICHEIRO
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("------------------------------")
    print("")
    opcaoMM=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMM==4):
        menu_administrador()
            
    elif(opcaoMM==0):
        exit
    
def menu_historicoADMIN():
    print("-------------------------------")
    print("-----      Historico      -----")
    print("")
    print()#NOME DO FICHEIRO
    print("")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("--------------------------------")
    print("")
    opcaoMHA=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMHA==4):
        menu_administrador()
            
    elif(opcaoMHA==0):
        exit



def menu_cliente():
    print("-----------------------------")
    print("-----      Cliente      -----")
    print("")
    print("1. Estacionar")
    print("2. Ver Zonas")
    print("3. Ver Historico")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("------------------------------")
    print("")
    opcaoMC=int(input("Escolha a opção pretendida -> "))
    if(opcaoMC==1):
        diasDaSemana()
        
    elif(opcaoMC==2):
        menu_zonas()
        
    elif(opcaoMC==3):
        menu_historicoCLIENTE()#Ficheiro e é extra para fazer
        
    elif(opcaoMC==4):
        menu_principal()
        
    elif(opcaoMC==0):
        exit

def menu_estacionar():
    
    print("--------------------------------")
    print("-----      Estacionar      -----")
    print("")
    print("1. Zona 1")
    print("2. Zona 2")
    print("3. Zona 3")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("--------------------------------")
    print("")
    opcaoME=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoME==1):
        menu_zona1()
        
    elif(opcaoME==2):
        menu_zona2()
        
    elif(opcaoME==3):
        menu_zona3()
        
    elif(opcaoME==4):
        menu_cliente()
        
    elif(opcaoME==0):
        exit
    

def menu_zona1():
    preco = 1.15
    duracao=45
    
    print("----------------------------")
    print("-----      Zona 1      -----")
    print("")
    print("Preço (Para Duração Maxima): ",preco)
    print("Duração Maxima (Minutos): ",duracao)
    print("Lugares Disponiveis:")
    print("1. Estacionar")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("-----------------------------")
    print("")
    opcaoMZ1=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMZ1==1):
        menu_zona1_estacionar()
        
    elif(opcaoMZ1==4):
        menu_estacionar()
        
    elif(opcaoMZ1==0):
        exit


def menu_zona1_estacionar():

        resto=1.15
        duracao=1
        valorz1 = float(input("Insira a quantia desejada -> "))
        estacionamento= valorz1*duracao/resto
        if (valorz1 < 0):
            print("Introduza um valor positivo.")
        if (estacionamento < 0):
            print("Introduza uma quantia mais alta.")
        if (estacionamento > 0.45):
            print("Só pode estacionar por 45 minutos, introduza uma quantia mais baixa.")
        else:
            print("Pode estacionar por ", round(estacionamento,2),"minutos")
            menu_recibo()
        

def menu_zona2():
    preco = 1
    duracao=2
    print("----------------------------")
    print("-----      Zona 2      -----")
    print("")
    print("Preço: ",preco, "Duração Maxima (Horas): ",duracao)
    print("Lugares Disponiveis:")
    print("1. Estacionar")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("-----------------------------")
    print("")
    opcaoMZ2=int(input("Escolha a opção pretendida -> ")) 
    
    if(opcaoMZ2==1):
        menu_zona2_estacionar()
        
    elif(opcaoMZ2==4):
        menu_estacionar()
        
    elif(opcaoMZ2==0):
        exit  

def menu_zona2_estacionar():

        resto=1
        duracao=2
        valorz2 = float(input("Insira a quantia desejada -> "))
        estacionamento= valorz2*duracao/resto
        if (valorz2 < 0):
            print("Introduza um valor positivo.")
        if (estacionamento < 0):
            print("Introduza uma quantia mais alta.")
        if (estacionamento > 2):
            print("Só pode estacionar por 2 horas, introduza uma quantia mais baixa.")
        else:
            print("Pode estacionar por ", round(estacionamento,2),"horas")
            menu_recibo()
        

def menu_zona3():
    preco = 0.62
    print("----------------------------")
    print("-----      Zona 3      -----")
    print("")
    print("Preço: ",preco, "Sem Duração Maxima ")
    print("Lugares Disponiveis:")
    print("1. Estacionar")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("-----------------------------")
    print("")
    opcaoMZ3=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMZ3==1):
        menu_zona3_estacionar()
        
    elif(opcaoMZ3==4):
        menu_estacionar()
        
    elif(opcaoMZ3==0):
        exit 

def menu_zona3_estacionar():
        valorz3 = float(input("Insira a quantia desejada -> "))
        if (valorz3 < 0):
            print("Introduza um valor positivo.")
        print("Pode estacionar")
        menu_recibo()
        
def menu_recibo():
    print("----------------------------------------5----")
    print("----- Fim de Estacionamento Autorizado -----")
    print("----- Data -----")
    print("     ",dateTimeObj.day,'/', dateTimeObj.month,'/', dateTimeObj.year)
    print("----- Hora -----")
    print("    ",dateTimeObj.hour,'H' ,':', dateTimeObj.minute,"M")
    print("    ",valorz1,valorz2,valorz3)
    print("")

def menu_historicoCLIENTE():
    print("-------------------------------")
    print("-----      Historico      -----")
    print("")
    print()#NOME DO FICHEIRO
    print("")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("--------------------------------")
    print("")
    opcaoMHC=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMHC==4):
        menu_administrador()
            
    elif(opcaoMHC==0):
        exit
    
    
        
def menu_opcoes():
    print("----------------------------")
    print("-----      Opções      -----")
    print("")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("-----------------------------")
    print("")
    opcaoMO=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMO==1):
        print("")
        
    elif(opcaoMO==2):
        print("")
        
    elif(opcaoMO==3):
        print("")
        
    elif(opcaoMO==4):
        menu_principal()
        
    elif(opcaoMO==0):
        exit

   
menu_principal()