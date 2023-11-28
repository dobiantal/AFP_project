def multiplicate(OPERANDUS_A, OPERANDUS_B):
    if OPERANDUS_B or OPERANDUS_A == 0:
        raise ValueError("Az OPERANDUS_B vagy OPERANDUS_A értéke nem lehet 0.")
    return OPERANDUS_A * OPERANDUS_B