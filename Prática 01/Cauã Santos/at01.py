### 💻 Exercício 1: O Registro do Sistema (I/O e Tipagem)
#Crie um programa que simule o registro de um novo usuário, solicitando as seguintes informações:
#* **Nome do usuário** (string).
#* **Ano de nascimento** (inteiro).
#* **Altura em metros** (float).

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
altura = float(input("Qual sua altura? "))

anoDeNascimento = 2026 - idade

print(f'Olá {nome}, você nasceu no ano {anoDeNascimento} e tem {altura}cm de altura')