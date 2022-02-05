#5) Reescreva a função abaixo de forma a utilizar os métodos de pesquisa em lista, vistos na aula passada. 
# A função ‘enumerate’ recebe uma lista como parâmetro e retorna uma lista de tuplas, estas 
# formada por pares (índice, valor). O valor ‘None’ é o valor nulo da linguagem Python, similar ao ‘null’ 
# de Java e JavaScript.

def pesquise(lista, valor):
    if(not lista.index(valor)):
        return None
    return lista.index(valor), valor

L = [1,2,3,5,4]
print(pesquise(L, 5))
