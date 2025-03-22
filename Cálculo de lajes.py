from math import *

#: Variáveis
h_alv = 0
comprimento_alv = 0

lx = float(input("Insira o valor de lx: "))
ly = float(input("Insira o valor de ly: "))
h = float(input("Espessura da laje em metros: "))

Valor_marcus = ly/lx
print("\nLy/Lx = ",Valor_marcus)

#: Valores da tabela marcus
kx = float(input("Kx: "))
mx = float(input("mx: "))
nx = float(input("nx: "))
my = float(input("my: "))
ny = float(input("ny: "))

#: Cálculo da carga atuante
qpp = h * 2500
qpav = float(input("Valor do qpav: "))
qalv = (input("Possui alvenaria? [S] ou [N]: "))

Area = lx * ly
if Area > 12:
    qsob = 150
else:
    qsob = 200

match qalv:
    case "S":
        h_alv = float(input("Insira a altura da alvenaria em metros: "))
        comprimento_alv = float(input("Insira o comprimento da alvenaria em metros: "))
        qalv = (h_alv * comprimento_alv * 0.15 * 1300) / Area
    case "N":
        qalv = 0


q = qpp + qpav + qalv + qsob

print(f"""CÁLCULO DA CARGA ATUANTE
qpp = {qpp} kgf/m²
qpav = {qpav} kgf/m²
qalv = {qalv} kgf/m²
qsob = {qsob} kgf/m²
q = {q} kgf/m² \n """)

#: Calculo dos momentos
Mx = q * (lx)**2 / mx
My = q * (ly)**2 / my
Xx = -q * (lx)** 2 / nx
Xy = -q * (ly)**2 / ny

print(f"""Calculo dos momentos
Mx = {round(Mx, 2)} kgf * m / m
My = {round(My, 2)} kgf * m / m
Xx = {round(Xx, 2)} kgf * m / m
Xy = {round(Xy, 2)} kgf * m / m \n""")

#: CÁLCULO DAS CARGAS DISTRIBUIDAS
qx = q * kx
qy = q - qx

print(f"""CÁLCULO DAS CARGAS DISTRIBUIDAS:
qx = {round(qx, 2)} kgf / m²
qy = {round(qy, 2)} kgf / m² \n""")