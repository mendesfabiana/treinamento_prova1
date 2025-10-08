# somar números até o usuário digitar 0

soma = 0
num = int(input('Digite um número para somar ou [0 para sair]: '))

while num != 0:
    soma += num
    num = int(input('Digite outro número ou [0 para sair]: '))
print('Saindo...')
print()
print(f'Soma: {soma}')
print()