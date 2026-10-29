class Calculadora:
    def sumar(self, operando_1, operando_2):
        return operando_1 + operando_2

    def restar(self, operando_1, operando_2):
        return operando_1 - operando_2

    def multiplicar(self, operando_1, operando_2):
        return operando_1 * operando_2

    def dividir(self, operando_1, operando_2):
        try:
            return operando_1 / operando_2
        except ZeroDivisionError:
            return "ERROR: División por cero"

    def modulo(self, operando_1, operando_2):
        return operando_1 % operando_2