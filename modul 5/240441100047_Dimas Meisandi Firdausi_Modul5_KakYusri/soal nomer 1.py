## SOAL NO 1


# Input total belanja dan keanggotaan dulu ya kak :)
total_belanja = int(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak Ada): ")


def calculate_discount():
    diskon = 0

    # Tentukan diskon berdasarkan jenis keanggotaan
    if keanggotaan == "Gold":
        diskon = 0.15
    elif keanggotaan == "Silver":
        diskon = 0.10
    elif keanggotaan == "Bronze":
        diskon = 0.05
    else:
        diskon = 0.0

    # Hitung diskon tambahan jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 0.05

    # Menghitung total diskon
    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon
    persentase_diskon = diskon * 100
    # Tampilkan hasil
    print(f"Persentase diskon: {int(persentase_diskon)}%")
    print(f"Total diskon: Rp{int(total_diskon,):,}")
    print(f"Total belanja setelah diskon: Rp{int(total_setelah_diskon):,}")

# Panggil fungsi untuk menghitung diskon dan menampilkan hasil
calculate_discount()

























# # Input total belanja dan keanggotaan dulu ya kak
# total_belanja = int(input("Masukkan total belanja: "))
# keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/Tidak Ada): ")

# # Fungsi untuk menghitung diskon
# def calculate_discount():
#     # Inisialisasi diskon
#     diskon = 0

#     # Tentukan diskon berdasarkan jenis keanggotaan
#     if keanggotaan == "Gold":
#         diskon = 0.15
#     elif keanggotaan == "Silver":
#         diskon = 0.10
#     elif keanggotaan == "Bronze":
#         diskon = 0.05
#     else:
#         diskon = 0.0

#     # Hitung diskon tambahan jika total belanja lebih dari 1 juta
#     if total_belanja > 1000000:
#         diskon += 0.05

#     # Hitung total diskon
#     total_diskon = total_belanja * diskon
#     total_setelah_diskon = total_belanja - total_diskon

#     return total_diskon, total_setelah_diskon

# # Hitung diskon dan total setelah diskon
# total_diskon, total_setelah_diskon = calculate_discount()

# # Tampilkan hasilnya
# print(f"Total diskon: Rp{total_diskon:,.2f}")
# print(f"Total belanja setelah diskon: Rp{total_setelah_diskon:,.2f}")
