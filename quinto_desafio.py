def inverter_string(s):
    inverted = ''
    for i in range(len(s)-1, -1, -1):
        inverted += s[i]
    return inverted

# Exemplo de uso
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
