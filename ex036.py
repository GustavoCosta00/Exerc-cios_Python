n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if n1 > n2:
    print("{} é maior do que {}".format(n1,n2))
elif n2 > n1:
    print("{} é maior do que {}".format(n2,n1))
elif n1 == n2:
    print("Os valores são iguais")