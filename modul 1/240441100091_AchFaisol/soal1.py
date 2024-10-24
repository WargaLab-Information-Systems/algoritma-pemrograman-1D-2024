#soal nomer 1
print("disini kita akan membantu Andi menghitung volume dari kedua celengannya")
print("1. kita hitung celengan Andi yang berbentuk balok")
p_balok = int(input("diketahu panjang: "))
l_balok = int(input("diketahui lebar: "))
t_balok = int(input("diketahu tinggi: "))
print("setelah meng-inputkan berapa panjang, lebar, dan tinggi dari celengan Andi barulah kita mencari rumus dari volume balok")
print("rumus dari volume balok adalah panjang*lebar*tinggi")
print(f"jadi kita rubah menjadi angka yaitu {p_balok}cm * {l_balok}cm * {t_balok}cm")
volume_balok = p_balok * l_balok * t_balok
print(f"maka volume dari celengan balok Andi adalah {volume_balok}cm2")
print("2. mencari volume dari celngan tabung")
diameter_tabung = int(input("diketahui daimeter celengan tabung Andi: "))
luasselimut_tabung = int(input("diketahui luas selimut celngan tabung Andi: "))
π = 22/7
print("rumus volume tabung adalah π * r2 * t")
print("jari-jari dan tinggi tabung belum diketahui jadi kita mencarinya terlebih dahulu")
print(f"rumus mencari jari-jari adalah diameter / 2")
jarijari_tabung = diameter_tabung/2
print(f"jadi jari-jarinya adalah {diameter_tabung}cm/2 = {jarijari_tabung}cm")
print(f"rumus mencari tinggi adalah L/(2 * π * jari-jari))")
t_tabung = luasselimut_tabung / (2*π*jarijari_tabung)
print(f"jadi tinggi tabung adalah 440cm2/(2*π*7cm) = {t_tabung}cm")
print("setelah mengetahui jari-jari dan tinggi tabung kita lanjut menghitung volume tabung")
print("rumus volume tabung adalah π * jarijari**2 * tinggi")
volume_tabung = π * jarijari_tabung**2 * t_tabung
print(f"jadi volume tabung dari celengan Andi adalah {volume_tabung}cm3")
