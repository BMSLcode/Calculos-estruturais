#: Importações
from math import *

#: Variáveis
h = int(input("Insira a espessura da laje em cm: "))
rmin = float(input("Insira o valor de rmin da tabela 20 e 20A: (Use . para fazer separação decimal): ")) #: Tabela 20 e 20A
Mmáx = float(input("Insira o maior momento máximo da planta: "))
bx = float(input("Insira o valor de bx em cm: "))
b = 1

#: Cálculos
d = (h - 2)
print("\nd: ", d,"cm")

Md = 1.4 * Mmáx
dmin = (rmin * sqrt(Md)) #:"Espessura" mínima

print("dmin: ", dmin, "cm")
print("Md: ", Md, "(Kgf x m)/m")

if dmin < d:
    print("Prossegue o cálculo: \n")
else:
    print("Refaça!")
   

#: Determinar a direção do cálculo
direcao = str(input("Qual a direção que deseja calcular? [X] ou [Y] ? "))
if direcao == "X":

    #: Cálculo da armadura positivo p/ resistir Mx
    #: Dimensionamento do aço
    lajes = 0
    while lajes < 7:
        lx = float(input("Insira o valor de lx em cm: "))
        ly = float(input("Insira o valor de ly em cm: "))
        Mmáx = float(input("\nInsira o momento máximo da laje: "))
        Md = 1.4 * Mmáx
        print("\nMd =", Md, "\n")
        
        r = (d/sqrt(Md))
        print("r =", r)

        if r >= 0.253:
            Alfa = 48.57
            print("Alfa =", Alfa)
        else:
            Alfa = float(input("Insira o valor de Alfa de acordo com a tabela 21 utilizando r: ")) #: Caso não ache o valor correspondente, use o valor menor.

        #: Cálculo do As
        As = (1.4 * Mmáx)/(Alfa * d)
        print("\nAs:", As, "cm²/m")

        if As < 0.9:
            As = 0.9
            print("As < 0.9 = 0.9 cm²/m")
        else:
            As = As
            print("As > 0.9 =", As, "cm²/m")

        #: Número de ferros
        As0 = 0.138

        Num_ferro = As / As0
        print("\nQuantidade de ferro (n∅4.2): ", Num_ferro)
        Num_ferro = int(input("Por gentileza, arredonde para + como inteiros: "))

        #: Espaçamento
        space = 100 / (Num_ferro - 1)
        print("\nEspaçamento (e): ", space, "cm")
        space = int(input("Por gentileza, arredonde para - como inteiros: "))

        norx = (ly - bx) / (space) + 1
        print("\nNørx = ", norx)
        norx = int(input("Por gentileza, arredonde para + como inteiro: "))

        lc = float(input("\nInsira o lc: (0.85, 0.75, 0.70) "))
        lx = lx / 100
        lcx = lc * lx
        print("\n lcx: ", lcx)
        lcx = float(input("Por gentileza, arredonde para múltiplo de 5: "))

        lajes = lajes + 1
        print("\nLaje", lajes, "->", norx, "Ø4.2 C","\b", space, "-", lcx, "\n\nPróxima laje:")

    #: Caso o código se encerre
    print("\nLaje", lajes, "->", norx, "Ø4.2 C", "\b", space, "-", lcx)

    #: Mostrar toda a memória de cálculo para ser copiada e colada na documentação.

#: Cálculo da direção Y
elif direcao == "Y":
    
    #: Cálculo da armadura positivo p/ resistir My
    #: Dimensionamento do aço
    lajes = 0
    while lajes < 7:
        lx = float(input("Insira o valor de lx em cm: "))
        ly = float(input("Insira o valor de ly em cm: "))
        Mmáx = float(input("\nInsira o momento máximo da laje: "))
        Md = 1.4 * Mmáx
        print("\nMd =", Md, "\n")
        
        r = (d/sqrt(Md))
        print("r =", r)

        if r >= 0.253:
            Alfa = 48.57
            print("Alfa =", Alfa)
        else:
            Alfa = float(input("Insira o valor de Alfa de acordo com a tabela 21 utilizando r: ")) #: Caso não ache o valor correspondente, use o valor menor.

        #: Cálculo do As
        As = (1.4 * Mmáx)/(Alfa * d)
        print("\nAs:", As, "cm²/m")

        if As < 0.9:
            As = 0.9
            print("As < 0.9 = 0.9 cm²/m")
        else:
            As = As
            print("As > 0.9 =", As, "cm²/m")

        #: Número de ferros
        As0 = 0.138

        Num_ferro = As / As0
        print("\nQuantidade de ferro (n∅4.2): ", Num_ferro)
        Num_ferro = int(input("Por gentileza, arredonde para + como inteiros: "))

        #: Espaçamento
        space = 100 / (Num_ferro - 1)
        print("\nEspaçamento (e): ", space, "cm")
        space = int(input("Por gentileza, arredonde para - como inteiros: "))

        norx = (lx - bx) / (space) + 1
        print("\nNørx = ", norx)
        norx = int(input("Por gentileza, arredonde para + como inteiro: "))

        lc = float(input("\nInsira o lc: (0.85, 0.75, 0.70) "))
        ly = ly / 100
        lcy = lc * ly
        print("\nlcy: ", lcy)
        lcy = float(input("Por gentileza, arredonde para múltiplo de 5: "))

        lajes = lajes + 1
        print("\nLaje", lajes, "->", norx, "Ø4.2 C","\b", space, "-", lcy, "\n\nPróxima laje:")

    #: Caso o código se encerre
    print("\nLaje", lajes, "->", norx, "Ø4.2 C", "\b", space, "-", lcy)

    #: Mostrar toda a memória de cálculo para ser copiada e colada na documentação.