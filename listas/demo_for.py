# crie um for que moster todos os valores de 0 a 10
"""
for i in range(11):
    print(i)




range (n) -> mostar todos os numeros inteiros de 0 a n -1
range (m,n) -> mostar todos os numeros inteiros de m a n -1
range (m,n,s) -> mostar todos os numeros inteiros de m a n -1 com step de s



while True:
    numero = int(input("Qual tabuada deseja calcular? Insira um número: "))
    if numero <= -1 :
        break
    print(f"\n--- A calcular a tabuada do {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
import os
"""
while True:
    print("""######### MENU #########
#opc1                 1#
#opc2                 2#
#opc3                 3#
#opc4                 4#
#opc5                 5#
########################""")
    num = input("selecione a opção pretentida : ")
    match num:
        case "1":
            print("\"opc1\"")
        case "2":
            print("\'opc2\'")
        case "3":
            print("opc3")
        case "4":
            print("a sair")
            break
        case _:
            print("caracter errado")
    input("digite enter pra continuar")
    os.system("cls")
"""
"""

condicao =True

#while condicao:
print("ola mundo")
print ( 2 << 10)

var_a:str = "nome"

print(var_a)
def soma(val1:int, val2:int) -> int:
    return val1 + val2

def subtracao(val1:int, val2:int) -> int:
    return val1 - val2

def soma2(val1:int = 0 , val2:int = 0 ) -> int:
    return val1 + val2
print(soma(2,3))
print(soma2())