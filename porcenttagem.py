preco = float(input('Digite o preço do produto: R$'))
novopreco = preco - (preco* 5 / 100)

print('Esse é o valor do produto:R${}'.format(preco))
print('Esse é o valor do produto com desconto de 5%:R${}'.format(novopreco))