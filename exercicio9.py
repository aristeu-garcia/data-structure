# 9 - No programa de estimativa de número discutido neste capítulo, o computador pensa em
# um número e o usuário insere estimativas, até que uma estimativa correta seja detectada.
# Escreva um programa no qual esses papéis sejam invertidos: o usuário pensa em um
# número e o computador calcula e fornece suposições. Como o computador na versão
# anterior desse jogo, o usuário deve fornecer dicas como “<” e “>” (significando “meu número
# é menor” e “meu número é maior”, respectivamente) quando o computador faz uma
# estimativa incorreta. O usuário insere igual “=” quando o computador faz uma estimativa
# correta. O usuário deve inserir o limite inferior e o limite superior do intervalo dos números
# na inicialização. O computador deve precisar de no máximo uma rodada (log2(alto - baixo)
# + 1 de suposições para obter o número correto. Seu programa deve rastrear o número de
# estimativas e gerar a mensagem “Você está trapaceando!” se o número de estimativas
# incorretas alcançar o máximo necessário. Eis uma interação de exemplo com esse
# programa:
# Entre com o menor número: 1
# Entre com o maior número: 100
# Seu número é 50
# Enter =, < ou >: >
# Seu número é 75
# Enter =, < ou >: <
# Seu número é 62
# Enter =, < ou >: <
# Seu número é 56
# Enter =, < ou >: =
# Uau! Eu acertei em 4 tentativas!

from random import randint

print('#### Iníciando Jogo ####')

menor = int(input("Entre com o menor número: "))
maior = int(input("Entre com o maior número: "))
random = randint(menor, maior)
chute = random
chances = 10
validacao = ''
contador = 1

print("Vamos jogar? Eu tenho 10 chances para adivinhar o número que você está pensando!\n\n")
while chances > 0:
    print("O meu chute eh: ", chute)
    validacao = input(
        "Acertei? \nDigite '>' (chutei um numero maior), '<' (chutei um numero menor) ou '=' (acertei!)\n")

    if (validacao == '>'):
        menor = chute
        chute = randint(menor+1, maior)
    elif (validacao == '<'):
        maior = chute
        chute = randint(menor, maior-1)
    elif (validacao == '='):
        print("Hahahaha! Ganhei de voce! Eu acertei em {} tentativa(s) e ainda poderia tentar mais {} vez(s)".format(chances))
        exit()
    else:
        print("ERRO! Comando não reconhecido!")
        exit()

    chances = chances - 1
    contador = contador + 1
    if (chances == 0):
        print("Ehh...parece que voce me venceu...Meus parabens!")

print('#### Fim do Jogo ####')
