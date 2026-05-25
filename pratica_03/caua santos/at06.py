#### 6) Escopo basico na pratica
#Analise o codigo abaixo:

#```python
#x = 10

#def teste():
  #  y = 5
 #   return x + y

#print(teste())
#```

#**Faca o seguinte:**
#1. Identifique qual variavel e **global**.
#2. Identifique qual variavel e **local**.
#3. Explique o que acontece se tentarmos usar `y` fora da funcao.
#4. Crie um exemplo parecido feito por voce.

#**Objetivo:** compreender escopo local e global.

#A variavel global é o x; A variavel local é o y; se tentar usar o y fora da função, da erro no código, porque a variavel
#local só fica dentro da função;

a = 10

def  teste():
    y = 5 
    return a + y

print(teste())
