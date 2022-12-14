# 6 - O Departamento de Folha de pagamento mantém uma lista de informações do
# funcionário para cada período de pagamento em um arquivo de texto. O formato de cada
# linha do arquivo é:
# <sobrenome> <salário por hora> <horas trabalhadas> 
# Escreva um programa que insira um nome de arquivo do usuário e imprima um relatório no
# terminal dos salários pagos aos funcionários no período determinado. O relatório deve estar
# em formato tabular com o cabeçalho apropriado. Cada linha deve conter o nome do
# funcionário, as horas trabalhadas e os salários pagos naquele período.
from tabulate import tabulate
nomeArquivo = input("Informe o nome do arquivo:")
indices = ['Nome', 'Salário por hora', 'Horas Trabalhadas']
try:
    with open('./exercicio6/' + nomeArquivo, 'r') as f:
        lines = f.readlines()
        valores = []
        for index, line in enumerate(lines):
            nome = line.split(" ")[0]
            salarioHora = line.split(" ")[1]
            horasTrabalhadas = line.split(" ")[1]
            valores.append([nome, salarioHora, horasTrabalhadas])
        print(tabulate(valores, indices))

        f.close()
except Exception as e:
    print("Error:", str(e))
