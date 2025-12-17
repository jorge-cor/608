#Crie uma aplicação que permite salvar e ler o perfil de um utilizador com pelo menos 5 campos
#deve ser possível ler e salvar múltiplos utilizadores no mesmo ficheiro

"""
SEPA = ","
def adicionar_utilizador():
    print("\n--- Novo Utilizador ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")
    cidade = input("Cidade: ")
    Turma = input("Turma: ")
    perfil = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "cidade": cidade,
        "turma": Turma
    }
    dados = (f"{perfil['nome']}, {perfil['idade']}, {perfil['email']}, {perfil['cidade']}, {perfil['turma']}\n")
    with open("utilizadores.bin", 'a', ) as file:
        file.write(dados)
        print("utilizador guardado com sucesso")

def listar_utilizadores():
    contador = 1
    print("\n--- Lista de Utilizadores ---")
    with open("utilizadores.bin", 'r', ) as file:
        for line in file:
            dado = line.strip().split(SEPA)
            if len(dado) >= 5:
                dados_lido = {
                    "nome": dado[0],
                    "idade": dado[1],
                    "email": dado[2],
                    "cidade": dado[3],
                    "turma": dado[4]
                }
                print(f"\nUtilizador #{contador}")
                print(f"Nome: {dados_lido['nome']}")
                print(f"Idade: {dados_lido['idade']}")
                print(f"Email: {dados_lido['email']}")
                print(f"Cidade: {dados_lido['cidade']}")
                print(f"Turma: {dados_lido['turma']}")

                print("-" * 20)
                contador += 1
    input("Prima ENTER para voltar ao menu...")


def menu():
    while True:
        print("\n=== GESTÃO DE PERFIS ===")
        print("1. Adicionar Utilizador")
        print("2. Ler Ficheiro")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            adicionar_utilizador()
        elif opcao == '2':
            listar_utilizadores()
        elif opcao == '3':
            print("A sair...")
            break
        else:
            print("Opção inválida.")

menu()
"""
import pickle
import json

user ={
    "nome": "nome2",
    "idade": 27,
    "email": "nome2@mail.com",
}
"""
with open("user.txt", 'ab') as file:
    pickle.dump(user, file)

with open("user.txt", 'rb') as files:
    while True:
        try:
            dados = pickle.load(files)
            print(dados)
        except EOFError:
            break"""

json_data = json.dumps(user)
print(json_data)
