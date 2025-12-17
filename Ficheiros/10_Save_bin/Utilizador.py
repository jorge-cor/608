

SEPA = "|"
def adicionar_utilizador():
    print("\n--- Novo Utilizador ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")
    cidade = input("Cidade: ")
    Turma = input("Turma: ")
    dados = f"{nome}{SEPA}{idade}{SEPA}{email}{SEPA}{cidade}{SEPA}{Turma}\n"
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
                print(f"\nUtilizador #{contador}")
                print(f"Nome: {dado[0]}")
                print(f"Idade: {dado[1]}")
                print(f"Email: {dado[2]}")
                print(f"Cidade: {dado[3]}")
                print(f"Profissão: {dado[4]}")
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