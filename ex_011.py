prod = float(input('Qual o preço do produto? R$'))
# Desconta 5% do preço total do mesmo produto
avista = prod - (prod*0.05)
# Adicona 8% do preço total do mesmo produto
parc = prod + (prod*0.08)
print('O produto que custa R${:.2f}, a vista ira ter um desconto de 5%, custando agora R${:.2f}'.format(prod,avista))

print('Caso queira parcelar, o produto que custava R${:.2f}, ira ter um amento de 8%, no total será R${:.2f}'.format(prod,parc))
