# input nilai
nama = input("masukkan nama: ")
nim = input("masukkan nim: ")
nilai_uts = float(input("masukkan nilai uts: "))
nilai_uas = float(input("masukkan nilai uas: "))

# menghitung rata-rata nilai
rata_rata = (nilai_uts + nilai_uas) / 2
if rata_rata > 100:
    grade = "yang tidak valid"
elif 80 <=rata_rata<=100:
    grade="A"
elif 70 <=rata_rata<80:
    grade="B"
elif 60 <=rata_rata<70:
    grade="C"
elif 40<=rata_rata<60:
    grade="D"
else:
    grade="E"

# menampilkan hasil
print(f"Nama:{nama}")
print(f"Nilai rata_rata anda: {rata_rata}")
print(f"anda mendapatkan nilai {grade}")
