#8) Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os 
# elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro 
# da lista, e falso em caso contrário.
def Contem(L,S): 
    if(S in L):
        print("Verdadeiro")
    else:
        print("Falso")
        
lista = ["Limão","Maracuja","Laranja","Caju","Abacaxi"]
frase = input("Digite uma fruta: ")
Contem(lista,frase)