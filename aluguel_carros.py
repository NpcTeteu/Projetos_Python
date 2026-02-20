dias = int(input("Quantos dias o carro foi alugado? "))
kms = float(input("Quantos km o carro roudou? "))
preço = (dias*60.00) + (kms*0.15)
print("O preço que deve ser cobrado é de {:.2f}".format(preço))