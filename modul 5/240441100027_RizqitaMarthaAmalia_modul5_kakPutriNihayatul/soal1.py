def calculate_discount(total_belanja, jenis_keanggotaan):
    diskon = 0
    # diskon untuk belanja lebih dari 1000000
    if total_belanja > 1000000:
        diskon += 0.05
    # diskon berdasarkan jenis keanggotaan
    if jenis_keanggotaan == "Gold":
        diskon += 0.15
    elif jenis_keanggotaan == "Silver":
        diskon += 0.10
    elif jenis_keanggotaan == "Bronze":
        diskon += 0.05
    else:
        diskon += 0.0

    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon
    return total_diskon, total_setelah_diskon

total_belanja = int(input("masukkan total belanja: "))
while True:
    member = input("apakah anda memiliki kartu member? (iya/tidak): ")
# pengguna mempunyai kartu member
    if member == "iya":
       jenis_keanggotaan = (input("masukkan jenis keanggotaanmu (Gold, Silver, Bronze): "))
    else:
       jenis_keanggotaan = "tidak valid, coba masukkan lagi"
       continue
    
    
    diskon, total_setelah_diskon = calculate_discount(total_belanja, jenis_keanggotaan)

    print(f"Total diskon: {diskon}")
    print(f"Total setelah di diskon: {total_setelah_diskon}")
    break