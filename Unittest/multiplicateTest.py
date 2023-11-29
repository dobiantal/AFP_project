from Operators.multiplicate import multiplicate

def test_multiplicate_function():
    # Teszt 1: Pozitív számok szorzása
    result = multiplicate(2, 3)
    if result != 6:
        print("Hiba a pozitív számok szorzása tesztjében")

  # Teszt 2: Negatív és pozitív szám szorzása
    result = multiplicate(-2, 3)
    if result != -6:
        print("Hiba a negatív és pozitív szám szorzása tesztjében")

        # Teszt 3: Lebegőpontos számok szorzása
    result = multiplicate(2.5, 4)
    if result != 10.0:
        print("Hiba a lebegőpontos számok szorzása tesztjében")

 # Teszt 4: Nem szám bemenet
    try:
        result = multiplicate("a", 3)
        print("Hiba a nem szám bemenet tesztjében")
    except ValueError:
        pass  # Ez helyes, mert kivételt várok

# Teszt 5: Az egyik operandus 0
    try:
        result = multiplicate(0, 5)
        print("Hiba az egyik operandus 0 tesztjében")
    except ValueError:
        pass  # Ez helyes, mert kivételt várok

 # Teszt 6: Mindkét operandus 0
    try:
        result = multiplicate(0, 0)
        print("Hiba mindkét operandus 0 tesztjében")
    except ValueError:
        pass  # Ez helyes, mert kivételt várok

    test_multiplicate_function()