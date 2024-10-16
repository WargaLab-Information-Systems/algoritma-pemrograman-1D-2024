nama = input("Masukkan nama Anda: ")
usia = int(input("Masukkan usia Anda: "))

if usia >= 18:
  diskon = 0
  member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")
  total_belanja =int(input("Masukkan total belanja: "))
  if member == "ya":
    diskon = 15
  if total_belanja >= 500000:
    diskon = 10
  if total_belanja > 500000 and member == "ya" :
     diskon = 25
  

  total_diskon = total_belanja *(diskon / 100) 
  total_bayar = total_belanja - total_diskon

  print("Rincian Pembayaran:")
  print("Nama Pembeli:", nama)
  print("Diskon yang didapatkan:", diskon, "%")
  print("Total harga sebelum diskon:",(total_belanja))
  print("Total harga setelah diskon:",(total_bayar))
else: 
    print("maaf usia anda belum lebih dari 18 tahun")

