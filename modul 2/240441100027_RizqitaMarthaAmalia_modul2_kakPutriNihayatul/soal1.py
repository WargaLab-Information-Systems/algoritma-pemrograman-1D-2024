# soal 1
nama = (input("Nama: "))
nim = int(input("Masukkan nim:"))
nilai_uts = int(input("Masukkan nilai uts: "))
nilai_uas = int(input("Masukkan nilai uas: "))
nilai_rata = int((nilai_uts + nilai_uas) / 2)
hasil = int((nilai_uts + nilai_uas) / 2)
print("nilai rata rata", hasil)

# pengkondisian
if 100 >= hasil >= 81 :
    print("Nilai A")
elif 80 >= hasil >= 71 :
    print("Nilai B")
elif 70 >= hasil >= 61 :
    print("Nilai C")
elif 60 >= hasil >= 41 :
    print("Nilai D")
elif 40 >= hasil >=0 :
    print("Nilai E")
else :
    print("Maaf nilai anda tidak valid")