sala = float(input('Qual é o salário do funcionário? R$'))
aumento = sala + (sala*0.15)
print('Um funcionário ganhava R${:.2f}, com o aumento de 15%, passa a receber {:.2f}'.format(sala,aumento))