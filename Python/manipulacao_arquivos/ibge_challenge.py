import csv

with open('desafio-ibge.csv', 'r' , encoding='ISO-8859-1') as entrada:
  for enderecos in csv.reader(entrada):
    print('{8} : {3}'.format(*enderecos))

#Ler o arquivo de exemplo, converter para o devido encoding e mostrar a nona e quarta coluna 