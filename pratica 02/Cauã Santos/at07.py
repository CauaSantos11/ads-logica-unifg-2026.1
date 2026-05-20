
### ➕ Exercício 7: Soma dos Pares (Acumuladores)

#Leia 8 valores inteiros e calcule a soma apenas daqueles
#  que forem números pares.
# **Objetivo**: Praticar o uso de acumuladores e filtros de paridade. 

somaPares = 0
for i in range(8):
    numero = int(input('Digite o número: '))

    # verifica se é par usando o operador módulo
    if numero % 2 == 0:
        somaPares += numero

print(f'Soma dos números pares: {somaPares}')