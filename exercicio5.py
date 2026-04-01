nome = input("Digite o nome do jogador: ")
salarioA = float(input("Digite seu salário atual: "))
salarioN = 0.00
if salarioA >= 0.00 and salarioA <= 1000.00:
    salarioN = salarioA * 1.20
elif salarioA >= 1000.01 and salarioA <= 5000.00:
    salarioN = salarioA * 1.10
elif salarioA > 5000.01:
    salarioN = salarioA * 1.05
     
print("Seu novo salário é: ", salarioN)