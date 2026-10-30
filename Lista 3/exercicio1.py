altura_levi = float(input("Altura inicial de Levi:\n"))
taxa_levi = float(input("Taxa de crescimento de Levi:\n"))
altura_hiago = float(input("Altura inicial de Hiago:\n"))
taxa_hiago = float(input("Taxa de crescimento de Hiago:\n"))

if altura_hiago <= altura_levi:
    print("Erro: Hiago deve ser maior que Levi inicialmente.")
else:
    altura_levi_cm = int(altura_levi * 100)
    altura_hiago_cm = int(altura_hiago * 100)
    
    anos = 0
    
    while altura_levi_cm < altura_hiago_cm:
        altura_levi_cm += int(taxa_levi)
        altura_hiago_cm += int(taxa_hiago)
        anos += 1
        
    print(f"Serão necessários {anos} anos para que Levi seja maior que Hiago.")