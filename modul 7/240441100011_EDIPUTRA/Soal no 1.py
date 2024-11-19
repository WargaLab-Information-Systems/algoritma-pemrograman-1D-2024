alat_kesehatan_dict = {
    'alat pengukur tekanan darah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'inhaler': 0
}
alat_kesehatan_set = set()

alat_kesehatan_dict['alat pengukur tekanan darah'] += 2
alat_kesehatan_dict['termometer'] += 3
alat_kesehatan_set.add('alat pengukur tekanan darah')
alat_kesehatan_set.add('termometer')

alat_kesehatan_dict['stetoskop'] += 4
alat_kesehatan_set.add('stetoskop')

alat_kesehatan_dict['alat pengukur tekanan darah'] -= 1
if alat_kesehatan_dict['alat pengukur tekanan darah'] <= 0:
  alat_kesehatan_set.remove('alat pengukur tekanan darah')

alat_kesehatan_dict['termometer'] -= 2
if alat_kesehatan_dict['termometer'] <= 0 :
  alat_kesehatan_set.remove('termometer')

alat_kesehatan_dict['stetoskop'] -= 3
if alat_kesehatan_dict['stetoskop'] <= 0 :
  alat_kesehatan_set.remove('stetoskop')

alat_kesehatan_dict['inhaler'] += 2
alat_kesehatan_set.add('inhaler')

print("Alat kesehatan yang masih dipinjam Heni saat ini")
for i in alat_kesehatan_set:
   print(f"- {i}")
print("\nJumlah alat kesehatan yang masih dipinjam Heni saat ini")
for alat,jumlah in alat_kesehatan_dict.items():
   print(f"{alat}: {jumlah}")