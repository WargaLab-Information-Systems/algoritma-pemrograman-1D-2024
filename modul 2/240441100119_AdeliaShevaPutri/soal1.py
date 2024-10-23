#soal 1
nama = input("masukan nama: ")
nim = input("masukan NIM : ")
uts = int(input(" nilai uts yang didapatkan: "))
uas = int(input(" nilai uas yang didapatkan: "))
print(" nama: ",nama)
print("NIM : ",nim)
rata_rata = (uts + uas)/ 2
print("nilai rata - rata adalah ",rata_rata)
if rata_rata >= 81 and rata_rata <= 100:
    print("mendapat nilai A")
elif rata_rata >=71 and rata_rata <= 80:
    print("mendapatkan nilai B")
elif rata_rata > 61 and rata_rata <= 70:
    print("mendapatkan nilai C")
elif rata_rata > 41 and rata_rata <= 60:
    print("mendapatkan nilai D")
else:
    print("mendapatkan nilai E")