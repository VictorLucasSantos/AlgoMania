# O Two Sum é bastante comum durante entrevistas. Seu objetivo é identificar um par de números que somados batam com o valor da variável target.

# Ele pode ser escrito em um algoritmo que roda no tempo O(n).

# Exemplos
# Se o array é [4, 1, 2, -2, 11, 15, 1, -1, -6, -4] e o target é 9. Neste caso, seu programa deve retornar:

# [-2, 11]

# O motivo é bastante simples:

# -2 + 11 = 9

# # A solucao deve estar implementada dentro da função abaixo.
# # Dica: Você pode criar outras funções e classes se quiser mas esta é a função principal que será usada.


# def solution(numbers, target_sum):
#     pass

def solution(numbers, target_sum):
    seen = {}
    for indx, value in enumerate(numbers):
        complemento = target_sum - value
        if complemento in seen:
            return [complemento, value]
            break
        seen[value] = indx
    return []
            
solution([4, 1, 2, -2, 11, 15, 1, -1, -6, -4], 9)