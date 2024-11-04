def hitung_diskon(total_belanja, keanggotaan):
    if keanggotaan == "Gold":
        diskon = 0.15
    elif keanggotaan == "Silver":
        diskon = 0.10
    elif keanggotaan == "Bronze":
        diskon = 0.05
    else:
        diskon = 0.0

    jumlah_diskon = total_belanja * diskon

    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 0.05
        jumlah_diskon += tambahan_diskon

    total_setelah_diskon = total_belanja - jumlah_diskon
    return total_belanja, jumlah_diskon, total_setelah_diskon

total_belanja = int(input("Masukkan total belanja: "))

while True:
    print("Pilih jenis keanggotaan:")
    print("1. Gold")
    print("2. Silver")
    print("3. Bronze")
    print("4. Tidak ada keanggotaan")

    pilihan = input("Masukkan pilihan keanggotaan (1/2/3/4): ")

    if pilihan == "1":
        keanggotaan = "Gold"
        break
    elif pilihan == "2":
        keanggotaan = "Silver"
        break
    elif pilihan == "3":
        keanggotaan = "Bronze"
        break
    elif pilihan == "4":
        keanggotaan = "Tidak ada"
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3, atau 4.")

total_awal, jumlah_diskon, total_setelah_diskon = hitung_diskon(total_belanja, keanggotaan)

print("Total belanja sebelum diskon:", total_awal)
print("Jumlah diskon:", jumlah_diskon)
print("Total belanja setelah diskon:", total_setelah_diskon)