klub_basket = {'zidan','isol','dimas','windy','icha'}
klub_renang = {'dani','jois','windy','zidan','sheva'}

siswa_2_klub = klub_basket.intersection(klub_renang)
print(f'Siswa yang mengikuti 2 klub adalah {siswa_2_klub}')

siswa_1_klub = klub_basket.symmetric_difference(klub_renang)
print(f'Siswa yang mengikuti 1 klub adalah {siswa_1_klub}')

siswa_unik = klub_basket.union(klub_renang)
print(f'Siswa unik yang setidaknya mengikuti satu dari kedua klub adalah {siswa_unik}')

jumlah_siswa_unik = len(siswa_unik)
print(f'Jumlah siswa unik adalah {jumlah_siswa_unik}')
