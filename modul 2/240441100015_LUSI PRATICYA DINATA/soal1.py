# Input data dari pengguna
Nama = input("Masukan nama anda: ")
NIM = input("Masukan NIM anda: ")
Nilai_UTS = float(input("Masukan nilai UTS anda: "))
Nilai_UAS = float(input("Masukan nilai UAS anda: "))

# Menghitung nilai rata-rata dengan rumus yang benar
Rata_rata = (Nilai_UTS + Nilai_UAS) / 2
print(f"Nilai rata-rata anda: {Rata_rata}")

# Menentukan grade berdasarkan rata-rata
if Rata_rata >= 100:
    print("nilai tidak valid")
elif Rata_rata >= 81:
    print("Anda mendapatkan nilai A")
elif Rata_rata >= 71:
    print("Anda mendapatkan nilai B")
elif Rata_rata >= 61:
    print("Anda mendapatkan nilai C")
elif Rata_rata >= 41:
    print("Anda mendapatkan nilai D")
else:
    print("Anda mendapatkan nilai E")