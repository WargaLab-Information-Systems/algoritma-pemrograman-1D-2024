# jawaban nomor 1
print("jawaban nomor 1")
input("tekan enter untuk lanjut")
print("mencari volume")
# diketahui celengan berbentuk balok memiliki panjang 20, cm, lebar 13 cm, dan tingginya 7 cm
# rumus mencari volume balok adalah panjang*lebar*tinggi

 
panjangB = int(input("masukkan nilai panjang balok yang diketahui :"))
lebarB = int(input("masukkan nilai lebar balok yang diketahui :"))
tinggiB = int(input("masukkan nilai tinggi balok yang di ketahui :"))

volumeB = panjangB*lebarB*tinggiB
print("maka volume dari celengan berbentuk balok adalah ",volumeB, "cm3")

input("tekan enter untuk lanjut")

# diketahui celengan berbentuk tabung memiliki diameter 14 cm dan luas selimut 440 cm2
# rumusnya adalah phi*r*r*t
# r adalah d di bagi 2
# dan karena tinggi belum di ketahui, maka kita cari dulu, rumussnya adalah luas/2*22/7*r

phi = 22/7
dT = int(input("masukkan nilai diameter yang diketahui :"))
luas_ST = int(input("masukkan nilai luas selimut tabung yang diketahui :"))


rT = dT/2
tinggiT = (luas_ST/2)/(phi*rT)

volumeT = phi*rT*rT*tinggiT

print("maka volume dari celengan berbentuk balok adalah ",volumeT, "cm3")

input("tekan enter untuk lanjut ke jawaban nomor2")



# jawaban nomor 2
print("jawaban nomor 2")
input("tekan enter untuk lanjut")
print("mencari suku ke 8")


# di ketahui suku ke 5 adalah 11 
# di ketahui suku ke 8 dan suku ke 12 adalah 52
# berapakah suku ke 8

# U5 = a + (5-1)* b hasilnya a = 11-4b
# U8 + U12 = (a+(8-1)b) + (a+(12-1)b)
# = (a-7b) + (a-11b)
# = 2a + 18b
# dan hasil dari a = 26-9b
# bila sudah di ketahui hasilnya seperti ini maka kita bisa menghitung a dan b
# b

input("tekan enter untuk mengetahui nilai b")
rumusB = (26-11)/(9-4)
b = rumusB
print("nilai dari b adalah ", b)
input("tekan enter untuk lanjut")

# untuk nilai yang b sudah di ketahui, dan sekarang adalah mencari nilai yang ada di a
rumusA = 11-4*(3) 
# 3 adalah hasil dari b yang sudah kita hitung sebelumnya 
a = rumusA
print("nilai a adalah", a)
input("tekan enter untuk mengetahui jawaban")

# sekarang kita aplikasikan kedua nilai yaitu nilai a dan b untuk mencari suku ke 8
n = 8
rumusN = (n/2)*(2*a+(n-1)*b)
print("jadi hasilnya suku ke 8 adalah", rumusN)

input("tekan enter untuk lanjut ke jawaban nomor 3")



# jawaban nomor 3
print("jawaban nomor 3")
input("tekan enter untuk lanjut")
print("menukar mata uang dari uang USD amerika ke Rupiah indonesia")
# ketika ingin menukar mata uang USD amerika ke Rupiah indonesia harus menggunakan kurs beli
# kurs beli USD amerika pada tanggal 25 september adalah 15.107 di ambil dari https://market.bisnis.com/read/20240925/93/1802246/nilai-tukar-rupiah-terhadap-dolar-as-hari-ini-rabu-25-september-2024#:~:text=Nilai%20tukar%20rupiah%20terhadap%20dolar%20Amerika%20Serikat%20%28AS%29,menguat%200%2C53%25%20atau%2080%20poin%20ke%20level%20Rp15.107.

input("tekan enter untuk lanjut")
kurs_beli = 15.107
USD = int(input("masukkan jumlah USD yang akan di tukar :"))
tukar = USD * kurs_beli
print("mata uang yang di tukar dari USD ke rupiah jumlah nominalnya adalah", tukar, "Rupiah")


# jawaban nomor 4
input("tekan enter untuk lanjut ke jawaban nomor 4")
print("jawaban nomor 4")
input("berapakah cara yang dapat di gunakan Darsono untuk memilih 4 orang dari 7 orang untuk di bentuk tim")
# darsono memiliki 7 orang dan hanya 4 yang akan di pilih untuk di bentuk tim, beberapa metode yang di gunakan

orang = int(input("masukkan jumlah orang yang di miliki darsono :"))
input("tekan enter untuk mengetahui jawaban")
N = 5040 # N adalah rumus faktorial dari nilai orang
n = 7
r = 4
R = 24 # R adalah nilai faktorial dari orang yang bisa di 
ncr = 144 # ncr adalah hasil dari (n-r)! 7 - 4  = 3 lalu di faktorisasikan 6

rumusF = (N)//(R*ncr)
print("jadi cara yang digunakan oleh Darsono yaitu ada", rumusF, "cara")