tahun=int(input('masukkan tahun yang ingin diketahui : '))

if ((tahun % 4 == 0) and (tahun % 100 != 0)) or (tahun % 400 ==0):
    print('tahun tersebut kabisat')
else:
    print('tahun tersebut tidak kabisat')