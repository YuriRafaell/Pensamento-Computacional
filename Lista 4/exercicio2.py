
meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

numero = int(input("Digite um número entre 1 e 12: "))

if 1 <= numero <= 12:
    print("Mês correspondente:", meses[numero - 1])
else:
    print(f"Erro: não existe mês de número {numero}. Por favor, digite um número entre 1 e 12.")
