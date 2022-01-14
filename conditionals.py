d = 25

if d <30: #Si es menor que 30 
    print("d Is less than 25")

c = 30

if c > 25: #Si es mayor que 25 
    print("c Is greater than 25")    

e = 25

if e == 25: #Si es igual que 25
    print("e Is equeal than 25")

color = "cyan"

if color == "blue": 
    print("The color is cyan")
else: 
    print("Any color")    


if color == "cyan": 
    print("The color is cyan")
elif color == "violet":
    print("The color is violet")    
else: 
    print("Any color")    

#Condición anidada, una condicional dentro de una condicional
name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "a":
        print("You are John Carter")
    else: 
        print("You are not John Carter")    
else:
    print("You are not John Carter") 


#Operador
if d > 2 and d <=10:
    print("D is greater than 2 and less than or equal to 10")
if d > 2 or x <= 20:
    print("D is greater than 2  or less or equeal to 20")
if (not(d == c)):
    print("d is not equeal y")    