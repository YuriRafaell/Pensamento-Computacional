numero_pessoas = int(input("Qual o número de pessoas?\n"))

print("Informe as idades:")
soma_idades = 0

for _ in range(numero_pessoas):
    idade = int(input())
    soma_idades += idade

if numero_pessoas > 0:
    media = soma_idades // numero_pessoas
    print(f"A média de idade das pessoas é {media} anos")
else:
    print("Nenhuma pessoa informada para o cálculo.")