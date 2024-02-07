# Definindo a lista de produtos original
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Atualizando os produtos
lista_produtos[1] = "rímel"
lista_produtos[4] = "cremes hidratantes"

# Removendo o delineador da lista
del lista_produtos[-1]

# Imprimindo a lista atualizada
print("Nova lista de produtos:")
for produto in lista_produtos:
    print(f"- {produto}")