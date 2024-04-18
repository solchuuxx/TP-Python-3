import pandas as pd
import csv

lista_edades = [] 

with open('edades-30Alumnos.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',', quotechar='"')
    for fila in lector_csv:
        lista_edades.append(fila[1])  # Asume que la edad está en la segunda columna

df = pd.DataFrame(lista_edades, columns=['Edades'])

def analisis_estadistico(df):
    # Calcula la frecuencia absoluta simple
    df['fi'] = df.groupby('Edades')['Edades'].transform('count')

    # Calcula la frecuencia relativa
    df['ri'] = df['fi'] / df['fi'].sum()

    # Calcula la frecuencia acumulada
    df['Fi'] = df['fi'].cumsum()

    # Calcula la frecuencia relativa y acumulada en porcentaje
    df['pi%'] = df['ri'] * 100
    df['Pi%'] = df['Fi'] / df['fi'].sum() * 100

    return df

df_resultado = analisis_estadistico(df)
print(df_resultado.head(30))
