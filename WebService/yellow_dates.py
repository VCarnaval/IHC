locations = [['END.: RUA CANDEIAS\n', 'TOTAL DE ACIDENTES: 9\n', 'ACIDENTES FATAIS: 1', -23.254118, -45.909641],
['END.: AVENIDA BENEDITO BENTO\n', 'TOTAL DE ACIDENTES: 9\n', 'ACIDENTES FATAIS: 0', -23.250881, -45.904255],
['END.: AVENIDA OLIVO GOMES\n', 'TOTAL DE ACIDENTES: 9\n', 'ACIDENTES FATAIS: 0', -23.169223, -45.891467],
['END.: RUA GISELE MARTINS\n', 'TOTAL DE ACIDENTES: 9\n', 'ACIDENTES FATAIS: 0', -23.254796, -45.898539],
['END.: RUA MAR DEL PLATA\n', 'TOTAL DE ACIDENTES: 8\n', 'ACIDENTES FATAIS: 1', -23.234773, -45.899025],
['END.: RUA MONTE AZUL\n', 'TOTAL DE ACIDENTES: 8\n', 'ACIDENTES FATAIS: 1', -23.250649, -45.925704],
['END.: AVENIDA ADILSON JOSE DA CRUZ\n', 'TOTAL DE ACIDENTES: 8\n', 'ACIDENTES FATAIS: 0', -23.274694, -45.887358],
['END.: AVENIDA DAS ROSAS\n', 'TOTAL DE ACIDENTES: 8\n', 'ACIDENTES FATAIS: 0', -23.175414, -45.825285],
['END.: ESTRADA DO JAGUARI\n', 'TOTAL DE ACIDENTES: 8\n', 'ACIDENTES FATAIS: 0', -23.156782, -45.905309],
['END.: RUA MOXOTO\n', 'TOTAL DE ACIDENTES: 8\n', 'ACIDENTES FATAIS: 0', -23.251785, -45.925024],
['END.: RUA VILACA\n', 'TOTAL DE ACIDENTES: 8\n', 'ACIDENTES FATAIS: 0', -23.183427, -45.884270],
['END.: AVENIDA LEONOR DE ALMEIDA RIBEIRO SOUTO\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 1', -23.266458, -45.909756],
['END.: AVENIDA PEDRO ALVARES CABRAL\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 1', -23.188527, -45.874303],
['END.: AVENIDA DOUTOR EDUARDO CURY\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 0', -23.201817, -45.910251],
['END.: AVENIDA MARECHAL HENRIQUE TEIXEIRA LOTT\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 0', -23.207884, -45.886597],
['END.: AVENIDA MARIA DE LOURDES MEDEIROS ASSIS\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 0', -23.272686, -45.889977],
['END.: ESTRADA NELSON TAVARES DA SILVA\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 0', -23.198697, -45.781028],
['END.: RUA CARLOS NUNES DE PAULA\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 0', -23.280611, -45.895835],
['END.: RUA GENESIA BERARDINELI TARANTINO\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 0', -23.191970, -45.876206],
['END.: RUA JOSE COBRA\n', 'TOTAL DE ACIDENTES: 7\n', 'ACIDENTES FATAIS: 0', -23.245916, -45.914442],
['END.: AVENIDA GUADALUPE\n', 'TOTAL DE ACIDENTES: 6\n', 'ACIDENTES FATAIS: 1', -23.231869, -45.897670]] #vetor de dados
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