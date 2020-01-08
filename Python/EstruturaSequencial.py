# #01
# print("Ola Mundo!")

# #02
# num = input("Digite um número:")
# print(f"o numero digitado foi:{num}")

# #03
# n1 = int(input("Digite um primeiro número: "))
# n2 = int(input("Digite um segundo número: "))
# print(n1 + n2)

# #04
# msg = ("Digite a ")
# nota1 = int(input(msg + "primeira nota: "))
# nota2 = int(input(msg + "segunda nota: "))
# nota3 = int(input(msg + "terceira nota: "))
# nota4 = int(input(msg + "quarta nota: "))
# print(nota1 + nota2 + nota3 + nota4 /4)

# #05
# mt = int(input("Digite a quantidade em metros: "))
# print(f"É equivalente a: {mt * 100} Cm")

# #06
# raio = float(input("Entre com o valor do raio: "))
# circunferencia = 2 * 3.14 * raio
# area = 3.14 * (raio * raio)
# print("Área: {:.2f}, Raio: {:.2f}, Circunferencia: {:.2f}".format(area, raio, circunferencia))

# #07
# b = int(input("Digite o Valor da base: "))
# h = int(input("Digite o Valor da altura: "))

# if b != h :
#     print("O quadro deve ter a base = altura!")
# else :
#     print(f"Área do quadrado é:{b * h * 2}")

# #08
# salario = float(input("Quanto você ganha por hora ? "))
# horas = float(input("Quantas horas voce trabalha por mes ? "))
# print(f"Voce recebeu o equivalente a: {horas * salario}")

# #09
# f = float(input("Qual valor Farenheit? "))
# c = (f-32) / 1.8
# print(f"Convertido para Celsius é equivalente a: {c}")

# #10
# c = float(input("Qual valor Celsius? "))
# f = (c * 1.8) + 32
# print(f"Convertido para Farenheit é equivalente a: {f}")

# #11
# int_1 = int(input("Digite um valor inteio: "))
# int_2 = int(input("Digite outro valor INTEIRO: "))
# real_1 = float(input("digite um valor real! "))
# print((2 * int_1) + int_2 / 2)
# print((3 * int_1) + real_1)
# print(real_1 ** 3)

# #12
# altura = float(input("Entre com os valores de altura: "))
# peso = (72.7 * altura) - 58
# print(f"Seu peso ideal é:{peso} Kg")

#13
# h = float(input("Entre com os valores de altura: "))
# gender = (input("Digite: 'm' para masculino, ou 'f' para feminino : "))
# peso = 0
# if gender == 'm':
#     peso = ((72.7*h) - 58)
# else: peso = ((62.1*h) - 44.7)
# print("seu peso ideal é: {:.3}Kg".format(peso))

# #14
# pesopeixe = float(input("Quantos quilos de peixe você trouxe ?? "))
# limitepeso = 50
# excessopeso = 0
# multapeso = 0
# if pesopeixe > 50:
#     excessopeso = pesopeixe - limitepeso
#     multapeso = excessopeso * 4
# else:
#     print("Não terá multas!")
# print("O excesso de peso foi {:.2} kg e a multa foi de R$ {:.2}".format(excessopeso, multapeso))

# #15
# horastrabalhadas = float(input("Quantas horas voce trabalhou neste mes ?? "))
# valordahora = float(input("quanto voce ganha por hora ?? "))
# sbruto = horastrabalhadas * valordahora
# ir = sbruto * 0.11
# inss = sbruto * 0.08
# sindicato = sbruto * 0.05
# sliquido = sbruto - ir - inss - sindicato
# print(sbruto, ir, inss, sindicato, sliquido)

# #16
# m2 = float(input("qual o tamanho em m2 ?? "))
# litros = m2 / 3
# lata = 54
# custolata = 80
# qtlatas = litros / lata
# valor_final = qtlatas * custolata

# print(f"m2: {m2} e litros{litros} quantas latas: {qtlatas} e valor final {valor_final}")

#17
m2 = float(input("qual o tamanho em m2 ?? "))
litros = m2 / 6
lata = 54
custolata = 80
custo
qtlatas = litros / lata
valor_final = qtlatas * custolata

print(f"m2: {m2} e litros{litros} quantas latas: {qtlatas} e valor final {valor_final}")
