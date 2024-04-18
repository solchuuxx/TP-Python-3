import pandas as pd
import csv

lista_edades = [] 

#Obtiene los datos de las edades del archivo "edades-30Alumnos.csv"
with open('edades-30Alumnos.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',', quotechar='"')
    for fila in lector_csv:
        lista_edades.append(fila[1])

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