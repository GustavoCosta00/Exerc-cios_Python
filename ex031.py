ano = int(input("Digite um ano"))
ano_bi = ano % 4

if ano_bi == 0:
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")