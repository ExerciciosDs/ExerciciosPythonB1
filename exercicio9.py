altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
	print("IMC: ",imc,". Classificação: Abaixo do peso normal")

elif imc >= 18.5 and imc < 24.9:
	print("IMC: ",imc,". Classificação: Peso normal")

elif imc >= 25 and imc < 29.9:
	print("IMC: ",imc,". Classificação: Excesso de peso")

elif imc >= 30 and imc < 34.9:
	print("IMC: ",imc,". Classificação: Obesidade classe 1")

elif imc >= 35 and imc < 39.9:
	print("IMC: ",imc,". Classificação: Obesidade classe 2")

elif imc >= 40:
	print("IMC: ",imc,". Classificação: Obesidade classe 3")
