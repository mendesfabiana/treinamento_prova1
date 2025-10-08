# Peça números até que a soma deles passe de 100.

cont = 0
soma = 0

while soma <= 100:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
print()
print(f'Foram digitados {cont} números e a soma deles foi {soma}')
print()