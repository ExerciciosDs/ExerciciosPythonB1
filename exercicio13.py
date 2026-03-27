nome = input("Digite o nome do novo usuário: ")
qtd = 0
qtdMaior = 0

while nome != "encerrar":
    idade = int(input("Digite a idade do novo usuário: "))
    
    if idade >= 18:
        qtdMaior += 1
    
    qtd += 1
    
    nome = input("Digite o nome do novo usuário: ")
    
print(qtd, "usuários foram cadastrados")
print(qtdMaior, "desses usuários são maiores de idade.")