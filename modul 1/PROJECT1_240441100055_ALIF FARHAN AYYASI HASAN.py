# tugas praktikum no 1

panjang_balok = 20
lebar_balok = 13
tinggi_balok = 7
diameter_tabung = 14
luas_selimut_tabung = 440
jari_jari_tabung = 7

volume_balok = panjang_balok*lebar_balok*tinggi_balok
tinggi_tabung = luas_selimut_tabung / (2 * 22/7*(diameter_tabung/2))
volume_tabung = 22/7 * (diameter_tabung / 2)**2 *tinggi_tabung

print("volume balok:", volume_balok, "cm3")
print("volume tabung:", volume_tabung, "cm3")



#tugas praktikum no 2

#Dua variabel awal
suku_5 = 11  # Suku ke-5 adalah 11
jumlah_8_12 = 52  # Jumlah suku ke-8 dan suku ke-12 adalah 52

#menghitung beda (b)
b = (jumlah_8_12 - 2*suku_5) / 10

# Mencari suku pertama (a)
a = suku_5 - 4*b

# Menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku = n * (2*a + (n-1)*b) / 2

# Menampilkan hasil
print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah 8 suku pertama = {jumlah_8_suku}")



# # tugas praktikum no 3

kurs_dollar = 15000  #kurs dollar pada tanggal 25 september 2024
dollar_suraji= 35

total_rupiah_suraji = kurs_dollar*dollar_suraji

print("jadi, total uang sanji jika di konversi dari dollar ke rupiah adalah", total_rupiah_suraji, "rupiah")


#tugss praktikum no 4

#jumlah orang yang ada
n = 7

#jumlah orang yang dipilih ke kelompok
r = 4

faktorial_7=7*6*5*4*3*2*1
faktorial_4=4*3*2*1
faktorial_3=3*2*1

hasil_faktorial = faktorial_7 / (faktorial_4*faktorial_3)

print("jadi hasil", hasil_faktorial, "cara untuk memilih 4 orang dari 7 orang")