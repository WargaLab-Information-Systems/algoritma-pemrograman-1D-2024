
#soal no 1
#celengan andi yang berbentuk balok
panjang= 20 #cm
lebar= 13 #cm
tinggi= 7 #cm
hasil1= panjang * lebar * tinggi

#celengan andi yang berbentuk tabung
diameter= 14 #cm
jari_jari= diameter / 2
luas_selimut= 440 #cm^2
phi = 3.14
tinggi_tabung= luas_selimut / (2 * phi  * jari_jari )
volume_tabung= phi * (jari_jari ** 2) * tinggi_tabung

print("membantu andi menghitung volume dari celengan nya yang berbentuk balok")
print("jika diketahui celengan andi yang berbentuk balok  adalah:")
print("panjang nya", panjang, "cm")
print("lebar nya", lebar, "cm")
print("dan tinggi nya", tinggi, "cm")
print("mari kita tentukan volume celengan balok milik andi")
panjang_balok =int(input(f"jika panjang balok tersebut:"))
lebar_balok =int(input(f"jika lebar balok tersebut :"))
tinggi_balok =int(input(f"dan tinggi balok tersebut:"))
volume_balok = panjang_balok * lebar_balok * tinggi_balok
print("maka volume celengan andi yang berbentuk balok adalah:",volume_balok,"cm^3")
#menghitung volume celengan yang berbentuk tabunng
print("sedangkan diketahui celengan andi yang berbentuk tabung adalah:")
print("diameter nya ",diameter, "cm", "artinya jari-jari dari diameter balok adalah jari-jari dibagi 2 =", jari_jari )
print("sedangkan luas selimut nya adalah", luas_selimut, "cm^2", "sebelum menghitung volume tabung" )
print("mari tentukan tinggi dari celengan andi yang berbentuk tabung")
luas_selimut2 =int(input(f"jika diketahui luas selimut dari celengan tabung adalah:"))
jari_jari2 =float(input(f"dan jari-jari dari celengan tersebut adalah:"))
tinggi_tabung2 = luas_selimut2 / (2 * phi * jari_jari2 )
print("dengan memakai rumus: luas_selimut / (2 * pi * jari_jari ) maka tinggi tabung adalah ", tinggi_tabung2, "cm")
print("jika kita sudah menentukan tinggi nya mari kita tentukan volume celengan tabung milik andi")
print("yakni dengan memakai rumus: pi * (jari_jari ** 2) * tinggi_tabung ")
print("maka bisa ditentukan volume celengan andi yang berbentuk tabung memiliki volume:",volume_tabung,"cm^3")