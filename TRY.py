"""

lista = [1,2,3,4,5]

try:
    print(lista[0])
    print(lista[1])
    print(lista[10])
except IndexError:
    print("IndexError")
print("o codigo vai terminar")



try:
    num_in ="10"
    print(int(num_in))

except ValueError: # corre quando há erros
    print("Oops!Soneting went wrong.")

else: # corre quando não há erros
    print("A conversao correu bem")

finally: # corre sempre
    print("o programa vai terminar")


while True:
    try:
        num=int(input("insira um numero: "))

    except ValueError as msg: # corre quando há erros
        print("O Valor não e numérico.", end=" ")
    else:
        print(num)

def input_int():
    while True:
        try:
            num=int(input("insira um numero: "))
        except ValueError as msg:
            print(msg_erro, end=" ")
        else:
            return

"""
def safe_input(
    _type: type,
    prompt:str,
    msg_erro:str="",
    new_line:bool=True):
    if not isinstance(_type, type):
        raise TypeError(f"O parâmetro '_type' deve ser um tipo (ex: int, float,str). Recebeu: {type(_type).__name__}")
    if not isinstance(prompt, str):
        raise TypeError(f"O parâmetro 'prompt' deve ser uma string. Recebeu: {type(prompt).__name__}")
    if not isinstance(msg_erro, str):
        raise TypeError(f"O parâmetro 'msg_erro' deve ser uma string. Recebeu: {type(msg_erro).__name__}")
    if not isinstance(new_line, bool):
        raise TypeError(f"O parâmetro 'new_line' deve ser um booleano. Recebeu: {type(new_line).__name__}")
    while True:
        try:
            num=_type(input(f"insira um {prompt} "))
        except ValueError:
            print(msg_erro, end="\n" if new_line else "")
        else:
            return num