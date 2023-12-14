cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)
print("O valor da hipotenusa é de: {:.2f}".format(hipotenusa))
