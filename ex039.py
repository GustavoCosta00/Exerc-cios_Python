nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2023 - nascimento

if idade <= 9:
    print("Nadador MIRIM")
elif idade > 9 and idade <= 14:
    print("Nadador INFANTIL")
elif idade > 14 and idade <= 19:
    print("Nadador JUNIOR")
elif idade > 19 and idade <= 25:
    print("Nadador SÊNIOR")
elif idade > 25:
    print("Nadador MASTER")
    
