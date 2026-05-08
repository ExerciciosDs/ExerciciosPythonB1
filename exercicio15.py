def maiorIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

idade = int(input("Digite a idade: "))

print(maiorIdade(idade))
