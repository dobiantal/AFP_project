def multiplicate(OPERANDUS_A, OPERANDUS_B):
    if not (str(OPERANDUS_A).isnumeric() and str(OPERANDUS_B).isnumeric()):
        raise ValueError("Az OPERANDUS_A és OPERANDUS_B értékei csak számok lehetnek.")

    OPERANDUS_A = float(OPERANDUS_A)
    OPERANDUS_B = float(OPERANDUS_B)

    if OPERANDUS_A == 0 or OPERANDUS_B == 0:
        raise ValueError("Az OPERANDUS_A vagy OPERANDUS_B értéke nem lehet 0.")

    return OPERANDUS_A * OPERANDUS_B