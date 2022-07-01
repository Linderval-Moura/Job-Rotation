'''Aqui desenvolvo o algoritmo da questão 4, faturamento
   mensal de cada Estado de uma distribuidora.'''

estados = {
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "Outros" : 19849.53
}

total = sum(estados.values())
for e,v in estados.items(): #Percorrendo chaves e valores de estados
    v = (v * 100) / total #Calcula percentual do valor 
    print('O percentual de {} é: {:.2f}%'.format(e,v)) #Imprime estado e percentual
