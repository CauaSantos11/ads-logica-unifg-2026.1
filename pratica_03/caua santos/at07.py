#### 7) Refatorando codigo monolitico
#Transforme o codigo abaixo em uma solucao modular:

#```python
#n1 = 8
#n2 = 6
#media = (n1 + n2) / 2

#if media >= 7:
  #  print("Aprovado")
#else:
  #  print("Reprovado")
#```

#**Requisitos:**
#- criar pelo menos **2 funcoes**;
#- uma funcao deve calcular a media;
#- outra funcao deve verificar a situacao.

#**Objetivo:** perceber a diferenca entre codigo monolitico e codigo modular.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

def media(n1,n2):
    return (n1 + n2)  / 2

resultadoMedia = media(n1,n2)

def situacao(resultadoMedia):
    if resultadoMedia >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

print(situacao(resultadoMedia))
