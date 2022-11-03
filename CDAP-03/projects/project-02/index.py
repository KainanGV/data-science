import pandas as pd

url = "https://raw.githubusercontent.com/profviniciusheltai/Aula_IA/main/Projeto02.csv"

dados = pd.read_csv(url)

mapa = {
  "home": "principal",
  "how_it_works": "como_funciona",
  "contact": "contato",
  "bought": "comprou",
}

dados = dados.rename(columns= mapa)

x = dados[["principal", "como_funciona", "contato"]]
y = dados["comprou"]

treino_x = x[:70]
treino_y = y[:70]

teste_x = x[70:]
teste_y = y[70:]

from sklearn.svm import LinearSVC

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)

previsoes = modelo.predict(teste_x)

from sklearn.metrics import accuracy_score

acuracia = accuracy_score(teste_y, previsoes)

print(f"A acuracia: {acuracia*100:.2f}%")


