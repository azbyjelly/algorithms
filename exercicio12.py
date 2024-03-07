tempo_fundos = float(input("Digite quanto tempo os fundos foram mantidos em deposito: "))
if tempo_fundos < 1:
    print("a taxa de juros é de 0.55")
else:
    if tempo_fundos < 2:
        print("a taxa de juros é de 0.65")
    else:
        if tempo_fundos < 3:
            print("a taxa de juros é de 0.75")
        else:
            if tempo_fundos < 4:
                print("a taxa de juros é de 0.85")
            else:
                if tempo_fundos < 5:
                    print("a taxa de juros é de 0.90")
                else:
                    print("a taxa de juros é de 0.95")

