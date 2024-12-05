def kelola_klub_ekstrakurikuler(klub_basket, klub_renang):

  siswa_kedua_klub = klub_basket.intersection(klub_renang)
  print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

  siswa_satu_klub = klub_basket.symmetric_difference(klub_renang)
  print("Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

  semua_siswa_unik = klub_basket.union(klub_renang)
  print("Semua siswa unik:", semua_siswa_unik)

  jumlah_siswa_unik = len(semua_siswa_unik)
  print("Jumlah siswa unik:", jumlah_siswa_unik)

klub_basket = {"adel", "musim", "cebol", "cepa", "sva", "sheva"}
klub_renang = {"musim", "cahyo", "robert", "Gani"}

kelola_klub_ekstrakurikuler(klub_basket, klub_renang)
