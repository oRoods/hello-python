def soma_lista(lista):
    total = 0
    for numero in lista:
        total +=numero
    return total
entrada = input("Digite os número da sua lista separando-os com vírgulas")
numeros = entrada.split(",")
numeros =[int(num.strip()) for num in numeros]
print("Soma total:", soma_lista(numeros))