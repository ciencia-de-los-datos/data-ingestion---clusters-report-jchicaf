"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #

    import pandas as pd
    # Leer archivo txt
    listAnchoCols = [9, 16, 16, 77]
    df = pd.read_fwf('clusters_report.txt', widths=listAnchoCols,  header=None, skiprows=[2,3])
    df.fillna('', inplace=True)
    df = df.drop(labels = 0,axis = 1).astype(str).groupby(df[0].mask(df[0]=='').ffill()).agg(' '.join).reset_index()
    df.columns = df.loc[13]
    df.drop(13, axis=0, inplace= True)

    # Columnas en minúscula
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    #Tipos de datos
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['cluster'] = df['cluster'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].apply(lambda x: float(x.replace('%', '').replace(',', '.').strip()))

    # palabras clave
    df['principales_palabras_clave'] = df.principales_palabras_clave.apply(lambda x: ' '.join(x.split()))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.', '')

    # Ordenar
    df.sort_values(by='cluster', inplace=True)
    df.reset_index(drop=True, inplace=True)

    #print(df)

    # with open('clusters_report.txt') as f:
    #     contents = f.readlines()

    # for line in contents:
    #     print(line)
    
    return df
