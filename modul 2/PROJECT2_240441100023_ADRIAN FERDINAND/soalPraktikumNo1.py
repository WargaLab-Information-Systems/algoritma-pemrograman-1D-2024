# Soal Praktikum Nomor 1

nama = input("Masukan Nama: ")
nim = input("Masukan NIM: ")
nilai_uts = int(input("Masukan Nilai UTS: "))
if nilai_uts > 100 :
    print("Error!, Nilai UTS yang harus anda masukkan 0-100")(exit)
nilai_uas = int(input("Masukan Nilai UAS: "))
if nilai_uas > 100 :
    print("Error!, Nilai UAS yang harus anda masukkan 0-100")(exit)

nilai_rata_rata = (nilai_uts + nilai_uas) / 2

if 81 <= nilai_rata_rata <= 100:
    nilai = "A"
elif 71 <= nilai_rata_rata <= 80:
    nilai = "B"
elif 61 <= nilai_rata_rata <= 70:
    nilai = "C"
elif 41 <= nilai_rata_rata <= 60:
    nilai = "D"
else:
    nilai = "E"

print(f"\nMasukan Nama: {nama}")
print(f"Masukan NIM: {nim}")
print(f"Nilai UTS: {nilai_uts}")
print(f"Nilai UAS: {nilai_uas}")
print(f"Nilai rata-rata anda: {nilai_rata_rata}")
print(f"Anda Mendapatkan Nilai: {nilai}")
