salario = float(input("Digite seu salário: "))
valor_casa = float(input("Digite o valor da casa: "))
tempo_financiamento = int(input("quantos anos vai financiar essa casa? "))
tempo = tempo_financiamento * 12
valor_prest = valor_casa / tempo

if valor_prest < salario * 0.3:
    print("Você pode financiar essa casa!")
elif valor_prest > salario * 0.3:
    print("Olha... seu financiamento não foi aprovado.")

