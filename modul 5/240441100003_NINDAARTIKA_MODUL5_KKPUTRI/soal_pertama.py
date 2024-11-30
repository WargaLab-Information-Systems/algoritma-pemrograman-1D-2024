def hitung_diskon(total_belanja, pilihan_keanggotaan):
    if pilihan_keanggotaan == 1:
        diskon_keanggotaan = 0.15
    elif pilihan_keanggotaan == 2:
        diskon_keanggotaan = 0.10
    elif pilihan_keanggotaan == 3:
        diskon_keanggotaan = 0.05
    else:
        diskon_keanggotaan = 0.0

    diskon_awal = total_belanja * diskon_keanggotaan
    diskon_tambahan = total_belanja * 0.05 if total_belanja > 1000000 else 0.0
    total_diskon = diskon_awal + diskon_tambahan
    total_setelah_diskon = total_belanja - total_diskon

    return total_diskon, total_setelah_diskon
while True:
    print("Pilih jenis keanggotaan:")
    print("1. Gold")
    print("2. Silver")
    print("3. Bronze")
    print("4. Tidak ada keanggotaan")
    pilihan_keanggotaan = input("Masukkan pilihan keanggotaan (1-4): ")
    
    if pilihan_keanggotaan in ['1', '2', '3', '4']:
        pilihan_keanggotaan = int(pilihan_keanggotaan)
    else:
        print("Input tidak valid. Silakan masukkan angka antara 1 hingga 4.")
        continue

    # Meminta input total belanja
    total_belanja = input("Masukkan total belanja: ")

    if total_belanja.replace('.', '', 1):
        total_belanja = float(total_belanja)
    else:
        print("Input tidak valid. Harap masukkan angka positif untuk total belanja.")
        continue

    # Menghitung diskon
    diskon, total_setelah_diskon = hitung_diskon(total_belanja, pilihan_keanggotaan)

    # Menampilkan hasil
    print(f"Total Diskon: {diskon:}")
    print(f"Total Setelah Diskon: {total_setelah_diskon:}")

    # Menanyakan apakah ingin menghitung ulang
    ulang = input("Ingin menghitung ulang? (ya/tidak): ").lower()
    if ulang != 'ya':
        break