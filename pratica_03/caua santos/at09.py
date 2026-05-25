#### 9) Depuracao de erro de execucao
#Analise o codigo:

#```python
#def dividir(a, b):
#    return a / b

#print(dividir(10, 0))
#```

#**Faca o seguinte:**
#1. Explique que erro acontece.
#2. Diga por que ele ocorre.
#3. Reescreva o programa para evitar esse problema.

#**Desafio extra:** mostrar uma mensagem amigavel quando `b == 0`.

#a e b não estão definidos 

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o primeiro número: '))

def dividir(a,b):
    if b == 0:
        return 'incompativel'
    
    else:
        return a / b

print(dividir(a,b))