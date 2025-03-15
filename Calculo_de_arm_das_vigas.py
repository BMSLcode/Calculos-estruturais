def det_round(G, dec):
    G *= 10 ** dec
    if G % 1 >= .5:
        G = (G + .1) / 10 ** dec
    else:
        G/= 10 ** dec
    return round(G, dec)

def det_r(Md):
    global d
    r = d / (Md / .15) ** .5
    r = det_round(r, 3)
    return r

def det_As(Md, alfa):
    global d
    As = Md / (alfa * d)
    As = det_round(As, 2)
    return As

def det_n8():
    global As
    n8 = As / .5
    if n8 % 1 > 0:
        n8 = n8 + 1 - (n8 % 1)
    return round(n8, 0)

def det_n10():
    global As
    n10 = As / .785
    if n10 % 1 > 0:
        n10 = n10 + 1 - (n10 % 1)
    return round(n10, 0)

def det_n12_5():
    global As
    n12_5 = As / 1.23
    if n12_5 % 1 > 0:
        n12_5 = n12_5 + 1 - (n12_5 % 1)
    return round(n12_5, 0)

def det_Asef_n8(n8):
    Asef = n8 * .5
    Asef = det_round(Asef, 2)
    return Asef

def det_Asef_n10(n10):
    Asef = n10 * .785 #: 2.355
    Asef = det_round(Asef, 2)
    return Asef

def det_Asef_n12_5(n12_5):
    Asef = n12_5 * 1.23
    Asef = det_round(Asef, 2)
    return Asef

def det_desp(Asef, As):
    Desperdício = ((Asef - As) / As) * 100
    Desperdício = det_round(Desperdício, 2)
    return Desperdício


h = float(input("Insira a altura da viga em centimetros: "))
Mmax_1_positivo = float(input("Insira o momento máximo POSITIVO do 1° vão em tf: "))
Mmax_2_positivo = float(input("Insira o momento máximo POSITIVO do 2° vão em tf: "))
Mmax_1_negativo = float(input("Insira o momento máximo NEGATIVO do 1° vão em tf: "))
Mmax_2_negativo = float(input("Insira o momento máximo NEGATIVO do 2° vão em tf: "))


d = h - 5

if Mmax_1_negativo >= Mmax_2_negativo:
    Md = 1.4 * Mmax_1_negativo * 1000
    Md = det_round(Md, 2)
    Momento_escolhido = Mmax_1_negativo * 1000

else:
    Md = 1.4 * Mmax_2_negativo * 1000
    Md = det_round(Md, 2)
    Momento_escolhido = Mmax_2_negativo * 1000

dmin = 0.148 * (Md / .15) ** 0.5
dmin = round(dmin, 2)

if dmin < d:
    print("")
    print(f"d = {h} - 5 = {d} cm")
    print(f"Md = 1.4 * {Momento_escolhido} = {Md} tf")
    print(f"dmin = 0.148 * ({Md} / .15) ** 0.5 = {dmin} cm")
    print(f"{dmin} < {d}, logo, prossegue-se o cálculo! \n")


print("Armadura positiva do 1° vão:\n")

Md = 1.4 * Mmax_1_positivo * 1000
Md = det_round(Md, 2)
r = det_r(Md)
print(f"Md = 1.4 * {Mmax_1_positivo * 1000} = {Md} tf")
print(f"r = {d} / ({Md} / .15) ** .5 = {r}")

alfa = float(input(f"r = {r}, por gentileza, insira o valor de alfa da tabela 21: "))
As = det_As(Md, alfa)
print(f"As = {Md} / ({alfa} * {d}) = {As} cm²\n")

if As >= 1:
    print("Número de barras:")

    n8 = det_n8()
    Asef = det_Asef_n8(n8)
    Desperdício = det_desp(Asef, As)

    print(f"n8 = {As} / .5 = {n8} § 8.0")
    print(f"Asef = {n8} * .5 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

    n10 = det_n10()
    Asef = det_Asef_n10(n10)
    Desperdício = det_desp(Asef, As)

    print(f"n10 = {As} / .785 = {n10} § 10.0")
    print(f"Asef = {n10} * .785 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

    n12_5 = det_n12_5()
    Asef = det_Asef_n12_5(n12_5)
    Desperdício = det_desp(Asef, As)

    print(f"n12_5 = {As} / 1.23 = {n12_5} § 12.5")
    print(f"Asef = {n12_5} * 1.23 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

else:
    print("Usar 2 |0| de 8.0 de asmin! \n")

print("Armadura negativa do 2° apoio:")

Md = 1.4 * Mmax_1_negativo * 1000
Md = round(Md, 2)
r = det_r(Md)
print(f"Md = 1.4 * {Mmax_1_negativo * 1000} = {Md} tf")
print(f"r = {d} / ({Md} / .15) ** .5 = {r}")

alfa = float(input(f"r = {r}, por gentileza, insira o valor de alfa da tabela 21: "))
As = det_As(Md, alfa)
print(f"As = {Md} / ({alfa} * {d}) = {As} cm²\n")

if As >= 1:
    print("Número de barras: ")

    n8 = det_n8()
    Asef = det_Asef_n8(n8)
    Desperdício = det_desp(Asef, As)

    print(f"n8 = {As} / .5 = {n8} § 8.0")
    print(f"Asef = {n8} * .5 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

    n10 = det_n10()
    Asef = det_Asef_n10(n10)
    Desperdício = det_desp(Asef, As)

    print(f"n10 = {As} / .785 = {n10} § 10.0")
    print(f"Asef = {n10} * .785 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

    n12_5 = det_n12_5()
    Asef = det_Asef_n12_5(n12_5)
    Desperdício = det_desp(Asef, As)

    print(f"n12_5 = {As} / 1.23 = {n12_5} § 12.5")
    print(f"Asef = {n12_5} * 1.23 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")
else:
    print("Usar 2 |0| de 8.0 de asmin! \n")

print("Armadura positiva do 2° vão:\n")

Md = 1.4 * Mmax_2_positivo * 1000
Md = round(Md, 2)
r = det_r(Md)
print(f"Md = 1.4 * {Mmax_2_positivo * 1000} = {Md} tf")
print(f"r = {d} / ({Md} / .15) ** .5 = {r}")

alfa = float(input(f"r = {r}, por gentileza, insira o valor de alfa da tabela 21: "))
As = det_As(Md, alfa)
print(f"As = {Md} / ({alfa} * {d}) = {As} cm²\n")

if As >= 1:
    print("Número de barras:")

    n8 = det_n8()
    Asef = det_Asef_n8(n8)
    Desperdício = det_desp(Asef, As)

    print(f"n8 = {As} / .5 = {n8} § 8.0")
    print(f"Asef = {n8} * .5 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

    n10 = det_n10()
    Asef = det_Asef_n10(n10)
    Desperdício = det_desp(Asef, As)

    print(f"n10 = {As} / .785 = {n10} § 10.0")
    print(f"Asef = {n10} * .785 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

    n12_5 = det_n12_5()
    Asef = det_Asef_n12_5(n12_5)
    Desperdício = det_desp(Asef, As)

    print(f"n12_5 = {As} / 1.23 = {n12_5} § 12.5")
    print(f"Asef = {n12_5} * 1.23 = {Asef} cm²")
    print(f"Desperdício = (({Asef} - {As}) / {As}) * 100 = {Desperdício}% \n")

else:
    print("Usar 2 |0| de 8.0 para o asmin!")
