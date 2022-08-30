# 7 - Os estatísticos gostariam de ter um conjunto de funções para calcular a mediana e o
# modo de uma lista de números. A mediana é o número que apareceria no ponto médio de
# uma lista se fosse ordenada. O modo é o número que aparece com mais frequencia na lista.
# Defina essa funções em um módulo denominado stats.py. Também inclui uma função
# chamada mean, que calcula a média de um conjunto de números. Cada função espera uma
# lista de números como um argumento e retorna um único número.

import statistics

lista = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11]

mediana = statistics.median(lista)
modo = statistics.mode(lista)
media = statistics.mean(lista)

print("Mediana: %.2f" % mediana)
print("Modo: %.2f" % modo)
print("Media: %.2f" % media)
