# -*- coding: utf-8 -*-
"""


Contamos el número de tokens de un texto almacenado en una columna de un array que se carga a partir de un fichero cvs
Par contar los tokens usamos la librería de OpenAI tiktoken y la codificación para uno de sus modelos


"""

# Instalamos spacy si es necesario
# !pip install spacy
# spacy.cli.download("es_core_news_sm") #Descargamos el modelo en español

# Cargamos las librerías
import spacy
import pandas as pd


# cargamos el fichero de texto 
ruta_in = "./datos/"
f_entrada = "noticias.csv"
df_texto = pd.read_csv(ruta_in + f_entrada, sep = ";")
df_texto = df_texto.dropna(subset=["subtitulo"]) # Borramos las filas que no traen datos en el campo subtitulo
df_texto = df_texto.reset_index(drop=True) # Reconstruimos el indice
nlp = spacy.load(ruta_in+"../es_core_news_sm-3.8.0")  # Cargar el modelo para español desde una descarga en local

# Función para encontrar el índice del texto de mayor longitud en una columna específica
def mayor_long(texto): # obtenemos la fila que contiene el texto de mayor longitud.
    m = texto.str.len().idxmax()
    return(m)

# Función para contar el número de tokens en cada texto de una lista o un texto individual
# La salida es una lista que eventualmente se puede pegar al dataframe con los textos
def num_tokens(textos):
    # Convertimos a lista si la entrada es un único string
    if isinstance(textos, str):
        textos = [textos]
        
    num_tokens = []
    for noticia in textos:
        txt = nlp(noticia)
        tokens = [token.text for token in txt]
        num_tokens.append(len(tokens))
    return (num_tokens)


may=mayor_long(df_texto["subtitulo"])
# Mostramos el número de tokens en el subtítulo más largo
print("Noticia con mayor longitud: ", may)
print("Número de tokens de la mayor noticia: ", num_tokens(df_texto["subtitulo"][may]))

# Contamos cuántos subtítulos tienen más de `n` tokens
n=20
cantidad_mayores_que_n =sum(n > 10 for n in num_tokens(df_texto["subtitulo"]))
print(f"Noticias con mas de {n} tokens: {cantidad_mayores_que_n}")

