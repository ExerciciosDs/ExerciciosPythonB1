nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 8:
	conceito = "A"
elif media >= 5 and media < 8:
	conceito = "B"
elif media < 5:
	conceito = "C"

print("A média final é de ",media,".")
print("O conceito é ",conceito,".")