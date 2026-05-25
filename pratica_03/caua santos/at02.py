#### 2) Soma com parametros
#Crie uma funcao chamada `somar(a, b)` que receba dois numeros e retorne a soma.

#**Requisitos:**
#- testar com numeros inteiros;
##- testar com um caso usando zero;
#- testar com um caso usando numero negativo.

#**Objetivo:** praticar parametros, argumentos e retorno.

a =  int(input("digite o primeiro numero: "))
b =  int(input("digite o segundo numero: "))

def somar(a,b):
    return a + b

print(somar(a,b))