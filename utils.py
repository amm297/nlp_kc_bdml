import re
from num2words import num2words

# Funcion que convierte de un arvchivo txt a un dict
def file_to_dict(file_name):
    d = None
    with open(file_name) as f:
        d = dict(x.rstrip().split(None, 1) for x in f)
    return d


# Funcion para procesar el texto
def process_text(min_length=50, lemas_dict={},translate_table={}, stop_words=[], lang='en', stemmer=None, review=None):
    if not review or len(review) < min_length:
        return None
    
    #Sustituimos si hay algun caracter &#DD
    review = re.sub(r'(&#\d+) | (&\w+)', '', review)
    
    words = []
    # Pocessamos nuestra review valida
    for word in re.split(r'[;,.\'\s]\s*', review):
        # lematizamos
        word = lemas_dict.get(word) or word
        # stemmer
        word = stemmer.stem(word) if stemmer else word
        # Quitamos los signos de puntuacion
        word = word.translate(translate_table)
        # Comprobamos que tenga algun valor
        # Comprobamos que tenga una longitud minima de 3 caracteres
        # Comprobamos que no sea un stopword
        if word and len(word) > 3 and word not in stop_words:
            # Comprobamos si es un numero y lo sutituimos si tenemos el idioma
            if lang and word.isdigit() :
                word = num2words(word, lang=lang, ordinal=False)
            # Añadimos a la lista
            # La pasamos a minuscula
            words.append(word.lower())

    return words