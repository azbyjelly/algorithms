def inverte_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# Exemplo de string
string = input("Digite uma string para inverter: ")
print(f"String invertida: {inverte_string(string)}")
