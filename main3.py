"""
lista       - []
Variavel    - ()
set         - {}
dicionarios - { : }
"""


aluno = {
    "nome":"Ricardo",
    "Turma":"GRSC",
    "Ano Inscrcao":2025,
    "Aprovado" : False
}

print(aluno["nome"])
print(aluno["Turma"])
# print(aluno["Ano_Inscrcao"])  # se a key nao existir  da erro

print(aluno.get("Ano Inscrcao"))
aluno["Aprovado"] = True # alterar valor

print(aluno["Ano Inscrcao"])
print(aluno.get("Aprovado"))

# Adicionar valores

print(aluno)
aluno["nota"] = 15 # Add novo valor
print(aluno["nota"])

aluno.update({"nota":18}) #eita se existir, add se não existir
print(aluno)

aluno.popitem() # remove sempre o ultimo
print(aluno)

del aluno["Aprovado"]
print(aluno)


for elm in aluno: # igual a for elm in aluno.keys():
    print(elm)

for elm in aluno.values():
    print(elm)

for elm in aluno.items():
    print(elm)

for chave, valor in aluno.items():

    print(f"chave {chave}, valor {valor}")