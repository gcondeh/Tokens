# Tokens
Peque�as utilidades para contar tokens y cortar cadenas de texto

contar_tokens_tiktoken
Se cargan de Datos desde un csv en df_texto, y se eliminan las filas que no tienen datos en la columna "subtitulo".
Se definen las funciones:
* Funci�n mayor_long: Encuentra el �ndice de la fila con el subt�tulo de mayor longitud en la columna "subtitulo".
* Funci�n num_tokens: Usa tiktoken para obtener el n�mero de tokens en cada texto de textos.
Ejemplos de uso:
* Obtener la fila con subt�tulo m�s Largo y su longitud.
* Se define un l�mite n (en este caso, 20), y se cuenta cu�ntos subt�tulos tienen m�s de 20 tokens.

contar_tokens_spacy
B�sicamente hace lo mismo que "contar_tokens_tiktoken", pero con spacy

separar_textos_en_parrafos
Se cargan de Datos desde un csv en df_texto, y divide el campo "subtitulo" en fragmentos de una logitud dada aumentando el n�mero de filas del dataframe. Despues se guarda el resultado en un fichero.
Implementa dos m�todos para separar los fragmentos. Por tokens, usando Tiktoken y por longitud del texto. 
