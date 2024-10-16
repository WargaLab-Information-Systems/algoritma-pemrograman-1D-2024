#PENYELEKSIAN NILAI AKHIR SEMESTER

#MEMASUKKAN DATA NAMA, NIM, NILAI UTS, DAN NILAI UAS UNTUK DIJADIKAN SEBAGAI ACUAN PENILAIAN
print("---------------------------------------------------")
print("SELAMAT DATANG DI PENYELEKSIAN NILAI AKHIR SEMESTER")
print("---------------------------------------------------")
nama = input("Masukkan Nama ")
nim = input("Masukkan NIM ")
UTS = int (input("Masukkan nilai UTS : "))
UAS = int (input("Masukkan nilai UAS : "))

#MENGELUARKAN DATA YANG SUDAH DIINPUTKAN DAN MEMPROSES PERHITUNGAN NILAI DENGAN MENCARI NILAI RATA-RATA
print("DATA YANG TELAH ANDA MASUKKAN")
print("--------------------------------------------------")
print("Masukan Nama" , nama )
print("NIM Anda : " , nim)
rata_rata = (UTS + UAS) / 2
print("Nilai rata-rata Anda adalah : " , rata_rata )

#PENYELEKSIAN KONDISI MENGGUNAKAN IF ELIF ELSE DENGAN KETENTUAN SOAL
if rata_rata >= 81 :
    print("Anda mendapatkan Nilai A")
elif rata_rata >= 71 :
    print("Anda mendapatkan Nilai B")
elif rata_rata >= 61 :
    print("Anda mendapatkan Nilai C")
elif rata_rata > 41 :
    print("Anda mendapatkan Nilai D")
else :
    print("Anda mendapatkan Nilai E")

print("--------------------------------------------------")



