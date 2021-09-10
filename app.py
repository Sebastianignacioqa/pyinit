#Variables
name = "Sebastian"
number = 10
price = 2.3 #float
boolean = True #True or False

diccionary = {
    "numberOfLegs": 4,
    "eyes": 2,
    "name": "Dorian"
}

numbers = (1,2,3,4,5,6,7) #tupla, no pueden cambiar, son inmutables
lista = [1,2,3,4,5,6,7]
None # es undefined, con N mayuscula

#Funciones
#def myfunc(): #Hay que indexar porque si no, no se esta dentro del bloque de codigo
  #  x = 5
  #  print(x)
# pass hace que no se ejecute el bloque de codigo
#myfunc()

#x = lambda a: print(a) #Funcion anonima
#x(10) #Aca estamos llamando a la funcion anonima

#Loops
#for number in lista: #como el map
  #  print (number* 2) 

counter = 0
while (counter <10):
    print(counter)
    counter = counter +1

#Manipulando listas
apellidos = ["Quezada", "Gonzalez", "Reyes"]
apellidos.append("Mendoza")
print(apellidos)
apellidos.remove("Reyes")
print(apellidos)



