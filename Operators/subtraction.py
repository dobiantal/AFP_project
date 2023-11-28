class Subtraction:
    global1 = ""
    global2 = ""
 
    @staticmethod
    def subtract(expression):
        numbers = [Decimal(num) for num in expression.split('-') if num]
        result = numbers[0] if numbers else Decimal(0)

        for num in numbers[1:]:
            result = operator.sub(result, num)

        Subtraction.global1 = expression
        Subtraction.global2 = format(result, '.8f')

        return format(result, '.8f')


    def calculate(self):
        getcontext().prec = 8  # Beállítottam a tizedesjegy pontosságot

        try:
            if '-' in self.expression:
                self.result = Subtraction.subtract(self.expression)
            else:
                raise ValueError("Érvénytelen kivonási kifejezés!")
        except (ValueError, SyntaxError, InvalidOperation):
            raise ValueError("Érvénytelen kifejezés!")
