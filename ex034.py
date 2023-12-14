r1 = float(input("Digite o valor da reta:"))
r2 = float(input("Digite o valor da reta:"))
r3 = float(input("Digite o valor da reta:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo")
else:
    print("Os segmentos acima não podem formar um triângulo")