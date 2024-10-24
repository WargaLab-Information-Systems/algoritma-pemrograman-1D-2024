nama= input("masukkan nama ")
nim= int(input("masukkan nim"))
uts= float(input("masukkan nilai uts: "))
uas= float(input("masukkan nilai uas: "))
rata= (uas+uts)/2
print("masukkan nama ",nama)
print("nim anda: ",nim)
print("nilai rata rata anda ",rata)

if rata>=80 and rata<=100:
    print("anda mendapatkan nilai b")
elif rata>=71 and rata<=80:
    print("anda mendapatkan nilai c")
elif rata>=61 and rata<70:
    print("anda mendaptkan nilai d")
elif rata>=41 and rata<=60:
    print("anda mendapatkan nilai e")
elif rata>=0 and rata<=40:
    print("anda mendapatkan nilai f")
else:
    print("tidak ada nilai segitu")
