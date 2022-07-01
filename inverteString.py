'''Aqui desenvolvo o algoritmo da questão 5, 
   programa que inverta os caracteres de um string.'''

string = str(input('Insira caracteres do tipo string: '))
stringInvertida = []
tam = len(string)

if tam == 1: #Caso haja apenas uma string
    print('Você digitou apenas espaço ou uma unica string:',string)

else:
    while tam > 0:
        stringInvertida += string[tam-1] #Invertendo apartir da ultima string
        tam -= 1 # decrementando a posição

    print("A string invertida é: ", *stringInvertida, sep ='') 
