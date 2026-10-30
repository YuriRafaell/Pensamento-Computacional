print("Informe os números (digite 0 para encerrar):")

maior_valor = None

while True:
    numero = int(input())
    
    if numero == 0:
        break
        
    if maior_valor is None or numero > maior_valor:
        maior_valor = numero

if maior_valor is not None:
    print(f"O maior valor é {maior_valor}.")
else:
    print("Nenhum valor foi informado.")