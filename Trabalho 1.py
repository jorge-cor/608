#
# Nome: Jorge Correia
# Data: 04/11/25
# Turma: GRSCPL092025
# Trabalho 1 - Revisões 1
#

#------------------1----------------------------
print("ola mundo")

#------------------2-----------------------------

numero = int(input("digite um numero inteiro"))
print("\n O número informado foi:", numero)

#--------------------3----------------------------

num1 = int(input("digite o 1º numero inteiro"))
num2 = int(input("digite o 2º numero inteiro"))
print(f"\nA soma de {num1} e {num2} é {num1+num2}")

#---------------------4----------------------------------
soma = 0
for i in range(4):
    nota = int(input(f"digite a {i+1} notas bimestrais:"))
    soma = soma + nota
media = soma/4
print(f"\na media das 4 notas bimestrais e {media}  ")

#----------------------5-------------------------------------

metros = float(input("Digite o valor em metros: "))

centimetros = metros * 100
print(f"\n{metros} metros equivalem a {centimetros} centímetros.")

#---------------------------6---------------------------------------

raio = float(input("Digite o valor do raio do círculo: "))

area = 3.1459 * (raio ** 2)
print(f"\nUm círculo com raio {raio} tem uma área de {area}.")


#------------------------------7------------------------------------

lado = float(input("Digite o valor do lado do quadrado: "))
area = lado ** 2
dobro_da_area = area * 2
print(f"\nA área do quadrado com lado {lado} é {area}.")
print(f"O dobro desta área é: {dobro_da_area}.")

#-------------------------------8-------------------------------------

valor_hora = float(input("Quanto ganha por hora? (ex: 5.50): "))
horas_trabalho = float(input("Quantas horas trabalhou este mês? (ex: 167): "))

salario = valor_hora * horas_trabalho

print("\n--- O seu salário deste mês ---")
print(f"Valor por hora: {valor_hora:.2f} €")
print(f"Horas trabalhadas: {horas_trabalho} horas")
print(f"Salário total: {salario:.2f} €")

#-------------------------------9-------------------------------------------------

print(" -- conversor de graus Fahrenheit para graus Celsius -- ")
fahr = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = 5 * ((fahr - 32) / 9)
print(f"\n{fahr}°F equivalem a {celsius}°C.")

#-------------------------------10-----------------------------------------------------

print(" -- conversor de graus Celsius para graus Fahrenheit -- ")
celsiu = float(input("Digite a temperatura em graus Celsius : "))
fahren = (celsiu * 1.8) + 32
print(f"\n{celsiu}°C equivalem a {fahren}°F.")

#------------------------------11--------------------------------------------------------

nume1 = int(input("Digite o 1º número INTEIRO: "))
nume2 = int(input("Digite o 2º número INTEIRO: "))

nume3 = float(input("Digite o 3º número REAL (ex: 4.5): "))

calc_a = (2 * nume1) * (nume2/ 2)
print(f"11.1) O produto do dobro de {nume1} com metade de {nume2} é: {calc_a}")

calc_b = (3 * nume1) + nume3
print(f"11.2) A soma do triplo de {nume1} com {nume3} é: {calc_b}")

calc_c = nume3 ** 3
print(f"11.3) O número {nume3} elevado ao cubo é: {calc_c}")

#-----------------------------12-----------------------------------------------------------

print("-- Calculadora de Peso Ideal com a formula ((72.7 * altura) - 58) --")
altura = float(input("Digite a sua altura em metros: "))
peso = (72.7 * altura) - 58
print(f"\nPara uma altura de {altura} M, o peso ideal estimado é {peso:.3f}kg.")

#----------------------------13-----------------------------------------------------------------

print("-- Calculadora de Peso Ideal por generos --")
a_altura = float(input("Digite a sua altura em metros: "))

genero = input("Qual o seu género? (Digite H , homem ou M ou mulher): ").upper()
if genero == 'H' or genero == 'HOMEM':
    peso_i = (72.7 * a_altura) - 58
    print(f"\nPara um HOMEM com {a_altura} M, o peso ideal estimado é {peso_i:.3f}kg.")
elif genero == 'M' or genero == 'MULHER':
    peso_i = (62.1 * a_altura) - 44.7
    print(f"\nPara uma MULHER com {a_altura} M, o peso ideal estimado é {peso_i:.3f}kg.")
else:
    print(f"\nErro: Género inválido. Respondeu '{genero}', mas era esperado 'H', 'M', 'MULHER' ou 'HOMEM'.\n.")

#--------------------------------14-------------------------------------------------------------------------------

print("--- Controle de Rendimento Diário: Pesca ---")

peso = float(input("Digite o peso de peixes pescado (em Kg): "))
LIMITE = 50
MULTA = 4.00
if peso > LIMITE:
    excesso = peso - LIMITE
    multa = excesso * MULTA
    print("Atenção: O limite foi excedido.")
else:
    excesso = 0
    multa = 0
    print("Situação regular: Dentro do limite permitido.")
print("\n--- Relatório Final ---")
print(f"Peso total pescado: {peso} Kg")
print(f"Excesso de peso:   {excesso} Kg")
print(f"Valor da Multa:  € {multa}")

