### 🔄 Exercício 14: Refatoração (While para For)

#Escolha um exercício anterior que você resolveu com `while` 
#e reescreva-o obrigatoriamente utilizando a estrutura `for`. Explique se a leitura do código ficou mais simples

#nota = int(input('Digite a nota'))

#while nota < 0 or nota > 10:
#    print('Nota inválida! Digite uma nota entre 0 e 10.')
#    nota = int(input('Digite a nota: '))

#print(f'Nota válida: {nota}')

#atividade 6,w complicado por pro for, tive q usaar a ia pra me  explicar o passo a passo e porque de cada alteração

print('Digite 1-Somar;2-Subtrair e 0-Sair')

for i in range(10):

    opcao = int(input('Digite a opção: '))

    if opcao == 0:
        break

#esse seria oo codigo de  while para for, fica melhor quando voce quer por um limite nas tentativa, por exemplo senhas de emails, banco, etc.


