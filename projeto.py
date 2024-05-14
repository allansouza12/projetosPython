import random
valoraleatorio = random.randint(1,10)
acertou = False
while acertou == False:
 chute= int(input( "digite um numero de 1 a 10 "))
 if chute > valoraleatorio :
    print( 'vc chutou alto')
 elif chute < valoraleatorio:
    print( 'vc chutou baixo')
 elif chute == valoraleatorio:
    acertou = True 
    print ("voce acertou")
        # errei indentaçao aqui, a condiçao while precisa ficar indentada
        #de forma correta, entao aqui se nao acertar o numero, o looping while
        # continuara com as condiçoes ate acertou for verdadeiro
        