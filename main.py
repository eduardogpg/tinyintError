from tinyint import tiny_int

def call_back_function(val):
  message = "Esta funcion se ejecuta cuando el número {} no es tinyint!".format(val)
  print(message)    

val = 600
tiny_int(val)
