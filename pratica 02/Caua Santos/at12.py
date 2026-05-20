## 🛒 Exercício 12: Registro de Compras (Interatividade)

#Solicite o valor de várias compras. 
#Após cada entrada, pergunte: "Deseja #continuar? (S/N)". 
# O programa encerra quando o usuário decidir parar.

continuar = "S"

while continuar == "S":
    compra = float(input("Digite o valor da compra: R$ "))
    
    print(f"Compra registrada: R$ {compra}")

    continuar = input("Deseja continuar? (S/N): ").upper()

print("Programa encerrado.")