nota = 0
contador = 0
total = 0

nota = int(input("Digite uma nota: "))
notaMaior = nota
notaMenor = nota

while nota != -1:
    
    contador +=1
    total += nota
    
    if nota > notaMaior:
        notaMaior = nota
        
    elif nota < notaMenor:
        notaMenor = nota
        
    nota = int(input("Digite uma nota: "))
    
    
if contador != 0:
    mediaFinal = total / contador

    print("A média é:", mediaFinal)
    print("A maior nota é:", notaMaior)
    print("A menor nota é:", notaMenor)
    
else:
    print("Nenhuma nota foi recebida.")