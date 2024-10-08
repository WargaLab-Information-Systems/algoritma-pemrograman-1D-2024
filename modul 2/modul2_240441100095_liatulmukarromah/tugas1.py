#KETENTUAN NILAI 
#100-81=A
#80-71=B
#70-61=C
#60-41=D
#40-0=E
 #input data
nama = input("masukkan nama: ")
nim = input("masukkan nim: ")
nilai_uts = int(input("masukkan nilai uts: "))
nilai_uas = int(input("masukkan nilai uas: "))

#menghitung skor rata-rata
nilai_rata_rata = (nilai_uts + nilai_uas)/2

#menentukan nilai
if 100 >= nilai_rata_rata >= 81:
    nilai = 'A'
elif 80 >= nilai_rata_rata >= 71:
    nilai = 'B'
elif 70 >= nilai_rata_rata >= 61:
    nilai = 'C'
elif 60 >= nilai_rata_rata >= 41:
    nilai = 'D'
elif 40 >= nilai_rata_rata >= 0:
    nilai = 'E'
else:
    nilai = "nilai tidak valid"
    print("nilai rata rata tidak memenuhi")

#hasil
print(f"nama: {nama}")
print(f"nim: {nim}")
print(f"nilai rata-rata: {nilai_rata_rata}")
print(f"anda mendapatkan nilai: {nilai}")