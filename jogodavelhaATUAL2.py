linhaUM =   [1,2,3]
linhaDOIS = [4,5,6]
linhaTRES = [7,8,9]
resp = "S"
jogo = [linhaUM,linhaDOIS,linhaTRES]
posicao = 0
jogada = 0

#Funções para verificar vencedor
def ganhou1():
    vencedor = ''
    if (linhaUM[0]== "X") and (linhaUM[1]== "X") and (linhaUM[2]== "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'
    if (linhaDOIS[0] == "X") and (linhaDOIS[1]== "X") and (linhaDOIS[2] == "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'
    if (linhaTRES[0] == "X") and (linhaTRES[1] == "X") and(linhaTRES[2] == "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'
    if (linhaUM[0] == "X") and (linhaDOIS[0] == "X") and(linhaTRES[0] == "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'
    if (linhaUM[1] == "X") and (linhaDOIS[1] == "X") and(linhaTRES[1] == "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'
    if (linhaUM[2] == "X") and (linhaDOIS[2] == "X") and(linhaTRES[2] == "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'
    if (linhaUM[0] == "X") and (linhaDOIS[1] == "X") and (linhaTRES[2] == "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'
    if (linhaUM[2] == "X") and (linhaDOIS[1] == "X") and (linhaTRES[0] == "X"):
        print ("JOGADOR 1 GANHOU!!!")
        vencedor = 'X'    
    return vencedor

def ganhou2():
    vencedor = ''
    if (linhaUM[0]== "O") and (linhaUM[1]== "O") and (linhaUM[2]== "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'
    if (linhaDOIS[0] == "O") and (linhaDOIS[1]== "O") and (linhaDOIS[2] == "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'
    if (linhaTRES[0] == "O") and (linhaTRES[1] == "O") and(linhaTRES[2] == "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'
    if (linhaUM[0] == "O") and (linhaDOIS[0] == "O") and(linhaTRES[0] == "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'
    if (linhaUM[1] == "O") and (linhaDOIS[1] == "O") and(linhaTRES[1] == "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'
    if (linhaUM[2] == "O") and (linhaDOIS[2] == "O") and(linhaTRES[2] == "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'
    if (linhaUM[0] == "O") and (linhaDOIS[1] == "O") and (linhaTRES[2] == "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'
    if (linhaUM[2] == "O") and (linhaDOIS[1] == "O") and (linhaTRES[0] == "O"):
        print ("JOGADOR 2 GANHOU!!!")
        vencedor = 'O'    
        
    return vencedor
        
#Print da matriz
print (linhaUM)
print (linhaDOIS)
print (linhaTRES)
print (jogo)

            #Ínicio programa principal#
  
while True:   
    for x in range(1,9):

        
######## Lógica para primeiro jogador: ########     
        print ("Jogador 1")
        posicao = int(input("Digite a posição que deseja jogar ou 0 para encerrar: "))

    #Lógica para verificar dados invalidos
        if (posicao>=10):
            print("Posição invalida")
            break
        elif (posicao==0):
            print ("Programa encerrado")
            break
        
    #Define as posições: 
        if (posicao==1):
            linhaUM[0]= "X"
        elif (posicao==2):
            linhaUM[1]= "X"
        elif (posicao==3):
            linhaUM[2]= "X"
        elif (posicao==4):
            linhaDOIS[0] = "X"
        elif (posicao==5):
            linhaDOIS[1]= "X"
        elif (posicao==6):
            linhaDOIS[2] = "X"
        elif (posicao==7):
            linhaTRES[0] = "X"
        elif (posicao==8):
            linhaTRES[1] = "X"
        elif (posicao==9):
            linhaTRES[2] = "X"
        jogada = jogada+1

    #Print após jogada do primeiro jogador:     
        print (linhaUM)
        print (linhaDOIS)
        print (linhaTRES)
        print ("Jogada: ", jogada)

        vencedor = ganhou1()
        # If para limitar ao maximo de 9 rodadas
        if (jogada == 9) and (vencedor == ''):
            print("/nVELHA!")
            break
        if (jogada == 9) or (vencedor != ''):
            break
        
    
######## Lógica para segundo jogador: ########         
        print ("Jogador 2")
        posicao = int(input("Digite a posição que deseja jogar ou 0 para encerrar: "))

        #Lógica para verificar dados invalidos
        if (posicao>=10):
            print("Posição ivalida")
            break
        elif (posicao==0):
            print ("Programa encerrado")
            break
        

    #Define as posições:
        if (posicao==1):
            linhaUM[0]= "O"
        elif (posicao==2):
            linhaUM[1]= "O"
        elif (posicao==3):
            linhaUM[2]= "O"
        elif (posicao==4):
            linhaDOIS[0] = "O"
        elif (posicao==5):
            linhaDOIS[1]= "O"
        elif (posicao==6):
            linhaDOIS[2] = "O"
        elif (posicao==7):
            linhaTRES[0] = "O"
        elif (posicao==8):
            linhaTRES[1] = "O"
        elif (posicao==9):
            linhaTRES[2] = "O"
        jogada = jogada+1
        
        ganhou2()
    #If para limitar ao maximo de 9 rodadas 
        if (jogada == 10):
            break
        
    #Print após jogada do segundo jogador: 
        print (linhaUM)
        print (linhaDOIS)
        print (linhaTRES)
        print ("Jogada: ", jogada)
 
   #Lógica para o While True funcionar
    resp = input ("Deseja continuar? [S] [N]")
    if (resp=='n') or (resp=='N'):
        print ("Jogo encerrado!")
        break


    
