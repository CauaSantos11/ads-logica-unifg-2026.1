### 🎓 Exercício 11: Classificação de Turma (Contadores)

#Leia a quantidade de alunos e, em seguida, 
# suas médias. Informe ao final o total de:
#* **Aprovados**: Média >= 7.
#* **Recuperação**: Média entre 4 e 6.9.
#* **Reprovados**: Média < 4.


alunosTotal = int(input('Digite a quantidade de alunos: '))

aprovados = 0
reprovados = 0
recuperacao = 0

for i in range(1, alunosTotal + 1):
    media = float(input(f'Digite a media do {i} aluno: '))

    if media >= 7:
        aprovados += 1
        print('aprovado')
    elif media >= 4:
        recuperacao += 1
        print('Recuperação')
    else:
        reprovados += 1
        print('reprovado')

print(f'Total de aprovados: {aprovados}')
print(f'Total de recuperação: {recuperacao}')
print(f'Total de reprovados: {reprovados}')