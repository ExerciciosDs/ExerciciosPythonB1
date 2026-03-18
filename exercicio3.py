idVendedor = int(input("Digite o ID do vendedor: "))
idPeca = int(input("Digite o ID da peça: "))
precoPeca = float(input("Digite o valor unitário da peça: "))
qtdVendida = int(input("Digite quantos foram vendidos: "))

totalCompra = precoPeca * qtdVendida

print ("O vendedor cujo ID é ", idVendedor," vendeu ", qtdVendida," do produto ID ", idPeca,".")
print ("O valor total da compra foi ", totalCompra,". Logo, sua comissão foi de ", totalCompra * 0.05, ".")