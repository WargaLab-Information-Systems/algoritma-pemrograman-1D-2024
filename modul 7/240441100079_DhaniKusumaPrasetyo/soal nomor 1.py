pinjam_alat = {'alat pengukur darah ': 8, 
                'termometer ': 8,
                'stetoskop': 8,
                'pengukur tensi': 8}
print("\ninventaris lab :",pinjam_alat)

alat_dipinjam = {'alat pengukur darah ': 0, 
                'termometer ': 0,
                'stetoskop': 0,
                'pengukur tensi': 0}

pinjam_alat  ['alat pengukur darah '] -=2
pinjam_alat  ['termometer '] -= 3

alat_dipinjam ['alat pengukur darah '] = 2
alat_dipinjam['termometer '] = 3

print("\nbarang yang dipinjam mahasiswi adalah ",alat_dipinjam['alat pengukur darah '],"alat pengukur darah dan ",alat_dipinjam['termometer '],"termometer")
print("barang yang dipinjam mahasiswi adalah :",alat_dipinjam)
print("update inventaris lab :",pinjam_alat)

pinjam_alat  ['stetoskop'] -= 4
alat_dipinjam['stetoskop'] = 4
print("\nbarang yang dipinjam mahasiswi adalah",alat_dipinjam['stetoskop'],"stetoskop")
print("barang yang dipinjam mahasiswi adalah :",alat_dipinjam)
print("update inventaris lab :",pinjam_alat)

pinjam_alat['alat pengukur darah '] += 1
alat_dipinjam['alat pengukur darah '] -= 1 

pinjam_alat  ['termometer '] += 2
alat_dipinjam['termometer '] -= 1

pinjam_alat['pengukur tensi'] = 2
alat_dipinjam['pengukur tensi'] =2

print("\nbarang yang dipinjam mahasiswi setelah menukarnya adalah",alat_dipinjam['pengukur tensi'],"pengukur tensi")
print("barang yang dipinjam mahasiswi adalah :",alat_dipinjam)
print("update inventaris lab :",pinjam_alat)