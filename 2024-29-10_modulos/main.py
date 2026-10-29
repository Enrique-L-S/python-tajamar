# Crear un par de módulos (los que veáis necesarios, pero no deberían ser mas de 5)
 
# para hacer un programa que me permita hacer cálculos en una calculadora
# debería tener al menos dos módulos (aunque podéis tener mas), uno para la lógica de calculo y otro para mostrar el menú de la calculadora

from calculadora import Calculadora

calc = Calculadora()

opciones = {
    1: calc.sumar,
    2: calc.restar,
    3: calc.multiplicar,
    4: calc.dividir,
    5: calc.modulo
}

print("CALCULADORA\n\n")
for ok, ov in opciones.items(): 
    print(f"{ok}.- {ov.__name__.capitalize()}")

opcion = int(input("Elige la operación: "))

print(f"Has elegido {opciones.get(opcion).__name__.capitalize()}")

op_1 = float(input("Elige el primer número: "))
op_2 = float(input("Elige el segundo número: "))

resultado = opciones[opcion](op_1, op_2)

print(f"El resultado es: {resultado}")