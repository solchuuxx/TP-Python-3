import pandas as pd

lista_edades = [19, 19, 18, 27, 24, 28, 30, 40, 44, 38, 37, 25, 25, 31, 32, 24, 29, 29, 29, 19, 19, 18, 20, 21, 21, 19, 19, 19, 18, 23] 

#Conversión de lista a dataframe y creación de la columna 'Edades'
df = pd.DataFrame(lista_edades, columns=['Edades'])

def analisis_estadistico(df):
    #verifica si df es una lista
    if not isinstance(df, pd.DataFrame):
        print("Error: El argumento no es un DataFrame.")
        return None
    #Calcula la frecuencia absoluta fi
    df['fi'] = df.groupby('Edades')['Edades'].transform('count')
    #Elimina las edades duplicadas de la columna "Edades"
    df = df.drop_duplicates()
    #calcula la frecuencia acumulada Fi
    df["Fi"] = df['fi'].cumsum()
    #calcula la frecuencia relativa ri
    df["ri"] = df["fi"] / df["fi"].sum()
    #calcula la frecuencia relativa acumulada Ri
    df["Ri"] = df['ri'].cumsum()
    #calcula la frecuencia porcentual simple pi%
    df['pi%'] = df['ri'] * 100
    #calcula la frecuencia porcentual acumulada Pi%
    df['Pi%'] = df['Ri'] * 100
    
    return df

df_resultado = analisis_estadistico(df)
print(df_resultado.head(30))