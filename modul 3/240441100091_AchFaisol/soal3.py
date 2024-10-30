while True:
  lama_sewa = int(input("Masukkan jumlah hari pinjam: "))

  denda_pokok = 2500
  denda_tambahan = 5500
  total_denda = 0

  if lama_sewa > 5:
     sisa_hari = lama_sewa - 5
     total_denda = sisa_hari*denda_pokok
  if lama_sewa > 10:
      terlambat = sisa_hari - 10
      batas_denda_tambahan = terlambat // 5 
      total_denda += batas_denda_tambahan * denda_tambahan
    

  print("Total denda yang harus dibayar:", total_denda)

  ulang = input("Apakah Anda ingin menghitung kembali?: ")
  if ulang != "iya":
    break
  

