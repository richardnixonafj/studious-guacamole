#!/usr/local/bin/python3
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
        #strip primeiro remove os espaços em branco e split fatia a string.
finally:
    print('finally')
    arquivo.close()
# mesmo que o o programa encontre um erro na execução ele vai executar: arquivo.close()
if arquivo.closed:
    print('Arquivo já foi fechado!')
