salario = float(input("digite seu salario: "))
financiamento = float(input("digite o financiamento: "))
if financiamento <= salario * 5:
    print("financiamento concedido")
else:
    print("financiamento negado")