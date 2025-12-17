"""
metodo  -> função dentro de uma classe
"""

class Contacto:
    def __init__(self, nome:str, email:str, telefone:str):
        print("objeto inicializado")
        self.nome = nome
        print (f"criar uma instancia do contacto com nome:{nome}")
        self.email = email
        print (f"criar uma instancia do contacto com email:{email}")
        self.telefone = telefone