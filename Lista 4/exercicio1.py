convidados = ["Daniel", "Aluizio", "Isabel", "Teles", "Eduardo"]

print("A lista contém os seguintes nomes:")
for nome in convidados:
    print(nome)

nome_verificar = input("\nQual nome você quer verificar? ")

if nome_verificar in convidados:
    print(f"O nome {nome_verificar} está na lista, acesso permitido!")
else:
    print(f"O nome {nome_verificar} não está na lista, acesso negado!")