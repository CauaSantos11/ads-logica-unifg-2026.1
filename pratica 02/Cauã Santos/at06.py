### 📝 Exercício 6: Validação de Nota (Laços)

#Peça uma nota entre 0 e 10. Se o usuário digitar um valor inválido, 
#use `while` para repetir a pergunta até que uma nota válida seja inserida.
#* **Critério**: O programa deve continuar enquanto `nota < 0` ou `nota > 10`.

nota = int(input('Digite a nota'))

while nota < 0 or nota > 10:
    print('Nota inválida! Digite uma nota entre 0 e 10.')
    nota = int(input('Digite a nota: '))

print(f'Nota válida: {nota}')