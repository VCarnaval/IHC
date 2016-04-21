locations = [] #vetor de dados
x = 0 #índice

print("[") #Iniciando o vetor de dados

while x < len(locations): #Loop para percorrer o vetor
    print("{") #Printando uma chave para iniciar o objeto
    print('"end": "',locations[x][0],'",') #Criando a variável "end" para o myJson
    print('"total_acidentes": ',locations[x][1][20:],",") #Criando a variável "total_acidentes" para o myJson
    print('"acidentes_fatais": ',locations[x][2][18:],",") #Criando a variável "acidentes_fatais" para o myJson
    print('"lat": ',locations[x][3],",") #Criando a variável "lat" para o myJson
    print('"long": ',locations[x][4]) #Criando a variável "long" para o myJson
    if x == ((len(locations)) - 1): #Verificando se estamos tratando do último objeto do vetor
    	print("}\n") #Fechando o último objeto do vetor, pois o mesmo não pode possuir vírgula após a chave
    else:
    	print("},\n") #Fechando o objeto do vetor
    x += 1

print("]") #Fechando o vetor