'''Aqui desenvolvo o algoritmo da questão 2, sequência de Fibonacci.'''

num = int(input('Digite um número para a sequência de Fibonacci: '))
v = [0,1]
anterior = v[0]
proxima = v[1]
soma = 1
tam = len(v)
i = 1
while num >= i: #Enquanto o número for maior ou igual que o 'i' continua calculando      
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
    v.append(proxima)
    i += 1     

if num in v: # Verificando se o número está na sequência
    print('O número {} pertence a sequência'.format(num))
else:
    print('O número {} não pertence a sequência'.format(num))
