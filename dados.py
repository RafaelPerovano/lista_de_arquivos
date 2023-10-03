tamanho = int(input('Digite a quantidade de numeros que deseja guardar: '))
c = 0
numeros = []
soma = 0
while c <= tamanho-1:
    n = str(input('Digite o numero {}: '.format(c+1)))
    numeros.append(n)
    c += 1
c = 0

with open ('arquivo.txt', 'w') as arquivo:
    for n in numeros:
        arquivo.write(n)
        arquivo.write('\n')

with open ('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        c += 1
        soma += int(linha)
    
media = soma/c
print('A media dos numeros é igual a:', media)