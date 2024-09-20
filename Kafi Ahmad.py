# simulasi percakapan jual beli
print ("Selamat datang di UTM plaza!")

# input dari pembeli
nama_pembeli = input("pembeli: halo, saya ingin membeli barang. {nama_pembeli}? ")
penjual = "Budi"
print(f"penjual ({penjual}): halo, {nama_pembeli}. apa yang ingin anda beli?")

# menyediakan barang dan harga
barang = input("pembeli: saya ingin membeli barang ?")
harga_barang = int(input(f"penjual ({penjual}): harga {barang} berapa per unit? Rp "))
jumlah_barang = int(input(f"penjual ({penjual}): anda ingin membeli berapa unit {barang}? "))

#perhitungan total harga
total_harga = harga_barang * jumlah_barang

# penerapan diskon (contoh logika: jika beli lebih dari 5 barang, dapat diskon 10%)
if jumlah_barang> 5:
    diskon = total_harga * 0.10 # diskon 10%
    total_bayar = total_harga - diskon
    print(f"penjual({penjual}): anda mendapat diskon 10%! total harga setelah diskon: Rp {total_bayar}")
else:
    total_bayar = total_harga
    print(f"penjual ({penjual}): total harga: Rp {total_bayar}")

#pembayaran
uang_pembeli = int(input (f"pembeli: saya akan membayar Rp "))
if uang_pembeli >= total_bayar:
   kembalian = uang_pembeli - total_bayar
   print(f"penjual ({penjual}): terima kasih, {nama_pembeli}. kembalian anda Rp {kembalian}.")
else:
    kekurangan = total_bayar - uang_pembeli
    print(f"penjual ({penjual}): maaf, uang anda kurang Rp {kekurangan}.")

#penutup percakapan
print(f"penjual ({penjual}): terima kasih telah berbelnja, {nama_pembeli}. selemat berbelanja lagi!")

