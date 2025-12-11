dias = int(input('digite quantos dias voce ficou com o carro:'))
km = float(input('Digite a quantidade de km rodados:'))

preco = (dias * 60) + (km * 0.15)

print('Esse é o total a pagar:{}R$'.format(preco))