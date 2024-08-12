robot_parancs = input("Kérem a robot parancsait: ")

# 2.2 feladat

"""
A count használata:     nagyobb_halmazból.count(elem)    count - megszámlálás
"""
print()
print(f"E betűk száma: {robot_parancs.count("E")}")
print(f"D betűk száma: {robot_parancs.count("D")}")
print(f"K betűk száma: {robot_parancs.count("K")}")
print(f"N betűk száma: {robot_parancs.count("N")}")

# 2.3 feladat

print()
lehetosegek = ["E", "D", "K", "N"]
for egyelem in lehetosegek:
    print(f"{egyelem} betűk száma: {robot_parancs.count(egyelem)}")