import math

def negyzetgyok(OPERANDUS_A):

    """
    if (type(OPERANDUS_A) == str):
        return 0
    """

    try:
        OPERANDUS_A = float(OPERANDUS_A)
        # Ha negatív számot kap 0 val tér vissza
        if (OPERANDUS_A < 0):
            return 0

        return math.sqrt(OPERANDUS_A)
    except TypeError:
        return "TERR"
    except:
        return "ERR"




   #return math.sqrt(OPERANDUS_A)



