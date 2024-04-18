import pandas as pd

lista_edades = [18, 19, 21, 22, 21, 19, 30, 44, 35, 23, 27, 28, 26, 26, 19, 19, 19, 20, 20, 27, 25, 25, 18, 18, 37, 40, 20, 20, 19, 29]

df = pd.DataFrame(lista_edades, columns=['Edades'])

def analisis_estadistico(df):
    df = df['Edades'].value_counts().reset_index().sort_values('index').reset_index(drop=True)
    df.columns = ['Edades', 'fi']
    df["Fi"] = df['fi'].cumsum()
    df["ri"] = df["fi"] / df["fi"].sum()
    df["Ri"] = df['ri'].cumsum()
    df['pi%'] = df['ri'] * 100
    df['Pi%'] = df['Ri'] * 100
    print(df.head(30))

analisis_estadistico(lista_edades)