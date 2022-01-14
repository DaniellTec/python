import csv


def pedir(color):
    f = ('azul')

    j = ('amarilla')

    if f == color:

        print(color + ' esta en la f')

    elif j == color:

        print(color + ' esta en la j')

    else:

        print("no tenemos ese color")

    return


print("¿Que color quieres entre estos azul,amarilla?")

color = input()

pedir(color)

myData = [[color, color, color]] #Los datos escriben

myFile = open('practica2.csv', 'w') #Se pasan a un archi editable

with myFile:
    writer = csv.writer(myFile) #Se crea el archivo

    writer.writerows(myData) #Se pasan los datos al archivo

print("Writing complete")