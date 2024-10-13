# Soal Praktikum Nomor 1
# Input data mahasiswa
nama = input("Masukan Nama: ")
nim = input("Masukan NIM: ")
# nilai_uts = int(input("Masukan Nilai UTS: "))
# nilai_uas = int(input("Masukan Nilai UAS: "))
nilai_rata_rata = int(input("masukkan nilai rata rata"))

# Menghitung nilai rata-rata
# nilai_rata_rata = (nilai_uts + nilai_uas) / 2
print(f"Masukan Nama: {nama}")
print(f"Masukan NIM: {nim}")
# print(f"Nilai UTS: {nilai_uts}")
# print(f"Nilai UAS: {nilai_uas}")
print(f"Nilai rata-rata anda: {nilai_rata_rata}")

if 81 <= nilai_rata_rata <= 100:
     "A"
elif 71 <= nilai_rata_rata <= 80:
    "B"
elif 61 <= nilai_rata_rata <= 70:
    "C"
elif 41 <= nilai_rata_rata <= 60:
     "D"
elif 0 <= nilai_rata_rata <= 40:
    print( "E")
else:
     print("nilai invalid")

