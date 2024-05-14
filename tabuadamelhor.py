num = int(input("DIGITE UM NUMERO PARA VER SUA TABUADA: "))
print ( f' a tabuada do {num} é: ')
for i in range (1,11):
    resultado = num  * i
    print (f'{num} * {i} = {resultado} ')
    