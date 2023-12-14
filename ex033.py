salario = float(input("Digite o valor do seu salário: "))
aumento = 0

if salario > 1250.00:
    aumento = salario + (salario * 0.1)
    print(aumento)
else:
    aumento = salario + ( salario * 0.15)
    print(aumento)