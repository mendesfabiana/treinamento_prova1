# Peça 5 notas, guarde em uma lista e depois mostre a média e a maior nota.

lista = []
cont = 0

while cont < 5:
    notas = float(input(f'Digite a {cont + 1}ª nota: '))
    lista.append(notas)
    cont += 1
    media = sum(lista) / len(lista)
    maior = max(lista)
print()   
for notas in lista:
    print(notas,end=' - ')
print()
print(f'Média: {media}')
print(f'Maior nota: {maior}')
print()