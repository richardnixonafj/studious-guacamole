#!/usr/local/bin/python3
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
    #strip primeiro remove os espaços em branco e split fatia a string.
arquivo.close()
