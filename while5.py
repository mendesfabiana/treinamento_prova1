'''Crie um pequeno menu com opções:
(1) Somar
(2) Subtrair
(0) Sair
O programa só deve parar quando o usuário escolher a opção 0.'''

opcao = 1

while opcao != 0:
    print()
    print('[1] Somar')
    print('[2] Subtrair')
    print('[0] Sair')
    print()
    opcao = int(input('Digite a opção desejada: '))
    print()
    if opcao == 1:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        soma = n1 + n2
        print(f'soma = {soma}' )
    elif opcao == 2:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        subtr = n1 - n2
        print(f'Subtração = {subtr}')    
    elif opcao == 0:
        print('Saindo...')
        print()        
    else:
        print('Opção Inválida! Tente novamente.')


