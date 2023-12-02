def Addition(A:int, B:int):
    try:
        if (float(A)+float(B)) % (float(A)+float(B)).__round__(0) == 0:
            return int(float(A)+float(B))
        else:
            return float(A)+float(B)
    except ValueError:
        return "Értékhiba"
    except TypeError:
        return "Helytelen típus"
    except:
        return "Err"
