numero = int(input("Digite um número: "))

if numero <= 0:
    print("O número deve ser maior que 0.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"Resultado do fatorial: {fatorial}")