# 1 – Escreva um programa que receba o raio de uma esfera (um número ponto flutuante)
# com entrada e produza o diâmetro, da circunferência, a área da superfície e o volume da
# esfera.

import math


raio = float(input('Digite o valor do raio de uma esfera: '))

diametro = raio ** 2

quadrado = raio * raio
area = math.pi * quadrado

print ("Area: {:.4f}".format(area))
print ("Diametro: {:.4f}".format(diametro))
