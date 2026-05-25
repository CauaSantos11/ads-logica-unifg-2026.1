#### 1) Saudacao modular
#Crie uma funcao chamada `saudacao(nome)` que receba o nome de uma pessoa e **retorne** uma mensagem de boas-vindas.

#**Requisitos:**
#3- a funcao deve usar `return`;
#- o programa principal deve chamar a funcao pelo menos **3 vezes** com nomes diferentes.

#**Exemplo esperado:**
#```python
#print(saudacao("Ana"))
# Bem-vindo(a), Ana!

nome = input("Digite seu nome: ")
def saudacao(nome):
    return f"Olá, {nome}!"
print(saudacao(nome))