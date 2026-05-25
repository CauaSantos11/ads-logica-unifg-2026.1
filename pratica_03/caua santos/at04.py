### 4) Situacao do aluno
#Crie uma funcao `verificar_situacao(media)` que:
#- retorne `"Aprovado"` se `media >= 7`;
#- retorne `"Reprovado"` caso contrario.

#Depois, integre essa funcao com a funcao do exercicio anterior.

#**Objetivo:** dividir calculo e decisao em partes diferentes.

media = float(input('digite a sua media: '))

def verificarSituacao(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

print(verificarSituacao(media))