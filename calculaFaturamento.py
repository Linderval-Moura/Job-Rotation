'''Aqui desenvolvo o algoritmo da questão 3, 
   faturamento diário de uma distribuidora.'''
import json

array = []
valores = []
fatSuperiorMedia = []
#Passando diretorio do arquivo e armazenando conteúdo no array
with open('C:/Users/linde/Desktop/Job Rotation/dados.json') as f:
    array=json.load(f)

for e in array: #Percorrendo array
    tam = len(array)
    if e['valor'] > 0: #ignorando dias sem faturamento
        menorValor = e['valor']
        maiorValor = e['valor']

        valores.append(e['valor'])
        media = sum(valores)/len(valores)

        for p in valores: #Percorrendo valores de faturamento
            if p < menorValor: #Obtendo menor valor
                menorValor = p
            elif p > maiorValor: #Obtendo maior valor
                maiorValor = p
    
        if e['valor'] > media:
            fatSuperiorMedia.append(e)

print('Menor valor de faturamento:', menorValor)
print('Maior valor de faturamento:', maiorValor)
print('Número de dias com faturamento superior à média mensal:', len(fatSuperiorMedia))
print('\nDados extras abaixo.')
print('Média mensal: {:.4f}'.format(media))
print('Dias com faturamento superior à média mensal:\n', fatSuperiorMedia)
