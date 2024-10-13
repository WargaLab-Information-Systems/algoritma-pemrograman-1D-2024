#1.Andi mempunyai celengan berbentuk balok dan tabung. celengan yang berbentuk balok memiliki ukuran panjang 20cm,lebar 13cm dan tinggi 75cm
#sedangkan celengan yang berbentuk tabung memiliki diameter 14cm dan luas selimutnya 440cm2
#buatlah program menghitung volume dari kedua celengan  yang dimiliki andi!
#volume Balok
#Rumus volume balok: Volume=Panjang*Lebar*Tinggi
panjang = 20 #cm
lebar = 13 #cm
tinggi =7 #cm
volume = panjang * lebar * tinggi
print("volume balok : ", volume) #cm

#volume tabung
#rumus volume tabung =phi * jari-jari * jari-jari * tinggi
#diketahui
jari_jari = 7 #diamter/2
luas_selimut =440
tinggi = 10 # luas selimut= 2 * 22/7 * 7 = 44 (luas selimut/ hasil) = tinggi

#volume tabung
phi = 22/7
volume = phi * jari_jari * jari_jari * tinggi
print("volume : ", volume)
