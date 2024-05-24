from gtts import gTTS
import os

def text_to_speech(text, lang='en', filename='output_test.mp3'):
    """
    Convierte el texto a un archivo de audio usando gTTS.

    :param text: El texto a convertir.
    :param lang: El idioma del texto (por defecto 'es' para español).
    :param filename: El nombre del archivo de salida (por defecto 'output.mp3').
    """
    # Crear el objeto gTTS con el texto y el idioma especificado
    tts = gTTS(text=text, lang=lang, slow=False)

    # Guardar el resultado en un archivo de audio
    tts.save(filename)

    print(f"Archivo de audio guardado como {filename}")

# Ejemplo de uso
texto = "Now, turn right carefully"
text_to_speech(texto)
