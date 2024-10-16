nama = str(input("masukkan nama : "))
NIM = str(input("masukkan NIM : "))
UTS = int(input("masukkan nilai UTS : "))
UAS = int(input("masukkan nilai UAS : "))

print(f"masukkan nama:", nama)
print(f"Masukkan NIM:", NIM)

Nilai = int(UTS + UAS) / 2
print(f"Nilai rata-rata anda adalah:", Nilai)

# perintah if elif
if Nilai <= 40:
     print("anda mendapatkan nilai E")
elif Nilai <= 60:
    print("anda mendapatkan nilai D")
elif Nilai <= 70:
    print("anda mendapatkan nilai C")
elif Nilai <= 80:
    print("anda mendapatkan nilai B")
elif Nilai <= 100:
    print("anda mendapatkan nilai A")
else:
    print("tidak mendapat nilai")