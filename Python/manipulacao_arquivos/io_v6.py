#!/usr/local/bin/python3

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)
            #modificada a saida da função print para imprimir dentro de um arquivo .txt
  

if arquivo.closed:
    print('Arquivo já foi fechado!')


if saida.closed:
    print('Arquivo de saida já foi fechado!')