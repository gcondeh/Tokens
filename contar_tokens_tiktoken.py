# -*- coding: utf-8 -*-
"""


Contamos el número de tokens de un texto almacenado en una columna de un array que se carga a partir de un fichero cvs
Par contar los tokens usamos la librería de OpenAI tiktoken y la codificación para uno de sus modelos


"""

# Instalamos tiktoken si es necesario
# !pip install tiktoken

# Cargamos las librerías
import tiktoken
import pandas as pd


# cargamos el fichero de texto 
ruta_in = "./datos/"
f_entrada = "noticias.csv"
df_texto = pd.read_csv(ruta_in + f_entrada, sep = ";")
df_texto = df_texto.dropna(subset=["subtitulo"]) # Borramos las filas que no traen datos en el campo subtitulo
df_texto = df_texto.reset_index(drop=True) # Reconstruimos el indice

# Función para encontrar el índice del texto de mayor longitud en una columna específica
def mayor_long(texto): # obtenemos la fila que contiene el texto de mayor longitud.
    m = texto.str.len().idxmax()
    return(m)

# Función para contar el número de tokens en cada texto de una lista o un texto individual
def num_tokens(textos, codificacion):
    # Convertimos a lista si la entrada es un único string
    if isinstance(textos, str):
        textos = [textos]
        
    # Gestión del error al obtener la codificación si el modelo no es correcto
    try:
        encoding = tiktoken.encoding_for_model(codificacion) # Le inficamos a tiktoken cual es la codificaicón que usará.
    except Exception as e:
        raise ValueError(f"Nombre de codificación inválido '{codificacion}': {e}")
        
    num_tokens = []
    
    for noticia in textos:
        y = len(encoding.encode(noticia))
        num_tokens.append(y)
    return (num_tokens)


may=mayor_long(df_texto["subtitulo"])
# Mostramos el número de tokens en el subtítulo más largo
print("Noticia con mayor longitud: ", may)
print("Número de tokens de la mayor noticia: ", num_tokens(df_texto["subtitulo"][may], 'gpt-4o-mini'))

# Contamos cuántos subtítulos tienen más de `n` tokens
n=20
cantidad_mayores_que_n =sum(n > 10 for n in num_tokens(df_texto["subtitulo"], 'gpt-4o-mini'))
print(f"Noticias con mas de {n} tokens: {cantidad_mayores_que_n}")

