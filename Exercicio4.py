# 4 - O matemático alemão Gottfried Leibniz desenvolveu o seguinte método para aproximar o
# valor de : 𝛑
# 𝛑/4 = 1 - 1/3 + 1/5 - 1/7 + …
# Escreva um programa que permita ao usuário especificar o número de iterações usadas
# nessa aproximação e exibir o valor resultante
numInteracoes = int(input("Digite o número de interações que serão usadas: "))

if (numInteracoes >= 1):
    valorInicial = 1
    i = 1
    resultado = float(valorInicial)
    a = 3

    while i < numInteracoes:
        if (i % 2 == 0):
            resultado = resultado + (1 / a)
        elif (i % 2 != 0):
            resultado = resultado - (1 / a)
        a = a + 2
        i = i + 1

    print("\n\nResultado da soma: ")
    print("%.2f" % resultado)
else:
    print("\nErro! O número de interações não pode ser menor que 1 (um)! ")
