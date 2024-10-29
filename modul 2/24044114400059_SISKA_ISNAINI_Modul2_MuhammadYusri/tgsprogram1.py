#data ketentuan
a = 100 - 81
b = 80 - 71
c = 70 - 61
d = 60 - 41
e = 40 - 0


nama = (input("Masukan nama : "))
nim = (input("masukan NIM : "))
nilai_uas = float(input("Masukan nilai UTS : "))
nilai_uts = float(input("Masukan nilai UAS : "))

#menghitung rata ratanya 
rata_rata = (nilai_uts + nilai_uas) / 2 
#rata_rata = int(input("masukan rata rata anda "))
print (f"Nilai rata rata anda {rata_rata} ")

#penyeleksian kondisi
if rata_rata  >= 81:
    print("Anda mendapatkan A ")
elif rata_rata >= 71:
    print("Anda mendapatkan B ")
elif rata_rata >= 61:
    print("Anda mendapat C ")
elif rata_rata >= 41:
    print("Anda mendapatkan D ")
elif rata_rata >= 0:
    print("anda mendapatkan E")
else:
    print("nilai anda tidak valid ")
