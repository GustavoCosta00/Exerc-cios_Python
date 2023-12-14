distancia = int(input("Quak a distância da viagem?"))
valor = 0

if distancia <= 200:
    valor = distancia * 0.50
    print("O valor da passagem é de {}".format(valor))
else:
    valor = distancia * 0.45
    print("O valor da passagem é de {}".format(valor))