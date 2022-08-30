# 3 - Um experimento científico padrão é deixar cair uma bola e ver até que altura ela quica.
# Depois que o “quicamento” da bola foi determinado, a razão fornece um índice de
# quicamento. Por exemplo, se uma bola largada de uma altura de 10 pés quica 6 pés de
# altura, o índice é de 0,6 e a distância depois de dois quique seria 10 pés + 6 pés + 6 pés
# +3,6 pés = 25,6. Observe que a distância percorrida para cada salto sucessivo é a distância
# até o chão mais 0,6 dessa distância conforme a bola volta a subir. Escreva um programa
# que permita ao usuário inserir a altura inicial da bola e o número de vezes que a bola pode
# continuar quicando. A saída deve ser a distância total percorrida pela bola

alturaInicialBola = float(input('Digite a altura inicial da bola: '))
numeroQuicarBola = float(
    input('Digite o numero de vezes que a bola pode continuar quicando: '))
quicadas = 2 * numeroQuicarBola
distanciaDepoisDeQuicar = alturaInicialBola + quicadas + 3, 6
print(distanciaDepoisDeQuicar)
