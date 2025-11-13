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
"""
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