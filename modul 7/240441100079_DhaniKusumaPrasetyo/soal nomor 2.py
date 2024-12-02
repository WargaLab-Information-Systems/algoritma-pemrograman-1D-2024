basket = {'dhani','jois','zidan','salman','revan'}
renang = {'jois','salman','faisol','dimas','farhan'}

sama = basket.intersection(renang)
print("siswa yang mengikuti kedua klub adalah :",sama)

sama = basket.symmetric_difference(renang)
print("siswa yang mengikuti satu klub saja :",sama)

gabung = basket.union(renang)
print("seluruh siswa yang hanya mengikuti setidaknya satu klub dari kedua klub tersebut", gabung)

jumlah = len(gabung)
print("jumlah seluruh siswa unik adalah :", jumlah)
