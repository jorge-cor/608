from listas import utils
from TRY import safe_input

utils.f1()
utils.f2()
utils.f3()

#safe_input(prompt, msg_erro="o valor introduzido não e numerico.")

num = safe_input("batata", "Numero: ")

num = safe_input(int, "Numero: ", "Não e um numero inteiro")
print(num)

num = safe_input(str, "String: " "Não e um String")
print(num)

num=safe_input(float, "float: ", "Não e um float")
print(num)