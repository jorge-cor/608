#
# Nome: Jorge Correia
# Data: 13/11/25
# Turma: GRSCPL092025
# Trabalho 2 - Revisões
#

"""
#Ex1

print ("------O Maior-------------------")
num1 = int(input("digite o 1º numero inteiro"))
num2 = int(input("digite o 2º numero inteiro"))
if num1 > num2:
    print (f"o numero {num1} e maior que o numero {num2} ")
elif num1 < num2:
    print(f"o numero {num1} e menor que o numero {num2} ")
else:
    print(f"ambos os valor com o numero {num1} sao iguais")

#Ex2

print ("------Positivo ou Negativo------------")
valor = int(input("digite um numero inteiro"))
if valor > 0:
    print (f"o numero {valor} e positivo ")
elif valor < 0 :
    print(f"o numero {num1} e negativo ")
else:
    print(f" -_- ZERO -_- ")

#Ex3

print ("--------Verificação de sexo------------")
sexo = input("digite \"F\" ou \"M\". F para Feminino, M para Masculino ").upper()
if sexo == "F":
    print ("a pessoa e de genero Feminino ")
elif sexo == "M" :
    print("a pessoa e de genero Masculino  ")
else:
    print("Sexo Inválido")


#Ex4

print("--------vogal ou consoante------------")

letra = input("digite uma letra").lower()
if letra in 'aeiou':
    print(f"A letra {letra} é uma Vogal.")
else:
    print(f"A letra {letra} é uma Consoante.")



#Ex5

print("--------nota Aluno------------")

nota1 = float(input("Introduza a primeira nota: "))
nota2 = float(input("Introduza a segunda nota: "))

media = (nota1 + nota2) / 2
print(f" a media do aluno {media} ")

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


#Ex6

print ("------O Maior-------------------")
nume1 = int(input("digite o 1º numero inteiro"))
nume2 = int(input("digite o 2º numero inteiro"))
nume3 = int(input("digite o 3º numero inteiro"))

if nume1 > nume2 and nume1 > nume3 :
    print (f"o numero {nume1} e maior que o numero {nume2} e {nume3}  ")
elif nume2 > nume1 and nume2 > nume3 :
    print(f"o numero {nume2} e maior que o numero {nume1} e {nume3}  ")
else:
    if nume1 == nume2 or nume1 == nume3 or nume2 == nume3:
        if nume1 == nume2:
            print(f"o 1º numero eigual a o 2º numero {nume2} ")
        elif nume1 == nume3:
            print(f"o 1º numero eigual a o 3º numero {nume3} ")
        elif nume2 == nume3:
            print(f"o 2º numero eigual a o 3º numero {nume3} ")
        else:
            print(f"o numero {nume3} e maior que o numero {nume1} e {nume2}")

# Ex7

print ("------O Maior e Menor-----------------")
nume1 = int(input("digite o 1º numero inteiro"))
nume2 = int(input("digite o 2º numero inteiro"))
nume3 = int(input("digite o 3º numero inteiro"))

if nume1 > nume2 and nume1 > nume3 :
    if nume3 > nume2:
        print (f"o numero {nume1} e maior e o  {nume2} e o menor ")
    else:
        print(f"o numero {nume1} e maior e o  {nume3} e o menor ")
elif nume2 > nume1 and nume2 > nume3 :
    if nume1 > nume3:
        print (f"o numero {nume2} e maior e o  {nume3} e o menor ")
    else:
        print(f"o numero {nume2} e maior e o  {nume1} e o menor ")
else:
    if nume1 == nume2 or nume1 == nume3 or nume2 == nume3:
        if nume1 == nume2:
            if nume2 > nume3:
                print(f"o numero {nume2} e maior e o  {nume3} e o menor ")
            elif nume2 < nume3:
                print(f"o numero {nume3} e maior e o  {nume2} e o menor ")
            else:
                print(f"os numeros sao iguais ao numero {nume2} ")
        elif nume1 == nume3:
            if nume2 > nume3:
                print(f"o numero {nume2} e maior e o  {nume3} e o menor ")
            elif nume2 < nume3:
                print(f"o numero {nume3} e maior e o  {nume2} e o menor ")
            else:
                print(f"os numeros sao iguais ao numero {nume3} ")
        elif nume2 == nume3:
            if nume1 > nume3:
                print(f"o numero {nume1} e maior e o  {nume3} e o menor ")
            elif nume1 < nume3:
                print(f"o numero {nume3} e maior e o  {nume1} e o menor ")
            else:
                print(f"os numeros sao iguais ao numero {nume3} ")
    else:
        if nume1 > nume2:
            print(f"o numero {nume3} e maior e o  {nume2} e o menor ")
        else:
            print(f"o numero {nume3} e maior e o  {nume1} e o menor ")


# Ex8

print ("------O Preço mais barato-----------------")
nume1 = int(input("digite o 1º Preço inteiro:\n"))
nume2 = int(input("digite o 2º Preço inteiro:\n"))
nume3 = int(input("digite o 3º Preço inteiro:\n"))
if nume1 > nume2 and nume1 > nume3:
    if nume3 > nume2:
        print(f"o Preço menor e o  {nume2} € ")
    else:
        print(f"o Preço menor e o  {nume3} €")
elif nume2 > nume1 and nume2 > nume3:
    if nume1 > nume3:
        print(f"o Preço menor e o  {nume3} € ")
    else:
        print(f"o Preço menor e o  {nume1} € ")
else:
    if nume1 == nume2 or nume1 == nume3 or nume2 == nume3:
        if nume1 == nume2:
            if nume2 > nume3:
                print(f"o Preço menor e o  {nume3} € ")
            elif nume2 < nume3:
                print(f"o Preço menor e o  {nume2} € ")
            else:
                print(f"Os valores dos produtos sao iguais em valor a {nume2} € ")
        elif nume1 == nume3:
            if nume2 > nume3:
                print(f"o Preço menor e o {nume3} € ")
            elif nume2 < nume3:
                print(f"o Preço menor e o {nume2} € ")
            else:
                print(f"Os valores dos produtos sao iguais em valor a {nume3} € ")
        elif nume2 == nume3:
            if nume1 > nume3:
                print(f"o Preço menor e o {nume3} €")
            elif nume1 < nume3:
                print(f"o Preço menor e o {nume1} €")
            else:
                print(f"Os valores dos produtos sao iguais em valor a {nume3} € ")
    else:
        if nume1 > nume2:
            print(f"o Preço menor e o {nume2} € ")
        else:
            print(f"o Preço menor e o {nume1} € ")



# Ex9

print("------numeros em ordem decrescente-----------------")
nume1 = int(input("digite o 1º numero inteiro:\n"))
nume2 = int(input("digite o 2º numero inteiro:\n"))
nume3 = int(input("digite o 3º numero inteiro:\n"))
if nume1 > nume2:
    if nume1 > nume3:
        if nume2 > nume3:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume1}\n {nume2}\n {nume3}\n fim")
        elif nume2 == nume3:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume1}\n {nume2}\n fim")
        else:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume1}\n {nume3}\n {nume2}\n fim")
    else:
        if nume1 == nume3:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume1}\n {nume2}\n fim")
        else:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume3}\n {nume1}\n {nume2}\n fim")
elif nume2 > nume1:
    if nume2 > nume3:
        if nume1 > nume3:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume2}\n {nume1}\n {nume3}\n fim")
        elif nume1 == nume3:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume2}\n {nume1}\n fim")
        else:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume2}\n {nume3}\n {nume1}\n fim")
    else:
        if nume1 == nume3:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume2}\n {nume1}\n fim")
        else:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume3}\n {nume2}\n {nume1}\n fim")
else:
    if nume3 > nume2:
        if nume1 > nume2:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume3}\n {nume1}\n {nume2}\n fim")
        elif nume1 == nume2:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume3}\n {nume1}\n fim")
        else:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume3}\n {nume2}\n {nume1}\n fim")
    else:
        if nume1 == nume2:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume3}\n {nume1}\n fim")
        else:
            print(f"O ordenando os numeros em ordem decrescente:\n {nume2}\n {nume3}\n {nume1}\n fim")


# Ex 10

print("-----------------------turno quue você estuda---------------------------")

turno=input("em que turno voce estuda colocando M-matutino ou V-Vespertino ou N- Noturno ").upper()
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")


# EX 11

print("-----------------------A nota de 0 a 10---------------------------")
nota = int(input("digite sua nota entre 0 a 10:\n "))

while nota < 0 or nota > 10:
    nota = input("valor invalido coloque um valor entre 0 a 10\n")
else:
    print("Obrigado ate breve")


# EX 12

print("-----------------------Login---------------------------")

while True:
    user = input("introduza o utilizador:\n")
    password = input("introduza o password:\n")
    if user != password :
        print("bem vindo !!!")
        break
    else:
        print(f"-"*20, "login incorreto","-"*20)
        print("volte a tentar")



# EX 13

idade = -1
salario = -1
sexo = "A"
civil = "A"
con=0
while con < 4 :
    nome = input("informe o nome do usuario:\n")
    con = len(nome)
while idade < 0 or idade > 150 :
    idade = int(input("informe o idade do usuario:\n"))
while salario < 0 :
    salario = float(input("informe o salario do usuario:\n"))
while sexo != "F" and sexo != "M" and sexo != "FEMENINO" and sexo != "MASCULINO" :
    sexo = input("informe o sexo do usuario(Ex f ou m):\n").upper()
while civil != "S" and civil != "C" and civil != "V" and civil != "D" and civil != "SOLTEIRO" and civil != "CASADO" and civil != "VIUVO" and civil != "DIVORCIADA" and civil != "SOLTEIRA" and civil != "CASADA" and civil != "VIUVA" and civil != "DIVORCIADA" :
    civil = input("informe o estado civil do usuario(Ex 's', 'c', 'v', 'd'):\n").upper()
if sexo == "F" :
    sexo = "Femenino"
elif sexo == "M" :
    sexo = "Masculino"
if civil == "S" :
    civil = "Solteiro"
elif civil == "C" :
    civil = "Casado"
elif civil == "V" :
    civil = "Viuvo"
elif civil == "D" :
    civil = "Divorciado"
print(f"*"*20,"resumo","*"*20)
print(f"\nNome: {nome};\nIdade: {idade} anos;\nSalário: {salario} €;\nSexo: {sexo};\nEstado Civil: {civil};\n")

# EX 14

populacao_a = 80000
taxa_a = 0.03
populacao_b = 200000
taxa_b = 0.015
anos = 0
print(f"Ano 0 -> População A: {populacao_a} | População B: {populacao_b}")
print("-" * 60)
while populacao_a < populacao_b:
    anos += 1
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b + (populacao_b * taxa_b)
print(f"\n Resultado alcançado em {anos} anos.")
print("-" * 60)
print(f"População final do país A: {populacao_a:.0f} habitantes")
print(f"População final do país B: {populacao_b:.0f} habitantes")
print("-" * 60)


# EX 15

populacao_1 = int(input("introduza a quantidade da população do pais A :\n"))
taxa_1 = float(input("introduza a taxa de crichimento do pais A :\n"))
populacao_2 = int(input("introduza a quantidade da população do pais B :\n"))
taxa_2 = float(input("introduza a taxa de crichimento do pais B :\n"))
anos = 0
print(f"Ano 0 -> População A: {populacao_1} | População B: {populacao_2}")
print("-" * 60)
if populacao_1 < populacao_2:
    populacao_a = populacao_1
    populacao_b = populacao_2
    paisa="país A"
    paisb="país B"
    taxa_a = taxa_1/100
    taxa_b = taxa_2/100
elif populacao_1 > populacao_2:
    populacao_a = populacao_2
    populacao_b = populacao_1
    paisa="país B"
    paisb="país A"
    taxa_a = taxa_2/100
    taxa_b = taxa_1/100
else:
    print(f"População igual em ambos os paises de {populacao_1}")
    populacao_a = populacao_1
    populacao_b = populacao_2
while populacao_a < populacao_b:
    if taxa_a < taxa_b:
        print("o crechimento")
    anos += 1
    populacao_a = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b + (populacao_b * taxa_b)
print(f"\n Resultado alcançado em {anos} anos.")
print("-" * 60)
print(f"População final do {paisa}: {populacao_a:.0f} habitantes")
print(f"População final do {paisb}: {populacao_b:.0f} habitantes")
print("-" * 60)


# EX 16
# EX 16.1
anum=0

while anum < 20:
    anum = anum + 1
    print(anum)

# EX 16.2
anum=0

while anum < 20:
    anum = anum + 1
    print(anum,end=" ")

# EX 17
pnum=0
maximo=0

while pnum < 5:
    pnum = pnum + 1
    numero=int(input(f"Introduza o {pnum}º numero"))
    if numero > maximo:
        maximo = numero
print(f"O numero maior e {maximo}")

"""
# EX 18

pnum=0
soma=0
media=0
while pnum < 5:
    pnum = pnum + 1
    numero=int(input(f"Introduza o {pnum}º numero"))
    soma=soma + numero
    media = soma/pnum
print(f"A soma e {soma} e a media e {media}")