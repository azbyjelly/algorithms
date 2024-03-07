salario_anual = float(input("Digite seu salario: "))
tempo_de_serviço = float(input("Digite seu tempo de serviço: "))
if tempo_de_serviço > 365:
    print(f"reajuste = {salario_anual + salario_anual * 0.20}")
else:
    print(f"reajuste = {salario_anual + salario_anual * 0.10}")
    