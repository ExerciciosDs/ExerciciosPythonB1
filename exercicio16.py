def totalPagar(valor, quantidade):
    return valor * quantidade

produto = float(input("Digite o valor da unidade do produto: "))
quantidade = int(input("Digite a quantidade de produtos comprados: "))

print("Total a se pagar: R$", totalPagar(produto, quantidade))
