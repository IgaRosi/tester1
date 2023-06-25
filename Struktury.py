dozwoloneWaluty = ('PLN','EUR','USD')
# waluta = input('Podaj walutę: ')
# if waluta.upper() in dozwoloneWaluty:
#     print('poprawna waluta')
# else:
#     print(f'nieznany kod waluty, podano: {waluta}')
#     print('nieznany kod waluty, podano: {}'.format(waluta))
#     print('nieznany kod waluty, podano: %s' % waluta)

lista = []
# lista.append('Iga')
lista.append('Ala')
lista.append('Mona')
lista.insert(1,'Ewa')
lista.append(dozwoloneWaluty)
# lista.sort()
lista.pop()


print(lista)




