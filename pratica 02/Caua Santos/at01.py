### 💻 Exercício 1: Classificação de Número (Decisão)

#Crie um programa que leia um número inteiro e informe se ele é positivo, negativo ou zero.
#* **Objetivo**: Praticar `if/elif/else` com faixas exclusivas.
#* **Dica**: Teste com os valores 0, 5 e -3.

numero = int(input("Digite um número: "))

if numero == 0:
    print("seu número é zero")
elif numero >= 1:
    print("Seu numero é positivo")
else:
    print("Seu numero é negativo")