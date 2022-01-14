#Lo define como una función
def hello(name="person"): ##Si no hay nada
    print("hi, " + name)##Encapsula
#No se ejecuta hasta que es llame a la función
hello("bitch")
hello()

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 40)) #Se suman los valores
print(add(400, 100)) #Se anadem los valores

add = lambda numberOne,numberTwo: numberOne + numberTwo #Función anónima, establece un resultado
print(add(10,50))