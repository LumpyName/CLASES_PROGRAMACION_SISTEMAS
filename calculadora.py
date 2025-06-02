from dividir import divicion, divicionentera, divicionresto
from multiplicar import multiplicando
from sumar import sumando
from restar import restando

a = int(input("Ingrese un numero  : "))
b = int(input("Ingrese otro numero: "))

print()

print("OPERACIONES CON LA DIVISION")
print(f"La division es              : {a} / {b} = {round(divicion(a, b), 3)}")

print(f"El residuo de la division es: {divicionresto(a, b)}")

print(f"La division entera es       : {divicionentera(a, b)}")

print()

print("OPERACION CON LA SUMATORIA")
print(f"La multiplicacion {a} + {b} = {sumando(a, b)}")

print()

print("OPERACION CON LA RESTAR")
print(f"La multiplicacion {a} - {b} = {restando(a, b)}")

print()

print("OPERACION CON LA MULTIPLICACION")
print(f"La multiplicacion {a} x {b} = {multiplicando(a, b)}")
