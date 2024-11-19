#Soal Nomor 2
#Masukkan Data Mahasiswa
nama = input("Masukkan Nama: ")
skor = int(input("Masukkan Skor: "))
ipk = float(input("Masukkan IPK: "))
#Penyeleksian Kondisi
if skor >= 1100 and ipk >= 3.0:
    print("Selamat Anda Lulus Persyaratan Beasiswa")
else:
    print("Mohon Maaf Anda Tidak Lulus Persyaratan Beasiswa")
