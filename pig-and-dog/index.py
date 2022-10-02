from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


#Criando animais:
# Inicializando lista de porcos, onde o número 1 representa true e 0 false
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]
# Inicializando lista de cachorro, onde o número 1 representa true e 0 false
cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# Criando base de dados dos animais:

treina_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# Criando base de classificação dos animais [1 - PORCO e 0 - CACHORRO]:

treina_y = [1, 1, 1, 0, 0, 0]

# Instanciamento
model = LinearSVC()

# Entro com os dados que desejo ensinar e a classificação desses dados:
model.fit(treina_x, treina_y)

# Criando um animal qualquer:
animal = [1, 1, 1]

model.predict([animal])

animal1 = [1, 1, 1]
animal2 = [1, 1, 0]
animal3 = [0, 1, 1]

teste_x = [animal1, animal2, animal3]
teste_y = [0, 1, 1]

previsoes = model.predict(teste_x)
previsoes

previsoes == teste_y

# Imputando a soma de acertos corretos numa variavel:
corretos = (previsoes == teste_y).sum()                         # Faz a soma de todos itens corretos da comparação previsoes == testesClasses e guarda na variavel corretos;
total = len(teste_y)                                            # Faz a soma de todos itens testados (a função len soma quantidade de itens), no caso animaisTestes;
taxaAcerto = corretos/total                                     # Calcula a taxa (relação) entre itens corretos e total
print (f"Taxa de acerto: {taxaAcerto * 100}")                   # Apresenta (imprime) a taxa de Acertos em porcentagem (por isso a multiplicação por 100)


acerto = accuracy_score(teste_y, previsoes)
print(acerto)