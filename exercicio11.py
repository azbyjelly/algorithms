horas_trabalhadas = int(input("digite o numero de horass trabalhadas: "))
if horas_trabalhadas <= 40:
    salario_semanal = horas_trabalhadas * 15
else:
    salario_semanal = 600 + (horas_trabalhadas - 40) * 21
print("o salario semanal é R$", salario_semanal)