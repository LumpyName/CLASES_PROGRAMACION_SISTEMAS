from SEMESTRE_1_TERCER_PARCIAL.lib import adultos_bbdd
from SEMESTRE_1_TERCER_PARCIAL.lib import ninas_bbdd
from SEMESTRE_1_TERCER_PARCIAL.lib import ninos_bbdd

tabla_IMC = {
    1: adultos_bbdd.tabla_adultos,
    2: ninas_bbdd.tabla_nina,
    3: ninos_bbdd.tabla_ninos
}
salir = False # No funciono la funcion exit() para terminar el programa y por eso use esa variable

try:
    print("Seleccione tipo de persona:")
    print("1. Adulto")
    print("2. Niña")
    print("3. Niño")
    opcion = abs(int(input("Opcion: "))) # Uso abs() para que siempre sea positivo

    if opcion > 3:
        raise IndexError("Solo existen esas 3 opciones...")

    peso = int(input("\nIngrese el peso en kg: "))
    metros = float(input("Ingrese la estatura en metros: "))

except ValueError as error:
    print(f"\nSe escribio un dato de manera incorrecta...")
    print("Saliendo del programa")
    salir = True 
except IndexError as err:
    print(f"\n{err}")
    print("Saliendo del programa")
    salir = True

if not salir:
    imc = round(peso / (metros)**2, 2)
    clasificacion = None

    for clasificacion_IMC, confirmacion in tabla_IMC[opcion].items():
        if confirmacion(imc):
            clasificacion = clasificacion_IMC
            break

    print("\nResultado del cálculo: \n")

    print(f"IMC calculado: {imc}")
    print(f"Clasificacion: {clasificacion}")

print()