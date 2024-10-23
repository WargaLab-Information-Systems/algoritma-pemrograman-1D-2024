#Soal Praktikum No.1
#Masukkan Data Mahasiswa
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
nilai_uts = int(input("Masukkan Nilai UTS: "))
nilai_uas = int(input("Masukkan Nilai UAS: "))
#Menghitung Nilai Rata-Rata
nilai_ratarata = (nilai_uts + nilai_uas) / 2
#Penyeleksian Kondisi
if nilai_ratarata >= 81 and nilai_ratarata <=100: 
    print("Nilai Anda adalah A")
elif nilai_ratarata >= 71 and nilai_ratarata <= 80:
    print("Nilai Anda adalah B")
elif nilai_ratarata >= 61 and nilai_ratarata <= 70:
    print("Nilai Anda adalah C")
elif nilai_ratarata >= 41 and nilai_ratarata <= 60:
    print("Nilai Anda adalah D")
else:
    print("Nilai Anda adalah E")
#Menampilkan Hasil
print("Masukkan Nama", nama)
print("NIM: ", nim)
print("Masukkan Nilai UTS: ", nilai_uts)
print("Masukkan Nilai UAS: ", nilai_uas)