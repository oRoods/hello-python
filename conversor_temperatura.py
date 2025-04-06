def celsius_para_farenheit(celsius):
    return (celsius *9/5) + 32

def farenheit_para_celsius(farenheit):
    return (farenheit - 32) *5/9
print("conversor de Temperatura")
print("1 - Celsius para Farenheit")
print("2 - Farenheit para Celsius")

opcao = input("Escolha uma opção (1 ou 2):")

if opcao == "1":
    c = float(input("Digite a temperatura em Celsius: "))
    f = celsius_para_farenheit(c)
    print(f"{c}ºC equivale a {f:.2f} ºF")
elif opcao == "2":
    f = float(input("Digite a temperatura em Farenheit: "))
    c = farenheit_para_celsius(f)
    print(f"{f}ºF equivale a {c:.2f}ºC")
else:
    print("Opção inválida. Tente 1 ou 2")