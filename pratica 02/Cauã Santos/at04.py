## 🔐 Exercício 4: Senha até Liberar Acesso (Laços)

#Desenvolva um sistema que utilize `while` para ler uma senha repetidamente até que o usuário digite a palavra **"acesso"**.
#* **Atenção**: Lembre-se de ler a senha novamente dentro do laço para evitar um loop infinito.

senha  = input('Digite a senha: ')
acesso = 'acesso'


while senha != acesso:
    print('Acesso negado')
    senha = input('Digite a senha: ')

print('acesso concedido')


