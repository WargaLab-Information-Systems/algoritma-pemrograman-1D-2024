nama_mahasiswa = input("Masukkan Nama: ")
nim_mahasiswa = input("Masukkan NIM: ")
nilai_uts = int(input("Masukkan Nilai UTS: "))
nilai_uas = int(input("Masukkan Nilai UAS: "))

print(f"Nama Anda: {nama_mahasiswa}")
print(f"NIM Anda: {nim_mahasiswa}")

# Mencari rata-rata
rata_rata = (nilai_uts + nilai_uas) / 2
print(f"Nilai rata-rata Anda adalah: {rata_rata}")

# Perintah if elif
if rata_rata <= 40:
    print("Anda Mendapatkan Nilai E")
elif rata_rata <= 60:
    print("Anda Mendapatkan Nilai D")
elif rata_rata <= 70:
    print("Anda Mendapatkan Nilai C")
elif rata_rata <= 80:
    print("Anda Mendapatkan Nilai B")
elif rata_rata <= 100:
    print("Anda Mendapatkan Nilai A")