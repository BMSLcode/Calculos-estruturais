h = float(input("Insira a altura da viga em metros: "))
Qmáx = float(input("Insira o maior cortante da viga em tf: "))

d = h - 0.05
Qmáx *= 1000

Drd2 = round(532.3 * (d * 100), 2)
Qdmáx = round(1.4 * Qmáx, 2)

print(f"\nd = {d} m \nQmáx = {Qmáx} kgf \nDrd2 = {Drd2} kgf \nQdmáx = {Qdmáx} kgf ")

if Qdmáx < Drd2:
    print("\nProsseguir o cálculo.\n")
else:
    print("\nRefaça\n")

Qsdmin = round(151.36 * (d * 100), 2)
print(f"Qsdmin = {Qsdmin} kgf \n")

if Qdmáx > Qsdmin:
    print(f"{Qdmáx} > {Qsdmin}")
    print("Calcular o Asw! \n")

    Qsw = round(Qdmáx - 99.45 * (d * 100), 2)
    Asw = round(Qsw / (3913.2 * d), 2)
    Ase = round(Asw / 2, 2)

    print(f"Qsw = {Qsw} kgf \nAsw = {Asw} cm/m² \nAse = {Ase} cm/m² \n")

    As5_0 = float(input("Insira o valor da bitola 5.0: "))
    no5_0 = round(Ase / As5_0, 2)
    no5_0 = int(input(f"no5.0 = {no5_0}, por gentileza, arredonde para múltiplo de 5 (+): "))

    e = 100 / (no5_0 - 1)
    emáx = Qdmáx / Drd2

    if emáx <= 0.67:
        emáx = 0.6 * (d * 100)
    elif emáx > 0.67:
        emáx = 0.3 * (d * 100)

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
