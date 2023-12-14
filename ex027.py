import random
numero = random.randint(1,10)
print(numero)

valor_usuario = int(input("Digite um número de 1 a 10: "))

if valor_usuario == numero:
    print("Você adivinhou o número")
else:
    print("O valor sorteado não é igual!")
