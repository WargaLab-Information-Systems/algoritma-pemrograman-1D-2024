# Diskon
diskon1 = 15  # Diskon untuk member
diskon2 = 10  # Diskon untuk belanja di atas 500.000
diskonmember = diskon1 / 100
diskonbelanja = diskon2 / 100


nama_pembeli = input("Masukkan nama pembeli: ")
umur = int(input("Masukkan umur pembeli: "))

if umur < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    total_belanja = int(input("Masukkan total belanja: "))
    member = input("Apakah kamu mempunyai kartu member (punya/tidak punya)? ")

    # Inisialisasi nilai diskon
    nilai_diskon = 0

    if member == "punya" and total_belanja > 500000:
        nilai_diskon = total_belanja * (diskonbelanja+diskonmember)  # Diskon untuk belanja di atas 500.000
    elif member == "punya" and total_belanja < 500000:
        nilai_diskon = total_belanja * diskonmember  # Diskon untuk member
    elif member == "tidak punya" and total_belanja > 500000:
        nilai_diskon = total_belanja * diskonbelanja  # Diskon untuk belanja di atas 500.000

    harga_setelah_diskon = total_belanja - nilai_diskon

    print("     Detail Pembelian     ")
    print("Nama Pembeli:", nama_pembeli)
    print("Umur Pembeli:", umur)
    print("Total Harga Sebelum Diskon:", total_belanja)
    print("diskon yang didapatkan:", nilai_diskon)
    
    if nilai_diskon > 0:
        print("Total Harga Setelah Diskon:", harga_setelah_diskon)
    else:
        print("Total belanja mu tanpa diskon:", total_belanja)
