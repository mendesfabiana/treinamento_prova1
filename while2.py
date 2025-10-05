# gerador de tabuada

n = int(input('\nQual a tabuada você gostaria de ver: '))
cont = 1
print('')
while cont < 10:
    tab = n * cont
    print(f'{n} x {cont} = {tab}')
    cont += 1
print('')