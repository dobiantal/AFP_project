from decimal import Decimal, getcontext

def subtract(OPERANDUS_A, OPERANDUS_B):
    # Beállítja a kívánt pontosságot (8 tizedesjegy)
    getcontext().prec = 10

    try:
        eredmeny = Decimal(OPERANDUS_A) - Decimal(OPERANDUS_B)
        return round(eredmeny, 8)
    except Exception as e:
        print("Hiba történt a kivonás során:", e)
        return None  # Jelzés hogy a művelet nem sikerült

