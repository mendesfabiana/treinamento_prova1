# Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas e os mostre na tela.

lista = []
cont = 0

while cont < 5:
    nomes = lista.append(input('Digite um nome: '))
    cont += 1
print('')   
for nomes in lista:
    print(nomes,end='  ')
       
