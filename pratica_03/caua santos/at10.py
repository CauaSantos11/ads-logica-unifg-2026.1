#### 10) Teste de mesa + caso de teste#
#Considere o codigo abaixo:

#```python
#def calcular_total(preco, quantidade):
#    subtotal = preco * quantidade
#   desconto = subtotal * 0.1
#   total = subtotal - desconto
#    return total
##```

#**Parte A - Teste de mesa**
#Monte uma tabela com os valores de:
#- `preco`
##- `quantidade`
#- `subtotal`
#- `desconto`
#- `total`

#Use a chamada:
#```python
##calcular_total(50, 2)


#**Parte B - Casos de teste**
##Crie pelo menos:
#- 2 casos normais;
#- 1 caso limitrofe;
#- 1 caso extremo.

#**Objetivo:** praticar validacao de funcoes por analise e teste.

preco = float(input('Informe o preço do produto: '))
quantidade = int(input('Informe o quantidade do produto: '))

def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

print(calcular_total(preco,quantidade))

