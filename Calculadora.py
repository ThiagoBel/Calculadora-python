while True:
    print("[1] = Adicao\n[2] = Subtracao\n[3] = Multiplicacao\n[4] = Divisao\n[5] = Sair")
    valor = int(input())

    if valor == 1:
        va1 = int(input("Primeiro numero: "))
        va2 = int(input("Segundo numero: "))

        rsa = va1 + va2

        print(str(va1) + " + " + str(va2) + " = " + str(rsa))
    elif valor == 2:
        vs1 = int(input("Primeiro numero: "))
        vs2 = int(input("Segundo numero: "))

        rss = vs1 - vs2

        print(str(vs1) + " - " + str(vs2) + " = " + str(rss))
    elif valor == 3:
        vm1 = int(input("Primeiro numero: "))
        vm2 = int(input("Segundo numero: "))

        rsm = vm1 * vm2

        print(str(vm1) + " * " + str(vm2) + " = " + str(rsm))
    elif valor == 4:
        vd1 = int(input("Primeiro numero: "))
        vd2 = int(input("Segundo numero: "))

        rsd = vd1 / vd2

        print(str(vd1) + " / " + str(vd2) + " = " + str(rsd))
    elif valor == 5:
        print("Ok")
        break
    else:
        print("?")