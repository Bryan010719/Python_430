
### Operadores aritmeticos ###
#Operadores con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 +3 - 7 / 1 // 4)

#Operaciones con cadenas de texto
print("hola " + "python " + "que tal?")
print ("hola " + str(5))

#Operaciones mixtas
print("hola " * 5)
print("hola " * (2 ** 3))
my_float = 2.5 * 2
print("hola " * int(my_float))

### Operadores comparativos ###


# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") #Ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) #cuenta caracteres
print("aaaa" <= "abaa")
print("aaaa" == "abaa")
print("aaaa" != "abaa")


### Operadores logicos ###

#Basada en el Algebra de Boole https://es.wikipedia.org/wiki/%C3%811gebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 > 4 and "Hola" < "Python")
print(3 > 4 or "Hola" < "Python")
print(3 > 4 and ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))



