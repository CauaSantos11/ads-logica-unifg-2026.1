### 🎂 Exercício 2: Faixa Etária Essencial (Decisão)

 #* **Menor de idade**: Menos de 18 anos.
#* **Maior de idade**: Entre 18 e 59 anos.
# **Idoso**: 60 anos ou mais.

idade = int(input("Qual sua idade? "))

if idade <= 17:
    print("Menor")
elif idade >=18:
    print("Maior")
elif idade > 59:
    print("velho")