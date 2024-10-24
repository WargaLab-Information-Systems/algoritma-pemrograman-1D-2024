nama = str(input("MASUKKAN NAMA ANDA: "))
nim = int(input("MASUKKAN NIM ANDA: "))
nilai_uts = int(input("MASUKKAN NILAI UTS ANDA: "))
nilai_uas = int(input("MASUKKAN NILAI UAS ANDA: "))

hasil_rata_rata = (nilai_uts + nilai_uas)/2
print("HASIL NILAI RATA RATA ANDA ADALAH", hasil_rata_rata)

# a = int(input("MASUKKAN NILAI RATA RATA ANDA: "))

if hasil_rata_rata  >=81 and hasil_rata_rata  <= 100 :
    print("SELAMAT ANDA MENDAPATKAN NILAI A")
elif hasil_rata_rata >=71 and hasil_rata_rata <=80 :
    print("ANDA MENDAPATKAN NILAI B")
elif hasil_rata_rata >=61 and hasil_rata_rata <=70 :
    print("ANDA MENDAPATKAN NILAI C")
elif hasil_rata_rata >=41 and hasil_rata_rata <=60 :
    print("ANDA MENDAPATKAN NILAI D")
elif hasil_rata_rata >=0 and hasil_rata_rata<=40:
    print("ANDA MENDAPATKAN NILAI E")
else :
    print("TIDAK ADA NILAI SEPERTI ITU")