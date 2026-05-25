#### 5) Boletim simples com modularizacao
#Crie um programa para um boletim simples, obrigatoriamente dividido em funcoes.

#**O programa deve ter, no minimo, estas funcoes:**
#- `ler_notas()`
#- `calcular_media(n1, n2)`
#- `verificar_situacao(media)`
#- `exibir_resultado(nome, media, situacao)`

#**Objetivo:** praticar decomposicao do problema em partes menores e reutilizaveis.

nome = input("Digite seu nome: ")

def saudacao(nome):
    return f"Olá, {nome}!"
                                                            
print(saudacao(nome))

n1 =  int(input("digite sua primeira nota: "))
n2 =  int(input("digite o segunda nota: "))

def calcular_media(n1,n2):
    return (n1 + n2) / 2

print(calcular_media(n1,n2))

media = calcular_media(n1,n2)

def verificarSituacao(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
print(verificarSituacao(media))
