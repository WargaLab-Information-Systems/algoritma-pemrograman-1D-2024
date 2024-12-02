
alat_dipinjam = {
    'alat pengukur tekanan darah': 2,
    'termometer': 3, 'stetoskop': 4
}
print("hari pertama heni meminjam", alat_dipinjam)


alat_dipinjam['alat pengukur tekanan darah'] = 1
alat_dipinjam['termometer'] = 1
alat_dipinjam['stetoskop'] = 1

alat_dipinjam.update({"inhaler" : 2 })
print("\nalat yang masih dipinjam heni saat ini " , alat_dipinjam)




