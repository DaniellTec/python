#import datetime #Se importa un módulo
from datetime import timedelta,date
#import fmath #Importamos el módulo creado
from fmath import add, susbstract

from colorama import Fore, Style

#print(datetime.date.today()) #Muestra la fecha de hoy
print(timedelta(minutes=70)) #Minutos a horas
print(date.today())#Muestra el día


#fmath.add(1, 2)
#fmath.susbstract(1, 2)
add(1, 2)
susbstract(1, 2)