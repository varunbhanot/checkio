def checkio(data):
    # Checking rows
    i = 0
    while i < 3:
        line = data[i]
        if (line == "XXX"): return "X"
        if (line == "OOO"): return "O"
        i += 1

    # Checking collumns
    j = 0
    while j < 3:
        column = data[0][j] + data[1][j] + data[2][j]
        if (column == "XXX"): return "X"
        if (column == "OOO"): return "O"
        j += 1

    # Checking diagonals
    d1 = data[0][0] + data[1][1] + data[2][2]
    d2 = data[2][0] + data[1][1] + data[0][2]
    print("D1: " + d1 + " - D2: " + d2)
    diagonals = [d1, d2]
    k = 0
    while k < 2:
        diagonal = diagonals[k]
        if (diagonal == "XXX"): return "X"
        if (diagonal == "OOO"): return "O"
        k += 1

    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
