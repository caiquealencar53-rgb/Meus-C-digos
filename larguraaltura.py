larg = float(input('Digite a a largura da parede:'))
alt = float(input('Digite a a altura da parede:'))
area = larg * alt
print('A sua parede tem a dimensão de {} x {} e a area de {}'.format(larg,alt,area))
tinta = area / 2
print('Pra pintar ess=ta parede voçê precisará de {}l de tinta'.format(tinta))