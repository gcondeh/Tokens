# Tokens
Pequeñas utilidades para contar tokens y cortar cadenas de texto

contar_tokens_tiktoken
Se cargan de Datos desde un csv en df_texto, y se eliminan las filas que no tienen datos en la columna "subtitulo".
Se definen las funciones:
* Función mayor_long: Encuentra el índice de la fila con el subtítulo de mayor longitud en la columna "subtitulo".
* Función num_tokens: Usa tiktoken para obtener el número de tokens en cada texto de textos.
Ejemplos de uso:
* Obtener la fila con subtítulo más Largo y su longitud.
* Se define un límite n (en este caso, 20), y se cuenta cuántos subtítulos tienen más de 20 tokens.

contar_tokens_spacy
Básicamente hace lo mismo que "contar_tokens_tiktoken", pero con spacy

separar_textos_en_parrafos
Se cargan de Datos desde un csv en df_texto, y divide el campo "subtitulo" en fragmentos de una logitud dada aumentando el número de filas del dataframe. Despues se guarda el resultado en un fichero.
Implementa dos métodos para separar los fragmentos. Por tokens, usando Tiktoken y por longitud del texto. 
