#NOMER 1
# VOLUME BALOK
print("Diketahui :")
print("panjang balok = 20cm")
print("Lebar = 13cm")
print("tinggi = 7cm")

print("Jika ingin menghitung volume balok,maka masukkan data-data yang sudah diketahui")
panjangbalok=int(input("masukkan panjang balok"))
lebarbalok=int(input("masukkan lebar balok"))
tinggibalok=int(input("masukkan tinggi balok"))

hasil=panjangbalok*lebarbalok*tinggibalok
print('hasil volume dari balok adalah',hasil)

#VOLUME TABUNG
print('diketahui :')
print('diameter = 14cm')
print('luas selimut = 440cm^2')
print('pi = 22/7')
print('r = ?')
print('t = ?')

print('cara menghitung r adalah diameter/2')
r=int(input('masukkan diameter'))
hasilr=r/2
print("hasil dari r adalah ", hasilr)

print('cara mencari tinggi = luas selimut / (2.pi.r)')
hasil1= int(2 * 22 / 7 * hasilr)
luas_selimut=int(input('masukkan luas selimut'))
t=luas_selimut / hasil1
print('hasil dari tinggi adalah ', t)

print('cara menghitung volume tabung adalah volume tabung = pi*r^2*t')
volume_tabung=22/7 * hasilr**2 * t
print('hasil dari volume adalah ', volume_tabung)
