nama = input("nama :")
nim = int(input("nim :"))
uts = float(input(" nilai uts :"))
uas = float(input("nilai uas :"))
rata_rata = (uts+uas)/2
print("nama :" ,nama)
print("nilai rata-rata  anda" ,rata_rata)
if rata_rata>=81 and rata_rata<=100:
    print("anda mendapatkan nilai A")
elif rata_rata>=71 and rata_rata<=80:
    print("anda mendapatkan nilai B")
elif rata_rata>=61 and rata_rata<=70:
    print("anda mendapatkan nilai C")
elif rata_rata>=41 and rata_rata<=60:
    print("anda mendapatkan nilai D")
elif rata_rata>=0 and rata_rata<=40:
    print("anda mendapatkan nilai E")
else:
 print("Maaf nilai anda tidak valib")
 