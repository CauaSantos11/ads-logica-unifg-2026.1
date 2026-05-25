#### 8) Depuracao de erro sintatico
#O codigo abaixo contem erro:

#```python
#def saudacao(nome)
#    print("Ola,", nome)

#**Sua tarefa:**
##- corrigir o codigo;
#- dizer qual era o erro;
#- explicar por que o programa nao executava.

#codigo corrigido:

nome = input('Qual seu nome: ')

def saudacao(nome):
    return f'Olá {nome}, bem-vindo'

print(saudacao(nome))