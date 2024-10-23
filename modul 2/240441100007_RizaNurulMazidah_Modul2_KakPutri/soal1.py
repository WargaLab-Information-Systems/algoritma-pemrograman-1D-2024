nama = "Riza"
nim = 240441100007
nilai_uts = int(input("Masukan Nilai UTS: "))
nilai_uas = int(input("Masukan Nilai UAS: "))

nilai_rata_rata = (nilai_uts + nilai_uas) / 2

if 81 <= nilai_rata_rata <= 100:
    print("Nilai Anda Adalah A")
elif 71 <= nilai_rata_rata <= 80:
    print("Nilai Anda Adalah B")
elif 61 <= nilai_rata_rata <= 70:
    print("Nilai Anda Adalah C")
elif 41 <= nilai_rata_rata <= 60:
    print("Nilai Anda Adalah D")
elif 0  <= nilai_rata_rata <= 40:
    print("Nilai Anda Adalah E")
else:
    print("Nilai Anda Tidak Valid")
    
print("\nNama:", nama)
print("NIM:", nim)
print("Nilai rata-rata anda", nilai_rata_rata)