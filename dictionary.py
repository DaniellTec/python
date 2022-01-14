#Definir datos mediante claves y valores
product = {

    "name" : "Something",
    "price" :  25.25,
    "quantity": 5


}

print(product)
print(type(product))
#print(dir(product))

print(product.keys()) #Muestra solo el valor de las {}
print(product.items()) #Muestra valor y contenido

product.clear()
print(product)

#Varios diccionarios en uno
product = [

    {"name": "cpu", "price":5.55},
    {"name": "gpu", "price":25.25}

]

print(product)