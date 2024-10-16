# volume balok
panjang = 20
lebar = 13
tinggi_balok = 7

# volume tabung
diameter = 14
luas_selimut = 440
phi = 22/7

# rumus mencari jari-jari 
jari_jari = diameter / 2

# rumus mencari tinggi tabung
tinggi_tabung = luas_selimut / (2*phi*jari_jari)

# menghitung volume balok
volume_balok = panjang*lebar*tinggi_balok
print("volume celengan balok Andi adalah", volume_balok, "cm")

# menghitung volume tabung
volume_tabung = 2*phi*jari_jari*tinggi_tabung
print("volume celengan tabung Andi adalah", volume_tabung, "cm")
