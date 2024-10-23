import math

panjang = 20
lebar = 13
tinggi = 7

volume_balok = panjang * lebar * tinggi
print(f"Volume balok celengan: {volume_balok} cm^3")

diameter = 14  
luas_selimut = 440 
radius = diameter / 2

#jika ingin menghitung volume tabung maka harus mencari tingginya terlebih dahulu

tinggi = luas_selimut / (2 * 3.14 * radius)
print (f"tinggi tabung celengan: {tinggi} cm")

volume_tabung = int (3.14 * radius**2 * tinggi)
print(f"Volume tabung celengan: {volume_tabung} cm^3")

