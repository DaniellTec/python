list1 = [1, "Meh", True, 25.5, [1, 3, 5]]
colors = ['cyan', 'purple']
number_list = list((1, 3 ,5)) #Para que muestre una tabla
print (number_list)

r = list(range(5, 25)) # Muestra un rango de valores
print (r)
print(len(colors))
print("cyan" in colors)

#Alterar listas
print (colors)
colors[1] = 'yellow' #Sustituye el siguiente valor
colors.append('violet') #Añade elementos
print (colors)

colors.extend(["red", "blue"]) #Añade más de un elemento
print (colors)

colors.insert(-1, "black") #Inserta un valor en una posición
print (colors)

colors.insert(len(colors), "black") #Inserta un valor en la posición final
print (colors)

colors.pop() #Elimina el último valor


colors.remove("black") #Elimina valores
print(colors)

colors.sort(reverse=True) #Los ordena de forma inversa
print(colors)