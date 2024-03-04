### Exception handing ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Exception base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
else: #Opcional
    #Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:#opcional
    #Se ejecuta siempre
    print("La ejecucion continua")

#Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un Value Error")
except TypeError:
    print("Se ha producido un Type Error")

#Captura de la informacion  de la excepcion
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)

