## ⚖️ Exercício 3: Par ou Ímpar (Laços e Decisão)

#Utilizando a estrutura `for`, percorra os números de 1 a 20 e informe se cada um deles é par ou ímpar.
#* **Regra**: Utilize o operador de módulo `numero % 2 == 0` para verificar a paridade.

for i in range(1, 21):
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        print('Par')
    else:
        print('Ímpar')