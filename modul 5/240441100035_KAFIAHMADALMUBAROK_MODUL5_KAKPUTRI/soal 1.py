total_belanja = int(input("masukkan total belanja: "))
keanggotaan = input("masukkan jenis keanggotaan: ").lower()


def hitung_diskon(total_belanja, keanggotaan):
    
    if keanggotaan == "gold":
        diskon = 15
    elif keanggotaan == "silver":
        diskon = 10
    elif keanggotaan == "bronze":
        diskon = 5
    else:
        diskon = 0 
    
    total_diskon = total_belanja * diskon / 100 
    hasil_setelah_diskon = total_belanja - total_diskon 

    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 5

        # total setelah diskon
        total_diskon += tambahan_diskon
        hasil_setelah_diskon = tambahan_diskon

    return hasil_setelah_diskon,total_diskon 

hasil_setelah_diskon,total_diskon = hitung_diskon(total_belanja, keanggotaan)

print(f"total diskon yang di dapat: {total_diskon}")
print(f"total yang harus di bayar: {hasil_setelah_diskon}")