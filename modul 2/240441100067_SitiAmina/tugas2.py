#SELEKSI BEASISWA

#MEMASUKKAN DATA SESUAI DENGAN YANG SUDAH ADA PADA SOAL
skorJaka = 1100
skorIda = 1200
ipkJaka = 3.5
ipkIda = 3.5

minSkor = 1100
minIpk = 3.0

#PENYELEKSIAN KONDISI MENGGUNAKAN IF ELSE DAN JUGA MENAMBAHKAN OPERATOR LOGIKA AND 
#MENGGUNAKAN TIPE DATA BOOLEAN SEBAGAI PERNYATAAN KONDISI
print("---------------------------------------------------")
if skorJaka > minSkor and ipkJaka >= minIpk :
   print("Selamat Jaka, Kamu Lolos seleksi Beasiswa")
else :
   print("Mohon maaf Jaka, Kamu belum memenuhi persyaratan")
   print("---------------------------------------------------")
if skorIda > minSkor and ipkIda >= minIpk :
   print("Selamat Ida, Kamu Lolos seleksi Beasiswa")
else :
   print("Mohon maaf Ida, Kamu belum memenuhi persyaratan")
print("---------------------------------------------------")

