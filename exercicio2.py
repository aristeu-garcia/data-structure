# 2 – O pagamento semanal total de um funcionário é igual ao salário por horas multiplicado
# pelo número total de horas regulares mais qualquer pagamento de horas extras. O
# pagamento de horas extras é igual ao total de horas extras multiplicado por 1,5 vez o salário
# por hora. Escreva um programa que receba como entradas o salário por hora, o total de
# horas regulares e o total de horas extras e exiba o pagamento semanal total de um
# funcionário.


salarioHora = float (input('Digite o salario hora: '))
horaRegular = float (input('Digite as horas regulares: '))
horasExtras = float (input ('Digite o numero de horas extras: '))

calcSalario = 1.5 * salarioHora
calcHoraExtra = horasExtras * calcSalario
semanal = salarioHora * horaRegular + horasExtras

print("Semanal",semanal)
print("Horas extras",calcHoraExtra)