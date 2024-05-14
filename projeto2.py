velocidade= int(input('qual foi a velocidade que passou? '))
max= 80
if velocidade <= max:
        print('nao houve multa')
elif velocidade== max +10:
    print(' houve multa leve')
elif velocidade >= max +11 and velocidade <= 100:
    print ('houve multa media')
else:
    print ('houve multa grave')
    
 