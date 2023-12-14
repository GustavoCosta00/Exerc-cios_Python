preco = float(input("Digite o preço do produto: "))
desconto = (preco * 5 / 100)
precoFinal = preco - desconto
print("O preço final desse produto com desconto é de: {}".format(precoFinal))