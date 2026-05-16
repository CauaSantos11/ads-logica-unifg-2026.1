### #💰 Exercício 2: Calculadora de Freelancer (Matemática)
#esenvolva um script para calcular o valor de um projeto freelancer solicitando:
#1. O valor cobrado por hora.
#2. A estimativa de horas para conclusão.

##Exiba o **valor bruto**, o **valor dos impostos (15%)** e o 
# **valor líquido final**.

#**Fórmulas:**
#* $Valor_{Bruto} = Horas \times Valor_{Hora}$
#* $Impostos = Valor_{Bruto} \times 0.15$
#* $Valor_{Liquido} = Valor_{Bruto} - Impostos$

valorHora = float(input('Valor cobrado por hora: '))
hora = int(input('Tempo estimado para conclusão: '))

valorBruto = hora / valorHora
imposto = valorBruto * 0.15
valorLiquido = valorBruto - imposto

print(f'Valor Bruto{valorBruto}, valor liquido{valorLiquido} e imposto de {imposto}')