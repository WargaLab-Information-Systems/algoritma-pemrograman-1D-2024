# NOMOR 1
# mencari nilai volume balok dan tabung
# mencari volume balok menggunakan rumus v=p*l*t

p = 20
l = 13
t = 7

volume_balok = p*l*t
print("nilai hasil dari volume balok adalah", volume_balok, "cm")

# mencari volume tabung menggunakan rumus 

diameter =  14
luas_selimut = 440
phi = 22/7
a = 2

#mencari jari-jari 
jari_jari= diameter / 2

#mencari tinggi tabung
tinggi_tabung = luas_selimut / (2*phi*jari_jari)
print(tinggi_tabung)

#menghitung volume tabung menggunakan rumus phi*2*r*t
volume_tabung = phi * jari_jari**2 * tinggi_tabung
print("nilai hasil dari volume tabung adalah", volume_tabung)
