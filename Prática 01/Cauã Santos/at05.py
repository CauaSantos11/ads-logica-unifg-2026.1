### 🚀 Exercício 5: Desafio do Download (Mistura de Conceitos)
#Calcule o tempo estimado de download solicitando:
#1. O tamanho do arquivo em **Megabytes (MB)**.
#2. A velocidade da internet em **Megabits por segundo (Mbps)**.

#**Regra de Negócio:** Considere que 1 Byte = 8 bits. Converta o tempo total para minutos inteiros e segundos restantes.

#**Fórmulas:**
#* $Tempo_{Segundos} = \frac{Tamanho_{MB}}{(Velocidade_{Mbps} / 8)}$
#* $Minutos_{Inteiros} = Tempo_{Segundos} // 60$
#* $Segundos_{Restantes} = Tempo_{Segundos} \% 60$

#**Saída:** "X minutos e Y segundos".

arquivo = float( input("Qual o tamanho do arquivo(MB): ") )
velocidade = float(input("Qual a velocidade da internet(MMBPS):  "))

tempoSegundos = arquivo / (velocidade / 8)
minutos = int(tempoSegundos / 60)
segundos = int(tempoSegundos % 60)

print(f"{minutos} minutos e {segundos} segundos")