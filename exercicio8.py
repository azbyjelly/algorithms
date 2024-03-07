ano_atual = int(input("Digite um ano: "))
ano_nascimento = int(input("Digite o ano em que nasceu: "))
idade = ano_atual - ano_nascimento
print("idade:", idade)
if 0 < idade <= 3:
    print("bebe")
elif 4 < idade <= 11:
    print("criança")
elif 12 < idade <= 17:
    print("adolescente")
elif 18 < idade <= 64:
    print("adulto")
else:
    print("idoso")