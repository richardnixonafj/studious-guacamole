#!/usr/local/bin/python3

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
#O uso do with trata diretamente o fechamento do arquivo, dispensando o finally

if arquivo.closed:
    print('Arquivo já foi fechado!')
