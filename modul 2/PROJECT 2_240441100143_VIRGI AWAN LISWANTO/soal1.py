# Data Diri
nama = "Virgi Awan Liswanto"
nim = 240441100143

# Input nilai
nama1 = input("sebutkan nama: ")
nim1 = int(input("masukkan nim: "))
nilai_uts = float(input("Masukkan nilai UTS (0 - 100): "))
nilai_uas = float(input("Masukkan nilai UAS (0 - 100): "))

# Hitung nilai rata-rata
jumlah_semua_angka = nilai_uts + nilai_uas
jumlah_angka = 2
nilai_rata_rata = jumlah_semua_angka / jumlah_angka

print("Nama: ", nama)
print("NIM: ", nim)
print("Nilai rata-rata: ", nilai_rata_rata)

# Menentukan grade berdasarkan nilai rata-rata
if 100 == nilai_rata_rata:
    grade = 'A+'
elif 99 >= nilai_rata_rata >= 81:
    grade = 'A'
elif 80 >= nilai_rata_rata >= 71:
    grade = 'B'
elif 70 >= nilai_rata_rata >= 61:
    grade = 'C'
elif 60 >= nilai_rata_rata >= 41:
    grade = 'D'
elif 40 >= nilai_rata_rata >= 0:
    grade = 'E'
else:
    grade = 'Nilai tidak valid!'

print(f"Nilai rata-rata: {nilai_rata_rata}, Grade: {grade}")
