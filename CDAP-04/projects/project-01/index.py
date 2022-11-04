import pandas as pd 

url = "https://raw.githubusercontent.com/profviniciusheltai/Aula_IA/main/Projeto03.csv"

dados = pd.read_csv(url)

a_rename = {
  "expected_hours": "horas_esperadas",
  "price": "preco",
  "unfinished": "nao_finalizado",
}

dados = dados.rename(columns = a_rename)

troca = {
  0: 1,
  1: 0
}

dados["finalizado"] = dados.nao_finalizado.map(troca)

import seaborn as sns

print(sns.scatterplot(x = "horas_esperadas", y = "preco", data = dados))

