## 🏆 Exercício 15: Desafio - Maior Nota (Busca)

#Leia 5 notas de alunos e, utilizando um laço `for`, informe qual foi a maior nota encontrada no grupo.
#* **Dica**: Inicialize a variável `maior` com um valor bem baixo ou com a primeira nota lida.

alunosTotal = 5

for i in range(1, alunosTotal + 1):
    media = float(input(f'Digite a media do {i} aluno: '))
