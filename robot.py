# 1. feladat

robot_parancs = input("Kérem a robot parancsait: ")

# 2. feladat

"""
Ezt nevezzük megszámlálás tételnek.
"""

E_szamlalo = 0
D_szamlalo = 0
K_szamlalo = 0
N_szamlalo = 0

for egyelem in robot_parancs:
    if egyelem == "E":
        E_szamlalo += 1
    elif egyelem == "D":
        D_szamlalo += 1
    elif egyelem == "K":
        K_szamlalo += 1
    elif egyelem == "N":
        N_szamlalo += 1

print(f"E betűk száma: {E_szamlalo} ")
print(f"D betűk száma: {D_szamlalo} ")
print(f"K betűk száma: {K_szamlalo} ")
print(f"N betűk száma: {N_szamlalo} ")

# 3. feladat

"""
KKKE
"""

# tehát kérdés: = vagy ==. Egy egyenlőség jelet használunk, ha egy változónak megadunk egy értéket.
# Tehát E_szamlalo = 0, ez esetben egy változóhoz (E_szamlalo) hozzáadunk egy értéket (0).
# Na, de ha két változót vizsgálunk, akkor == egyenlőség jel kell.
# if E_szamlalo == D_szamlalo:


if E_szamlalo > D_szamlalo:  # EEEKDKEKDKEKDDNN E = 5, D = 4
    E_szamlalo -= D_szamlalo  # E = 1, D = 4
    D_szamlalo = 0  # E = 1, D = 0
elif E_szamlalo < D_szamlalo:
    D_szamlalo -= E_szamlalo
    E_szamlalo = 0
elif E_szamlalo == D_szamlalo:
    E_szamlalo = 0
    D_szamlalo = 0

if K_szamlalo > N_szamlalo:
    K_szamlalo -= N_szamlalo
    N_szamlalo = 0
elif K_szamlalo < N_szamlalo:
    N_szamlalo -= K_szamlalo
    K_szamlalo = 0
elif K_szamlalo == N_szamlalo:
    K_szamlalo = 0
    N_szamlalo = 0


lehetosegek = ["E", "D", "K", "N"]
parancsok = []

for egyelem in lehetosegek:
    if egyelem == "E":
        parancsok.append(E_szamlalo * egyelem)
    elif egyelem == "D":
        parancsok.append(D_szamlalo * egyelem)
    elif egyelem == "K":
        parancsok.append(K_szamlalo * egyelem)
    elif egyelem == "N":
        parancsok.append(N_szamlalo * egyelem)

print(f"Egy legrövidebb út parancsszava: ", end="")
for egyelem in parancsok:
    print(egyelem, end="")
