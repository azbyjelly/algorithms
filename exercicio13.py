ano = int(input("Digite o ano do modelo: "))
peso = float(input("Digite o peso do modelo: "))
if ano < 1970:
    if peso < 1200:
        print("classe 1, a taxa de registro é de R$16,50")
    if 1200 <= peso <= 1700:
        print("classe 2, a taxa de registro é de R$25,50")
    if peso > 1700:
        print("classe 3, a taxa de registro é de R$46,50")
else:
    if 1971 <= ano <= 1979:
        if peso < 1200:
            print("classe 4, a taxa de registro é de R$27,00")
        if 1200 <= peso <= 1700:
            print("classe 5, a taxa de registro é de R$30,50")
        if peso > 1700:
            print("classe 6, a taxa de registro é de R$52,50")
    else:
        if ano <= 1980:
            if peso < 1600:
                print("classe 7, a taxa de registro é de R$19,50")
            if peso > 1600:
                print("classe 8, a taxa de registro é de R$55,50")
