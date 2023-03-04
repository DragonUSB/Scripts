# Importamos el ModuMódulo

import pywhatkit 

# Usamos Un try-except
try: 

  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+584247585681", "Mensaje De Prueba%0AMensaje De Prueba", 21,05) 
  print("Mensaje Enviado") 

except: 
  print("Ocurrio Un Error")