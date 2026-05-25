#### 3) Media de aluno
#Crie uma funcao `calcular_media(n1, n2)` que receba duas notas e retorne a media aritmetica.

#**Depois:**
#- peca ao usuario duas notas;
#- chame a funcao;
#- exiba a media retornada.

#**Desafio extra:** formatar a media com uma casa decimal.

n1 =  int(input("digite sua primeira nota: "))
n2 =  int(input("digite o segunda nota: "))

def calcular_media(n1,n2):
    return f'Sua media é {(n1 + n2) / 2}'

print(calcular_media(n1,n2))