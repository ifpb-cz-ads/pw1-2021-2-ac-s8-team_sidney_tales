def maximo(n1, n2):
    if (n1 > n2):
        print("O numero maior é: %d"%(n1))
    elif (n1 < n2):
        print("O numero maior é: %d"%(n2))
    else:
        print("Os numeros %d e %d são iguais"%(n1,n2))

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

maximo(n1, n2)