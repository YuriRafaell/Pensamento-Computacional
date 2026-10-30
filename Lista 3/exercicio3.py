cardapio = {
    100: 5.50,
    101: 15.00,
    103: 20.00,
    104: 18.00,
    105: 6.00
}

total = 0.0

while True:
    codigo = int(input("Digite o código do item: "))
    
    if codigo == -1:
        break
        
    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade: "))
        total += cardapio[codigo] * quantidade
    else:
        print("Item inválido. Tente novamente.")

total_formatado = f"{total:.2f}".replace('.', ',')

print(f"Total a pagar: R$ {total_formatado}")