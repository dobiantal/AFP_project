def div(OPERANDUS_A , OPERANDUS_B):
    try:
        return int(OPERANDUS_A) / int(OPERANDUS_B)
    except ValueError:
        return "Hibás érték!"
    except SyntaxError:
        return "Szintaktikai hiba!"
    except ZeroDivisionError:
        return "0-val való osztás 0-t ad!"



print(div(40, 10))
