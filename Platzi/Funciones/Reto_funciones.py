"""
Si recibes una computadora, debes retornar el mensaje: "Con mi computadora puedo programar usando Python".
Si recibes un celular, debes retornar el mensaje: "En mi celular puedo aprender usando la app de Platzi".
Si recibes un cable, debes retornar el mensaje: "¡Hay un cable en mi bota!".
Y si no recibes ninguno de estos valores, debes retornar el mensaje: "Artículo no encontrado".

"""


def message_creator(text):
   # Escribe tu solución 👇
   option = { "computadora" : "Con mi computadora puedo programar usando Python",
             "celular" :"En mi celular puedo aprender usando la app de Platzi",
             "cable": "¡Hay un cable en mi bota!",
             }
   if text in option.keys():
    print(option.keys())
    return option[text]
    
   else:
    print("Articulo no encontrado")
   

text = 'computadora'
response = message_creator(text)
print(response)


