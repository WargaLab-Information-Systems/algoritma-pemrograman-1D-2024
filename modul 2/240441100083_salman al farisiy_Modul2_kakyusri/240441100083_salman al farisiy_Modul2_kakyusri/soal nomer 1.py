#soal nomer 1
# nama = (input("masukkan nama :"))
# nim = (input("masukkan NIM: "))
# uts = int(input("masukkan nilai UTS:"))
# uas = int(input("masukkan nilai UAS: "))
nilai = int(input("masukkan nilai:"))

# print ("nama anda:", nama)
# print ("nim anda:", nim)
print ("nilai rata-rata anda:", nilai)


if nilai >= 0 and nilai <= 40:
    print("nilai anda e")
elif nilai >= 41 and nilai <=60:
    print("nilai anda d")
elif nilai >= 61 and nilai <=70:
    print("nilai anda c")
elif nilai >= 71 and nilai <=80:
    print("nilai anda b")
elif nilai >= 81 and nilai <=100:
    print("nilai anda a")
else:
    print("nilai anda tidak valid")
    