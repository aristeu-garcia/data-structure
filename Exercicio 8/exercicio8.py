# 8 - Escreva um programa que permita ao usuário navegar pelas linhas de texto em um
# arquivo. O programa deve solicitar ao usuário um nome de arquivo e inserir as linhas de
# texto em uma lista. O programa então deve entrar em um laço no qual imprima o número de
# linhas no arquivo e solicite ao usuário um número de linha. Os números reais das linhas
# variam de 1 ao número de linhas no arquivo. Se a entrada for 0, o programa deve ser
# encerrado. Do contrário, o programa deve imprimir a linha associada a esse número.
nomeArquivo = input("Digite o nome do arquivo que deseja acessar: ")

contador = 0
escolha = ''
linhaArmazenada = []

if (nomeArquivo == "arquivo-um.txt" or nomeArquivo == "arquivo-dois.txt" or nomeArquivo == "arquivotres.txt"):
    with open("./" + nomeArquivo, "r") as arquivo:
        texto = arquivo.readlines()
        for linha in texto:
            contador = contador + 1
            print("Linha {}".format(contador))
        escolha = int(
            input("Digite qual o número de linha que deseja imprimir: "))

        if (escolha > 0 and escolha <= contador):
            for linha in texto:
                linhaArmazenada.append(linha)
        else:
            print("ERRO! Numero de linha invalido!")
            exit()
        print("Resultado: \n")
        print(linhaArmazenada[escolha-1])
else:
    print("ERRO! ESSE ARQUIVO COM ESSE NOME NÃO EXISTE!")
