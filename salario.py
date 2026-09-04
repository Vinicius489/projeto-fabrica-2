import os
os.system ("cls")

valor_hora = float(input("Digite quanto você ganha por hora: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))

salario = valor_hora * horas

print(f"Seu salário do mês é: R$ {salario:.2f}")