from random import randint
altura = ''
largura = ''
escolha = 'a b'

while not altura.isnumeric():
    altura = input('Digite uma altura: ')
while not largura.isnumeric():
    largura = input('Digite uma largura: ')
altura = int(altura)
largura = int(largura)

while True:
    escolha = input('Digite uma posição no formato (linha coluna): ').split()
    if len(escolha) == 2:
        if escolha[0].isnumeric() and escolha[1].isnumeric():
            escolha[0] = int(escolha[0])
            escolha[1] = int(escolha[1])
            if escolha[0] < altura and escolha[1] < largura:
                break
print(escolha)
lista = [[0 for l in range(largura)] for a in range(altura)]
lista[randint(0,altura-1)][randint(0,largura-1)] = 1

if lista[int(escolha[0])][int(escolha[1])] == 1:
    print('Você acertou a bomba')
for i in range(altura):
    for j in range(largura):
        print(lista[i][j], end=' ' if j != largura - 1 else '\n')
