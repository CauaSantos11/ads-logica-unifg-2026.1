### 💵 Exercício 9: Reajuste Salarial por Faixa (Decisão)

#Aplique um percentual de reajuste ao salário informado seguindo a tabela:
#* **Até R$ 1.500,00**: 15% de aumento.
#* **De R$ 1.500,01 a R$ 3.000,00**: 10% de aumento.
#* **Acima de R$ 3.000,00**: 5% de aumento.

salario = float(input('informe seu salario: '))

if salario <= 1500.00:
    aumento1 = salario * 1.15
    print(f'{aumento1:.2f} é seu novo salario')

elif salario > 1500.00:
    aumento2 = salario * 1.10
    print(f'{aumento2:.2f} é seu novo salario')

elif salario >3000.00:
    aumento3 = salario * 1.05
    print(f'{aumento3:.2f} é seu novo salario')
