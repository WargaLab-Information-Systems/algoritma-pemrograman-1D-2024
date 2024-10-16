nama = input("masukan nama: ")
nim = input("masukan NIM : ")
uts = int(input("masukan nilai uts: "))
uas = int(input("masukan nilai uas: "))
print("masukan nama: ",nama)
print("NIM anda: ",nim)
rata_rata = (uts + uas)/ 2
print("nilai rata - rata = ",rata_rata)
if rata_rata >= 81 and rata_rata <= 100:
    print("mendapat nilai a")
elif rata_rata >= 71 and rata_rata <= 80:
    print("mendapatkan nilai b")
elif rata_rata >= 61 and rata_rata <= 70:
    print("mendapatkan nilai c")
elif rata_rata >= 41 and rata_rata <= 60:
    print("mendapatkan nilai d")
elif rata_rata >=0 and rata_rata <= 40:
    print("mendapatkan nilai e")
else:
    print("tidak memenuhi kondisi")