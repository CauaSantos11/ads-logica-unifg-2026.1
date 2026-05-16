### 🔐 Exercício 4: Verificador de Acesso (Lógica e Relacionais)
#Desenvolva um sistema de verificação que solicite a **idade** e os **anos de experiência** do usuário.

#**Regra Importante:** Não utilize `if/else`. O programa deve imprimir apenas `True` ou `False` para a condição de acesso.

#*Regra Lógica:**
#$$Acesso = (Idade \geq 18) \text{ AND } (Experiencia > 2)$$

#**Saída esperada:** "Acesso Liberado: True".

idade = int(input("Digite sua idade:"))
tempoTrabalho = int (input("Digite seu tempo de experciencia:"))

acesso = (idade >= 18 and tempoTrabalho > 2)

print (acesso)