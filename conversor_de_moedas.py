real = float(input('Digite um valor para saber sua conversão, não é necessário por ponto ou vírula: R$ '))
dolar = 5.49
euro = 5.61
libra = 6.59
francoS = 5.71
dolarC = 4.25
dolarA = 3.80
jpy = 0.04040
print('O valor de R$ {:.2f} convertido para dólar é US$ {:.2f}.'.format(real, real/dolar))
print('O valor de R$ {:.2f} convertido para euro é € {:.2f}.'.format(real, real/euro))
print('O valor de R$ {:.2f} convertido para libra é £ {:.2f}.'.format(real, real/libra))
print('O valor de R$ {:.2f} convertido para Franco Suiço é Fr {:.2f}.'.format(real, real/francoS))
print('O valor de R$ {:.2f} convertido para dólar Canadense é C$ {:.2f}.'.format(real, real/dolarC))
print('O valor de R$ {:.2f} convertido para dólar Australiano é A$ {:.2f}.'.format(real, real/dolarA))
print('O valor de R$ {:.2f} convertido para iene é ¥ {:.2f}.'.format(real, real/jpy))
print('=' * 70)
# Segunda forma de escrever este código.
real = float(input('Digite um valor em R$ para converter: R$ '))
dolar = real / 5.49
euro = real / 5.61
libra = real / 6.59
francoS = real / 5.71
dolarC = real / 4.25
dolarA = real / 3.80
jpy = real / 0.04040
print('O valor de R$ {:.2f} convertido para dólar é US$ {:.2f}.'.format(real, dolar))
print('O valor de R$ {:.2f} convertido para euro é € {:.2f}.'.format(real, euro))
print('O valor de R$ {:.2f} convertido para libra é £ {:.2f}.'.format(real, libra))
print('O valor de R$ {:.2f} convertido para Franco Suiço é Fr {:.2f}'.format(real, francoS))
print('O valor de R$ {:.2f} convertido para dólar Canadense é C$ {:.2f}.'.format(real, dolarC))
print('O valor de R$ {:.2f} convertido para dólar Australiano é A$ {:.2f}.'.format(real, dolarA))
print('O valor de R$ {:.2f} convertido para iene é ¥ {:.2f}.'.format(real, jpy))