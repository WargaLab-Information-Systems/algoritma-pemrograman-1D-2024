# Jawaban soal nomor1
Nama = str(input("silahkan masukkan Nama anda: "))
Nim = str(input("silahkan masukkan Nim anda: "))
# input data string yaitu Nama dan Nim.

Uts = int(input("Silahkan masukkan nilai UTS anda: "))
Uas = int(input("Silahkan masukkan nilai UAS: "))
# input data integer yaitu Uts dan Uas.
input("tekan enter untuk lanjut")

a = (Uts + Uas) / 2
# rumus rata - rata dari jumlah nilai di bagi jumlah data karena disini datanya dua maka di bagi dua.
if a >=100 or a <0 :
    print("maaf nilai anda tidak valid")
elif a >=81:
    print("Nama anda adalah", Nama)
    print("Nim anda adalah", Nim)
    print("Nilai rata-rata anda adalah", a, "A")
elif a >=71:
    print("Nama anda adalah", Nama)
    print("Nim anda adalah", Nim)
    print("Nilai rata-rata anda adlah", a, "B")
elif a >=61:
    print("Nama anda adalah", Nama)
    print("Nim anda adalah", Nim)
    print("Nilai rata-rata anda adalah", a, "C")
elif a >=41:
    print("Nama anda adalah", Nama)
    print("Nim anda adalah", Nim)
    print("Nilai rata-rata anda adalah", a, "D")
else:
    print("Nama anda adalah", Nama)
    print("Nim anda adalah", Nim)
    print("Nilai rata-rata anda adalah", a, "E")
# Seleksi kondisi
input("tekan enter untuk lanjut ke jawaban nomor 2")


# Jawabn soal nomor2
nilaiJ = 1100
ipkJ = 3.5
# nilai dan ipk dari Jaka
if nilaiJ >=1100 and ipkJ >=3.0:
    print("Selamat Jaka berhasil")
else:
    print("Jaka gagal tetap semangat dan coba lagi")

nilaii = 1000
ipki = 3.5
#nilai dan ipk dari Ida

if nilaii >=1100 and ipki >= 3.0:
    print("Selamat Ida berhasil")
else:
    print("Ida gagal tetap semangat dan coba lagi")

input("tekan enter untuk lanjut ke jawaban nomor 3")

# #jawaban nomor 3

# nilaiJ = 1100
# ipkJ = 3.0
# if nilaiJ >= 1100 and ipkJ >= 3.0:
#     print("Selamat Jaka berhasil")
# else:
#     print("Jaka gagal tetap semangat dan coba lagi")
# nilaii = 1000
# ipki = 3.0
# if nilaii >= 1100 and ipki >= 3.0:
#     print("Selamat Ida berhasil")
# else:
#     print("Ida gagal tetap semangat dan coba lagi")

# input("tekan enter untuk lanjut ke jawaban nomor 4")

# jawaban soal nomor 4
# tahun = int(input("masukkan tahun berapa yang anda cari:"))
# input yang di minta
# rumus yang saya pakai adalah 
# angka tahun di bagi 400, jika habis maka tahun itu merupakan tahun kabisat.
# Jika angka tahun tidak habis dibagi 400 tetapi habis dibagi 100, maka tahun itu bukan tahun kabisat.
# Jika angka tahun itu tidak habis dibagi 400, tidak habis dibagi 100 tetapi habis dibagi 4, maka tahun itu tahun kabisat.
# Dan jika tidak habis di bagi 4 maka tahun itu bukan tahun bukan tahun kabisat.
# Rumus ini saya dapat dari https://id.wikipedia.org/wiki/Tahun_kabisat

# if tahun % 400 == 0:
#     print(tahun, "benar tahun kabisat")
# elif tahun % 100 == 0:
#     print(tahun, "bukan tahun kabisat")
# elif tahun % 4 == 0:
#     print(tahun, "adalah tahun kabisat")
# else:
#     print(tahun, "bukan tahun kabisat")

# input("tekan enter untuk lanjut ke jawaban nomor 5")


# jawaban soal nomor 5
# nama = str(input("Silahkan masukkan nama anda: "))

# usia = int(input("Silahkan masukkan usia anda: "))
# if usia >= 18:
#     member = str(input("apakah anda memiliki member: "))
#     if member == "ya":
#         total = int(input("Silahkan masukkan total belanja anda: "))
#         if total >= 500000:
#             diskon2 = (15 / 100 + 10 / 100) * total
#             hdiskon2 = total - diskon2
#             print("hasil diskon adalah ", + hdiskon2)
#         else:
#             diskon1 = 15 / 100 * total
#             hdiskon1 = total - diskon1
#             print("hasil diskon adalah", + hdiskon1)
#     else:
#         total = int(input("masukkan total belanja anda,: "))

#         # tidak dapat diskon member
#         if total >= 500000:
#             diskon = 10 / 100 * total
#             hdiskon = total - diskon
#             print("hasil diskon adalah", + hdiskon)
#         else:
#             print("maaf anda tidak mendapatkan diskon", + total, + nama)
# else:
#     print("maaf umur anda belum mencukupi",nama)
