#Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o 
# número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os 
# valores de máximo e mínimo, e falso em caso contrário.

def Valida(S,min,max):
    if(len(S) <= max and len(S) >= min):
        print("Verdadeiro")
    else:
        print("falso")

minimo = int(input("digite a quantidade minima de caracteres: "))
maximo = int(input("digite a quantidade maxima de caracteres: "))

palavra = input(f"digite uma palavra com a quantidade de caracteres entre {minimo} e {maximo}: ")
Valida(palavra,minimo,maximo)