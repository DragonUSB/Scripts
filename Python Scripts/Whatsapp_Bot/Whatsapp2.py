# Importamos el ModuMódulo

import pywhatkit 

# Usamos Un try-except
try: 

  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+584161156701", "Mensaje De Prueba%0AMensaje De Prueba", 9, 24) 
  print("Mensaje Enviado") 

except: 
  print("Ocurrio Un Error")