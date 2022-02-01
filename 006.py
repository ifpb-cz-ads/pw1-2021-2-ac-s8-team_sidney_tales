#6) Reescreva o programa da abaixo de forma a utilizar for em vez de while.

def soma(L):
    total=0
    x = 1
    for x in L:
        total = total + x
    return total

print(soma([5,4,3,2,1]))
