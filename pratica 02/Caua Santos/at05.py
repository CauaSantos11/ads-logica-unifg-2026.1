### 📈 Exercício 5: Contar Positivos (Laços e Decisão)

#Solicite 10 números ao usuário usando `for` e, ao final, 
# informe quantos desses números são positivos.
#* **Dica**: Inicialize um contador em zero 
# (`contador_positivos = 0`) antes do laço.

contadorPositivo = 0

for i in range(1, 11):
    numero =   int(input('Digite 10 numeros: '))
    
    if numero > 0:
        contadorPositivo += 1 

print(f'{contadorPositivo}, são positivos')