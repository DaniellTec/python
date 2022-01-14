foods = ['apples', 'bread','cheese','milk']

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print("\n")
#Recorre todos los elementos 
for food in foods:
    if food == "cheese":
        break
    print(food)

for number in range (1, 6):
    print(number)    
 
for text in "Text":
    print(text) 

count = 5

#Mientras se cumpla la condición se repite el bucle
while count <=10:
    print(count)
    count = count +1
