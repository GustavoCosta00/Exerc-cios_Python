vel = int(input("Digite a velocidade do seu carro: "))
vel_limite = 80

if vel > vel_limite:
    print("Você ultrapassou a velocidade limite e foi multado!")
    multa = (vel - vel_limite) * 7
    print(" Você recebeu uma multa de {}".format(multa))
else:
    print("Você não foi multado")