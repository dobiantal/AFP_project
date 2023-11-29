from decimal import Decimal,getcontext,InvalidOperation

class Subtraction():

    def __init__(self,expression):
        self.expression = expression
        self.result = None

    global1 = ""
    global2 = ""

    @staticmethod
    def subtract(expression):
        numbers = [Decimal(num) for num in expression.split('-') if num]
        result = numbers[0] if numbers else Decimal(0)

        for num in numbers[1:]:
            result -= num

        Subtraction.global1 = expression
        Subtraction.global2 = format(result, '.8f')

        return format(result, '.8f')

    def calculate(self):
        getcontext().prec = 8  # Beállítottam a tizedesjegy pontosságot

        if '-' in self.expression:
            try:
                self.result = Subtraction.subtract(self.expression)
            except (ValueError, SyntaxError, InvalidOperation) as e:
                return str(e)  # Visszatérés hibaüzenettel
        else:
            return "Hiba!"


