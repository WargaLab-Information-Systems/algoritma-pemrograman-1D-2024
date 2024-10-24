nama = input("Masukkan nama: ")
nim = int(input("Masukkan NIM: "))
uts = int(input("Masukkan nilai uts: "))
uas = int(input("Masukkan nilai uas: "))

rata_rata = (uts + uas) / 2

grade = ''
if rata_rata <= 100:
    grade = 'A'
elif rata_rata <= 80:
    grade = 'B'
elif rata_rata <= 70:
    grade = 'C'
elif rata_rata <= 60:
    grade = 'D'
else:
    grade = 'E'

print(f"\nNama:", nama)
print("NIM:", nim)
print("Nilai rata-rata nilai anda", rata_rata)
print("Anda Mendapatkan Nilai", grade)