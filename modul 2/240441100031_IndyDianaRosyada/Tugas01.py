nama = input("Masukkan Nama: ")
nim = input("Masukkan Nim: ")
Nilai_UTS = int(input("Masukkan Nilai UTS: "))
Nilai_UAS = int(input("Masukkan Nilai UAS: "))

Nilai_Rata_Rata = (Nilai_UTS + Nilai_UAS) / 2

if 81 <= Nilai_Rata_Rata <= 100:
    nilai = "A"
elif 71 <= Nilai_Rata_Rata <= 80:
    nilai = "B"
elif 61 <= Nilai_Rata_Rata <= 70:
    nilai = "C"
elif 41 <= Nilai_Rata_Rata <= 60:
    nilai = "D"
elif 0 <= Nilai_Rata_Rata <= 41:
    nilai = "E"
else:
    nilai = "skor tidak valid"

print("Masukkan Nama",nama)
print("Masukkan Nim",nim)
print("Nilai Rata Rata anda",Nilai_Rata_Rata)
print("Anda mendapatkan nilai",nilai)