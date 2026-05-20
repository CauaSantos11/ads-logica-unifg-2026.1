### 🍕 Exercício 3: Divisão Justa (Divisão Inteira e Módulo)
#Crie um programa para dividir fatias de pizza entre uma equipe, perguntando:
#* O número total de fatias.
#* O número de programadores na equipe.

#Calcule e imprima quantas fatias inteiras cada um comerá e o resto que sobrará na caixa.

#**Fórmulas:**
#* $Fatias_{PorPessoa} = Total_{Fatias} // Programadores$
#* $Sobra = Total_{Fatias} \% Programadores$

fatiaspizzas = int(input('Quantas fatias de pizza tem? '))
pessoas = int(input('quantas pessoas tem?'))

fatiasPessoas = fatiaspizzas / pessoas


print(f'todo mundo vai comer{fatiasPessoas} fatias')
