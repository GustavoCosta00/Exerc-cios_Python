nascimento = int(input("Qual seu ano de nascimento? "))
ano_atual = 2023
idade = ano_atual - nascimento

if idade < 18:
    print("Você precisa se alistar")
else:
    print("Você não precisa mais se alistar")