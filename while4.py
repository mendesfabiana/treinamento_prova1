'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]

while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Informe novamente: ').strip().upper()[0]
print(f'Sexo {sexo} registro com sucesso!')
