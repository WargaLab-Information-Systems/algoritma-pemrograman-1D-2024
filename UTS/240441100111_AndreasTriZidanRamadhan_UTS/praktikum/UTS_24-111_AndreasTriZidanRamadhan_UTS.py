waktu = 0

while True :
    tanya_makan =input('apakah kamu sudah makan? (ya/tidak)')
    if tanya_makan == 'ya':
        waktu += 0
    elif tanya_makan == 'tidak':
        waktu += 15
    else:
        print('masukkan jawaban yang bener dongg!!')
        continue
    
    tanya_mandi=input('apakah kamu sudah mandi? (ya/tidak)')
    if tanya_mandi == 'ya':
        waktu += 0
    elif tanya_mandi == 'tidak':
        waktu += 10
    else:
        print('masukkan jawaban yang bener dongg!!')
        continue

    tanya_kendaraan=input('kamu berangkat menggunakan apa? (jalan kaki / motor)')
    if tanya_kendaraan == 'jalan kaki':
        waktu +=30
    elif tanya_kendaraan == 'motor':
        waktu += 15
    else:
        print('masukkan jawaban yang bener dongg!!')
        continue
    print(f'total waktu yang dibutuhkan untuk persiapan dan perjalanan adalah : {waktu}')

    if waktu > 60:
        print('waktumu terlambat')
    if waktu < 60:
        print('tepat waktu')
    break