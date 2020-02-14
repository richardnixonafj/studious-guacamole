#!/usr/local/bin/python3
arquivo = open('pessoas.csv')  #open buildin
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    #printa o resultado do *registro.split delimitado por ,
    print('Nome: {}, Idade: {}'.format(*registro.split(','))) 