print("Insira a taxa do exame para 10 pacientes:")

valores = []
for _ in range(10):
    valores.append(float(input()))

n = len(valores)

soma = sum(valores)
am = soma / n

soma_inversos = sum(1 / x for x in valores)
hm = n / soma_inversos

produto = 1
for x in valores:
    produto *= x
gm = produto ** (1 / n)

erro_harmonica = (hm - am) / am
erro_geometrica = (gm - am) / am
erro_medio = (erro_harmonica + erro_geometrica) / 2
erro_medio_pct = erro_medio * 100

print(f"Média aritmética: {am:.2f}")
print(f"Média harmônica: {hm:.2f}")
print(f"Média geométrica: {gm:.2f}")
print(f"Erro médio: {erro_medio_pct:.2f}%")