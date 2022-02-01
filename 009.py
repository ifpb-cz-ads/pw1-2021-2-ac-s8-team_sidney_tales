#9) Altere o programa abaixo de forma que o usuário tenha três chances de acertar o número. 
# O programa termina se o usuário acertar ou errar três vezes. A função ‘random.randint(x, y)’
# recebe como parâmetros dois inteiros, x e y, e retorna um outro inteiro escolhido aleatoriamente 
# entre x e y.

import random
n=random.randint(1,10)
z = 3

while(z >= 0):
    
    x=int(input("Escolha um número entre 1 e 10: "))
    if (x==n):
        print("Você acertou!")
        z = -1
    else:
        z=z-1
        print(f"Você errou. Restam {z} tentativas")
        if (z == 0):
            print("Fim de Jogo, você perdeu")

    
