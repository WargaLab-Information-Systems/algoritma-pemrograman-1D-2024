#balok
panjang = 20
lebar = 13
tinggi_balok = 7

#tabung
diameter_tabung = 14
radius_tabung = diameter_tabung / 2
luas_selimut_tabung = 440  
tinggi_tabung = luas_selimut_tabung / (2 * 3.14 * radius_tabung)

volume_balok = panjang * lebar * tinggi_balok
volume_tabung = 3.14 * radius_tabung**2 * tinggi_tabung

print("Hasil dari volume balok:", volume_balok)
print("Hasil dari volume tabung:", volume_tabung) 

