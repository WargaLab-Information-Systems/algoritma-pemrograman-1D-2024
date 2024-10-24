nama=input('masukkan nama : ')
nim=input('masukkan nim : ')
nilai_uts=int(input('masukkan nilai UTS : '))
nilai_uas=int(input('masukkan nilai UAS : '))
nilai_rata_rata=(nilai_uts+nilai_uas)/2

print('Nama anda : ',nama)
print('NIM anda : ', nim)
print('Nilai rata-rata anda : ',nilai_rata_rata)

if (nilai_rata_rata <= 100 and nilai_rata_rata>=81):
    print('Anda mendapatkan nilai A')
elif (nilai_rata_rata <= 80 and nilai_rata_rata>=71):
    print(' Anda mendapatkan nilai B')
elif (nilai_rata_rata <= 70 and nilai_rata_rata>=61):
    print(' Anda mendapatkan nilai C')
elif (nilai_rata_rata <= 60 and nilai_rata_rata>=41):
    print(' Anda mendapatkan nilai D')
elif (nilai_rata_rata < 41 and nilai_rata_rata >= 0):
    print('Anda mendapatkan nilai E')
else :
    print ('nilai yang anda input kurang benar')

