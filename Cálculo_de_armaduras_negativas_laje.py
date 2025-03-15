#: Importações
from math import *

#: Variáveis
h = int(input("Insira a espessura da laje em cm: "))
bitola = float(input("Insira o valor da bitola (Ex: 4.2): "))
Mmáx = float(input("Insira o maior momento máximo da planta: "))
bx = 15
b = 1

#: Cálculos
d = h - 2
Md = 1.4 * Mmáx
r = d / sqrt(Md) #: "Espessura" mínima

print(f"\nd: {d} cm")
print(f"Md: {round(Md, 2)} (Kgf x m)/m")
print(f"r: {round(r, 3)} cm")
alfa = float(input("Insira o valor de alfa de acordo com a tabela 21: ")) #: Alfa

print("")

#: Armadura negativa
As_negativo = round(Md / (alfa * d), 2) 

if As_negativo < .9:
    print("As_negativo: Md / (alfa * d) = As negativo")
    print(f"As_negativo: {Md} / ({alfa} * {d}) = {As_negativo} < 0,9 ∴ As negativo = 0,9 cm²/m \n")
    As_negativo = .9
else:
    print("As_negativo: Md / (alfa * d) = As negativo")
    print(f"As_negativo: {Md} / ({alfa} * {d}) = {As_negativo} > 0,90 cm²/m ∴ As negativo = {As_negativo} cm²/m \n")

#: Função para calcula as bitolas de aço
def nbit(bitola, As_negativo):
    # Área da seção transversal da bitola
    if bitola == 4.2:
        As0 = 0.138
    elif bitola == 5.0:
        As0 = 0.196
    elif bitola == 6.0:
        As0 = 0.282
    else:
        raise ValueError("Bitola não suportada. Use 4.2 ou 5.0 ou 6.0.")
    
    # Cálculo do número de bitolas
    num_bitolas = As_negativo / As0
    print(f"As_negativo / As0 = numero de bitolas")
    print(f"{As_negativo} / {As0} = {num_bitolas}")
    print(f"nbit: {round(num_bitolas, 2)}")

    # Entrada do usuário para arredondar o número de bitolas
    nbit_arredondado = int(input("Insira o valor de nbit arredondado (+): "))
    print(" ")
    return nbit_arredondado


num_bit = nbit(bitola, As_negativo)

while num_bit > 13:
    if bitola == 4.2:
        bitola = 5.0
        print(f"O número de bitolas é maior que 13, ∴ a bitola irá ser ∅5.0 -> r = 0.196")
        num_bit = nbit(bitola, As_negativo)

    elif bitola == 5.0:
        bitola = 6.0
        print("\nO número de bitolas é maior que 13, ∴ a bitola irá ser ∅6.0 -> r = 0.282")
        num_bit = nbit(bitola, As_negativo)
        
#: Espaçamento arredondado na linha do código
e = int(input(f"Espaçamento = {round(100 / (num_bit - 1), 2)} \nInsira o valor do espaçamento arredondado (-): "))

#: Lajes
l1x = float(input("\nInsira o lx da 1° laje em metros: "))
l1y = float(input("Insira o ly da 1° laje em metros: "))

l2x = float(input("\nInsira o lx da 2° laje em metros: "))
l2y = float(input("Insira o ly da 2° laje em metros: "))

#: Dimensões das lajes para determinar o l
if l1x < l1y:
    L1 = l1x
else:
    L1 = l1y

if l2x < l2y:
    L2 = l2x
else:
    L2 = l2y

#: l
if L1 < L2:
    l = L2 * 100
else:
    l = L1 * 100
print(f"\nl = {l} cm")

#: Cálculo do a
bitola = bitola / 10
a = (3/8) * l + 20 * bitola + .75 * d
print(f"\na = {round(a, 2)} cm\n")

print(f"a21: {round((1/3) * a, 2)}")
a21 = int(input("Insira o valor de a21 (+): "))

print(f"a22: {round((2/3) * a, 2)}")
a22 = int(input("Insira o valor de a22 (+): "))

a = a21 + a22
print(f"a = {a21} + {a22} = {a}cm")

#: LN
ln = (a + 2 * d) / 100
print(f"\nLN = {ln}")

print(f"∅ {10 * bitola} C {e} - {ln}")

l_lado = float(input("\nInsira a dimensão da interseção das lajes em metros: "))
l_lado = l_lado * 100
print("norx = ", round((l_lado - bx) / e + 1, 2))
norx = float(input("Insira o valor de norx (+): "))

print(f"{norx} ∅ {10 * bitola} C {e} - {ln}\n")

input("Software desenvolvido por: BMSL ")