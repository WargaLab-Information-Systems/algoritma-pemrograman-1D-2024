nama = input("masukkan nama:")
nim = int(input("masukkan nim:"))
uts = float(input("masukkan niali UTS:"))
uas = float(input("masukkan nillai UAS:"))
rata_rata = ( uts + uas ) /2
print("nilai rata-rata anda", rata_rata)

if rata_rata >= 81 and rata_rata <= 100:
    print("Anda mendapat nilai A")
elif rata_rata >= 71 and rata_rata <= 80:
    print("Anda mendapat nilai B")
elif rata_rata >= 61 and rata_rata <= 70:
    print("Anda mendapat nilai C")
elif rata_rata >= 41 and rata_rata <= 60:
    print("Anda mendapat nilai D")
else :
    print("Anda mendapat nilai E")
