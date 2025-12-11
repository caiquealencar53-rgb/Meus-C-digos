salario = float(input('Digite o salario atual: R$'))
reajuste = salario + (salario * 15/ 100)
print('O seu salrio de {:.2f}R$ foi reajustado para {:.2f}R$ um aumento de 15%'.format(salario,reajuste))