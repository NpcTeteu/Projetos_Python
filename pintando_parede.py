larg = float(input("Qual a largura de sua parede em metros: "))
comp = float(input("Qual o comprimento de sua parede em metros: "))
dimen = float (larg*comp)
tinta = dimen / 2
print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e a sua área é de {:.2f}m²'.format(larg,comp,dimen))
print('Para pintar sua parde é necessário {:.2f}L de tinta'.format(tinta))