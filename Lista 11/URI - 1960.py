N = int(input("Digite um número: "))
a = ""
b = ""
c = ""
if N < 1000 and N > 0:
    centenas = N // 100
    dezenas = (N % 100) // 10
    unidades = N % 10
    if centenas != 0:
        if centenas == 9:
            a = "CM"
        if centenas > 5 and centenas < 9:
            x = centenas - 5
            if x == 1:
                a = "DC"
            if x == 2:
                a = "DCC"
            if x == 3:
                a = "DCCC"
        if centenas == 5:
            a = "D"
        if centenas > 0 and centenas < 5:
            x = 5 - centenas
            if x == 1:
                a = "CD"
            if x == 2:
                a = "CCC"
            if x == 3:
                a = "CC"
            if x == 4:
                a = "C"
    if dezenas != 0:
        if dezenas == 9:
            b = "XC"
        if dezenas > 5 and dezenas < 9:
            y = dezenas - 5
            if y == 1:
                b = "LX"
            if y == 2:
                b = "LXX"
            if y == 3:
                b = "LXXX"
        if dezenas == 5:
            b = "L"
        if dezenas > 0 and dezenas < 5:
            y = 5 - dezenas
            if y == 1:
                b = "XL"
            if y == 2:
                b = "XXX"
            if y == 3:
                b = "XX"
            if y == 4:
                b = "X"
    if unidades == 9:
        c = "IX"
    if unidades > 5 and unidades < 9:
        z = unidades - 5
        if z == 1:
            c = "VI"
        if z == 2:
            c = "VII"
        if z == 3:
            c = "VIII"
    if unidades == 5:
        c = "V"
    if unidades > 0 and unidades < 5:
        z = 5 - unidades
        if z == 1:
            c = "IV"
        if z == 2:
            c = "III"
        if z == 3:
            c = "II"
        if z == 4:
            c = "I"
print(f"{a}{b}{c}")