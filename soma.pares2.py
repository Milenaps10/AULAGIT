numero = int(input('Qual número você gostaria de ter a somatória dos pares?'))
conta = 0
resultado = 0
while not conta == numero:
  conta = conta + 2
  resultado = resultado + conta
print('O resultado da soma dos pares de {} é: {}' .format(numero, resultado))