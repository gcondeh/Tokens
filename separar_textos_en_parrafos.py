# -*- coding: utf-8 -*-
"""
Script para dividir textos en fragmentos basados en caracteres o tokens.
Requisitos:
- Archivo de entrada: CSV con columnas 'titulo' y 'subtitulo'.
- Salida: Un archivo CSV con los textos divididos en fragmentos.

Configuraciones:
- chunk_size: Tamaño del fragmento.
- chunk_overlap: Superposición de los fragmentos.


Se usa langchain para los cortes, modificando ligeramente los criterios:

\n\n. salto de parrafo.
\n. Salto de línea.
. Punto seguido
" " Espacios
"" Cualquier cosa

"""
# Inslatamos los paquetes necesarios
# ! pip install langchain_text_splitters tiktoken

# Cargamos librerías
import pandas as pd
import tiktoken
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Carga de datos
ruta_in = "./datos/"
f_entrada = "noticias.csv"
df_texto = pd.read_csv(ruta_in + f_entrada, sep = ";")
df_texto = df_texto.dropna(subset=["subtitulo"]) # Borramos las filas que no traen datos en el campo subtitulo
df_texto = df_texto.reset_index(drop=True) # Reconstruimos el indice

# Obtenemos la codificación del modelo que usaremos con Tiktoken
encoding = tiktoken.encoding_for_model('gpt-4o-mini') 


# Función para contar tokens que se usará en el text_splitter
def contar_tokens(texto):
    tokens = encoding.encode(texto)
    return len(tokens)


# Recortar textos por número de tokens
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,  # Tamaño de cada fragmento en tokens
    chunk_overlap=5,  # Superposición entre fragmentos en tokens, para mantener contexto
    length_function=contar_tokens,  # Utilizamos la función de conteo de tokens definida arriba
    is_separator_regex=False,
    separators=["\n\n","\n","."," ",""],
    keep_separator=False
)

"""
# Recortar textos por longitud del texto
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False,
    separators=["\n\n","\n","","."," ",""],
    keep_separator=False
)
"""

# Bucle con la separación de los fragmentos
temp = pd.DataFrame(columns=["doc_id", "sent_id", "titulo","fragmento"])
h=0
for i,fila in df_texto.iterrows():
   splitted_texts = text_splitter.split_text(fila["subtitulo"])
   for txt in splitted_texts:
        temp.loc[h]= [ i, h, fila["titulo"], txt]
        h=h+1

ruta_salida = "./datos/"
f_salida = 'noticias_x_frases.csv'
temp.to_csv(ruta_salida + f_salida, index=False, sep=";")