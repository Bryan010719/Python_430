### Classes ###
# Definicion
class MyEmptyPerson:
    pass # para poder dejar la clase vacia


print(MyEmptyPerson)
print(MyEmptyPerson())

# clase con constructor, funciones y propiedades privadas y publicas


class person:
    def __init__(self, name, surname, alias="sin alias"):
        self.full_name = f"{name}{surname}({alias})" # propiedad publica
        self.__name = name #propiedad privada
    def get_name(self):
        return self.__name


    def walk(self):
         print(f"{self.full_name} esta caminando")


my_person = person("Bryan ","Lucatero")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = person("Bryan ","Lucatero","Chato")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon"
print(my_other_person.full_name)

my_other_person.full_name= 666
print(my_other_person.full_name)


