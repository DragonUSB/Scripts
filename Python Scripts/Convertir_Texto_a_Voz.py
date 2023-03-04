# Importamos el paquete
from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
# Texto a convertir en audio
mytext = "Hola, saludos desde Merida, Venezuela"

# Realizamos la conversión del texto a voz
tts = gTTS(text=mytext, lang='es', slow=False)

# Finalmente guardamos el archivo de Audio
tts.save("facialix.mp3")

# Load `mp3_fp` as an mp3 file in
# the audio library of your choice
tts.write_to_fp(mp3_fp)