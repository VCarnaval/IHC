locations = [['END.: AVENIDA JOSE RIBEIRO BASTOS\n', 'TOTAL DE ACIDENTES: 3\n', 'ACIDENTES FATAIS: 1', -23.278744, -45.897818],
['END.: PONTE MARIA PEREGRINA\n', 'TOTAL DE ACIDENTES: 3\n', 'ACIDENTES FATAIS: 1', -23.162320, -45.903029],
['END.: AVENIDA ANCHIETA\n', 'TOTAL DE ACIDENTES: 3\n', 'ACIDENTES FATAIS: 0', -23.192699, -45.899224],
['END.: AVENIDA ANTONIO JOAQUIM DE ALVARENGA FILHO\n', 'TOTAL DE ACIDENTES: 3\n', 'ACIDENTES FATAIS: 0', -23.276387, -45.891704],
['END.: AVENIDA JOAO BASSI\n', 'TOTAL DE ACIDENTES: 2\n', 'ACIDENTES FATAIS: 0', -23.183696, -45.790403],
['END.: AVENIDA JOSE PEDRO\n', 'TOTAL DE ACIDENTES: 2\n', 'ACIDENTES FATAIS: 0', -23.169630, -45.813794],
['END.: AVENIDA LIVIO VENEZIANI\n', 'TOTAL DE ACIDENTES: 2\n', 'ACIDENTES FATAIS: 0', -23.210073, -45.850332],
['END.: AVENIDA MARIO FRIGI\n', 'TOTAL DE ACIDENTES: 2\n', 'ACIDENTES FATAIS: 0', -23.256938, -45.897262],
['END.: AVENIDA PAPA JOAO PAULO II\n', 'TOTAL DE ACIDENTES: 2\n', 'ACIDENTES FATAIS: 0', -23.202731, -45.951391],
['END.: AVENIDA RIO BUQUIRA\n', 'TOTAL DE ACIDENTES: 2\n', 'ACIDENTES FATAIS: 0', -23.143234, -45.916470],
['END.: RUA DAS GLICINIAS\n', 'TOTAL DE ACIDENTES: 1\n', 'ACIDENTES FATAIS: 0', -23.174404, -45.825482]] #vetor de dados
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