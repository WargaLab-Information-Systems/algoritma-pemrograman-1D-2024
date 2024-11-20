alat ={
    'pengukur_tekanan_darah': 0,
    'termometer': 0,
    'inhaler': 0,
    'stetoskop': 0

}


alat ["pengukur_tekanan_darah"] += 2
alat ["termometer"] += 3
print("\nhari kesatu meminjam", alat)

alat ["stetoskop"] += 4
print("\nhari kedua meminjam", alat)

alat ["pengukur_tekanan_darah"] -= 1
alat ["termometer"] -= 2
print("\nhari ke tuju", alat)

if alat["stetoskop"] == 4:
    alat["stetoskop"] -= 3
    alat["inhaler"] += 2
    print("\nbarang yang ditukar", alat)
else:
    print()


print(f"{alat}")
