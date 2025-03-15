h = float(input("Insira a altura da viga em metros: "))
Qmáx = float(input("Insira o maior cortante da viga em tf: "))
Comprimento_viga = float(input("Insira o comprimento total da viga em metros: "))

Comprimento_viga *= 100
b = .15
d_m = h - 0.05
d_cm = (h * 100) - 5
Qmáx *= 1000

Qrd2 = round(532.3 * d_cm, 2)
Qdmáx = round(1.4 * Qmáx, 2)

print(f"""\n
d = {h} - 0.05 = {d_m} m
Qmáx = {Qmáx/1000} * 1000 = {Qmáx} kgf
Qrd2 = 532.3 * {d_cm} = {Qrd2} kgf
Qdmáx = 1.4 * {Qmáx} = {Qdmáx} kgf
""")

if Qdmáx < Qrd2:
    print("\nProsseguir o cálculo.\n")
else:
    print("\nRefaça\n")

Qsdmin = round(151.36 * d_cm, 2)
print(f"Qsdmin = 151.36 * {d_cm} = {Qsdmin} kgf \n")

if Qdmáx > Qsdmin:
    print(f"{Qdmáx} > {Qsdmin}")
    print("Calcular o Asw! \n")

    Qsw = round(Qdmáx - 99.45 * (d_cm), 2)
    Asw = round(Qsw / (3913.2 * d_m), 2)
    Ase = round(Asw / 2, 2)

    print(f"Qsw = {Qsw} kgf \nAsw = {Asw} cm/m² \nAse = {Ase} cm/m² \n")

    As5_0 = float(input("Insira o valor da bitola 5.0: "))
    no5_0 = round(Ase / As5_0, 2)
    no5_0 = int(input(f"no5.0 = {no5_0}, por gentileza, arredonde para múltiplo de 5 (+): "))

    e = 100 / (no5_0 - 1)
    emáx = Qdmáx / Qrd2

    if emáx <= 0.67:
        emáx = 0.6 * d_cm
    elif emáx > 0.67:
        emáx = 0.3 * d_cm

    if emáx <= 30:
        print(f"\n5.0 C {emáx}\n")

    if 25 < emáx:
        print("Calcular o tmaior. \n")

        carga_viga = float(input("Insira a carga da viga em tf: "))
        carga_viga *= 1000
        tmaior = round((Qdmáx - Qsdmin) / (1.4 * carga_viga), 2)
        tmaior = float(input(f"tmaior = {tmaior}, por favor, arredonde para múltiplo de 5 (+): "))

        Qmáx = float(input("Insira o maior cortante da viga em tf: "))
        Qdmáx_2 = round(1.4 * Qmáx, 2)

else:
    print(f"{Qdmáx} <= {Qsdmin}")
    print("Para que se tenha armadura mínima de estribo para toda viga!")
    emáx = round(Qdmáx / Qrd2, 2)
    print(f"emáx = {Qdmáx} / {Qrd2} = {emáx} cm \n")

    if emáx < .67:
        e = .6 * d_cm
                
        if emáx <= 30:
            Quantidade_de_ferro = (((Comprimento_viga + 30) - 5)/ e) + 1
            if Quantidade_de_ferro % 1 > 0:
                Quantidade_de_ferro = Quantidade_de_ferro + 1 - (Quantidade_de_ferro % 1)
            
            perímetro = round(b * 2 + h * 2, 2)
            
            
            print(f"e = 0.6 * {d_cm} = {.6 * d_cm} cm")
            print(f"Quantidade_de_ferro = ((({Comprimento_viga} + 30) - 5) / {emáx}) + 1 = {Quantidade_de_ferro}")
            print(f"Perímetro = {b} * 2 + {h} * 2 = {perímetro} m")
            print(f"{Quantidade_de_ferro} |o| 5.0 C {e} - {perímetro}")
