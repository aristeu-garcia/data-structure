# 5 - A TidBit Computer Store tem um plano de crédito para compras de computadores. Há
# um pagamento inicial de 10% e uma taxa de juros anual de 12%. Os pagamentos mensais
# são 5% do preço de compra listado menos o pagamento inicial. Escreva um programa que
# considere o preço de compra como entrada. O programa deve exibir uma tabela, com
# cabeçalho apropriado, de um cronograma de pagamento durante o tempo de vida do
# empréstimo. Cada linha da tabela deve conter os seguintes itens:
# ● O número do mês (começando com 1)
# ● O saldo total atual devido
# ● Os juros devidos naquele mês
# ● O valor do principal devido naquele mês
# ● O pagamento daquele mês
# ● O saldo remanescente após o pagamento
# O valor dos juros para um mês é igual ao saldo * taxa / 12. O valor do principal de um mês é
# igual ao pagamento mensal menos os juros devidos.
from tabulate import tabulate

valor = float(input("Informe o valor de sua compra: "))
indices = ['Mês', 'Saldo atual devido', 'Juros mensal',
           'Valor Mensal Principal', 'Pagamento mensal', 'Saldo remanescente']


def mostraTabela():

    meses = 1
    saldoRemanescente = 0
    saldoDevido = valor
    pagamentoInicial = 0
    pagamentoMensal = 0
    taxa = 0
    juros = 0
    valorMensalPrincipal = 0
    valores = []
    while True:
        pagamentoInicial = (10/100) * valor
        if (meses == 1):
            taxa = 10/100
            pagamentoInicial = (22/100) * valor

        if ((meses / 12) % 2 == 0 and meses >= 1):
            taxa = 10/100
            pagamentoInicial = pagamentoInicial + ((12/100) * valor)

        pagamentoMensal = pagamentoInicial - ((5/100) * valor)
        saldoDevido = saldoDevido - pagamentoMensal
        if (saldoDevido <= 0):
            break
        juros = (saldoDevido * taxa) / 12
        valorMensalPrincipal = pagamentoMensal-juros
        saldoRemanescente = saldoRemanescente + pagamentoMensal

        valores.append([meses, saldoDevido, juros, valorMensalPrincipal,
                        pagamentoMensal, saldoRemanescente])
        meses = meses + 1
    print(tabulate(valores, indices))


mostraTabela()
