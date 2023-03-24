for i in range(1, 100 + 1):
    divisibleByThree = i % 3 == 0
    divisibleByFive = i % 5 == 0
    toPrint = i
    if divisibleByFive or divisibleByThree:
        toPrint = ""
        if divisibleByThree:
            toPrint += "Crackle"
        if divisibleByFive:
            toPrint += "Pop"
    print(toPrint)
