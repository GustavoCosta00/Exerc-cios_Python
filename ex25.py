frase = input("Digite uma frase: ")
qtd_letra_a = frase.count("a")
primeiro_a = frase.find("a")
ultimo_a = frase.rfind("a")

print("A quantidade de 'a' é {}\n o primeiro 'a' aparece em {}\n o ultimo 'a' aparece em {}".format(qtd_letra_a, primeiro_a, ultimo_a))