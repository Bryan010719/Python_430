### Variables ###

my_string_variable ="My string variable"

print(my_string_variable)
my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)


#concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

#Variables en una sola linea.¡cuidado con abusan de esta sintaxis!
name, surname, alias, age = "bryan", "lucatero", "Chato", 17
print("me llamo:", name, surname, "mi edad es:",
age, "y mi alias es: ", alias)

#inputs
name = input("cual es tu nombre? ")
age = input("cuantos años tienes? ")
print("tu nombre es:", name)
print("tienes",age,"años")

#cambiamos su tipo
name = 35
age = "carlos"
print(name)
print(age)

#forzamos el tipo
address: str = "mi direccion"
address = True
address = 5
address = 1.2
print(type(address))