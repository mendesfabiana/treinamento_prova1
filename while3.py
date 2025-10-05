# testando
lista = []
cont = 0

while cont < 10:
    n = lista.append(int(input('Digite um número: ')))
    cont += 1
print('')
print(lista)

par = 0
impar = 0

for n in lista:
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f'Par: {par} \nImpar: {impar}\n')