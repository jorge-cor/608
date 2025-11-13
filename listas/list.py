lis =[
'Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo',
    'Filipa', 'Gonçalo', 'Helena', 'Inês', 'Jorge',
    'Luís', 'Marta', 'Nuno', 'Olívia', 'Pedro',
    'Rita', 'Sérgio', 'Teresa', 'Vasco', 'Xavier',
    'Alice', 'Bernardo', 'Cátia', 'Duarte', 'Eva',
    'Fernando', 'Gabriela', 'Hugo', 'Isabel', 'José',
    'Lara', 'Miguel', 'Natália', 'Óscar', 'Patrícia',
    'Ricardo', 'Sara', 'Tomás', 'Vítor', 'Alexandra',
    'Bárbara', 'Cristiano', 'Diana', 'Fábio', 'Guilherme',
    'Joana', 'Leonardo', 'Manuela', 'Nicole', 'Paulo'
]

print(lis)

nova_lis = [(elm, idx) for idx,elm in enumerate(lis) if elm.endswith('a')]
print(nova_lis)

nomes2 = [
    'Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo',
    'Filipa', 'Gonçalo', 'Helena', 'Inês', 'Jorge',
    'Luís', 'Marta', 'Nuno', 'Olívia', 'Pedro',
    'Rita', 'Sérgio', 'Teresa', 'Vasco', 'Xavier',
    'Alice', 'Bernardo', 'Cátia', 'Duarte', 'Eva',
    'Fernando', 'Gabriela', 'Hugo', 'Isabel', 'José',
    'Lara', 'Miguel', 'Natália', 'Óscar', 'Patrícia',
    'Ricardo', 'Sara', 'Tomás', 'Vítor', 'Alexandra',
    'Bárbara', 'Cristiano', 'Diana', 'Fábio', 'Guilherme',
    'Joana', 'Leonardo', 'Manuela', 'Nicole', 'Paulo'
]
# 1
tamanhos = [len(nome) for nome in nomes2]

print(tamanhos)
# 2
tamanhos2 = [len(nome) for nome in nomes2 if nome.startswith('A')]

print(tamanhos2)
# 3
par = [nome for nome in nomes2 if len(nome) %2 == 0 ]

print(par)
# 4
resultado = [(nome[::-1], len(nome), idx) for idx, nome in enumerate(nomes2) if len(nome) % 2 != 0 ]

print(resultado)