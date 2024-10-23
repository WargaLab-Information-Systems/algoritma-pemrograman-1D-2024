# # soal no1
# nama = input("masukan nama: ")
# nim = input("masukan NIM : ")
# uts = int(input("masukan nilai uts: "))
# uas = int(input("masukan nilai uas: "))
# print("masukan nama: ",nama)
# print("NIM anda: ",nim)
# rata_rata = (uts + uas)/ 2
# print("nilai rata - rata = ",rata_rata)
# if rata_rata > 81 and rata_rata <= 100:
#     print("mendapat nilai a")
# elif rata_rata > 71 and rata_rata <= 80:
#     print("mendapatkan nilai b")
# elif rata_rata > 61 and rata_rata <= 70:
#     print("mendapatkan nilai c")
# elif rata_rata > 41 and rata_rata <= 60:
#     print("mendapatkan nilai d")
# else:
#     print("mendapatkan nilai e")

# # soal no2 dan no3
# skor_minimal = 1100
# ipk_minimal = 3.0

# skor_jaka = 1100
# ipk_jaka = 3.5
# if skor_jaka > skor_minimal and ipk_jaka > ipk_minimal:
#     print(f"maka jaka lulus beasiswa")
# else:
#     print(f"maka jaka tidak lulus beasiswa")

# skor_ida = 1000
# ipk_ida = 3.5
# if skor_ida > skor_minimal and ipk_ida > ipk_minimal:
#     print(f"maka ida lulus beasiswa")
# else:
#     print(f"maka ida tidak lulus beasiswa")

# # soal no4
# tahun = int(input("masukan tahun: "))

# if tahun % 400 == 0 or tahun % 4 == 0:
#     print(tahun," merupakan tahun kabisat")
# else:
#     print(tahun," bukan tahun kabisat")

# # soal no5
# nama = input("nama pembeli ")
# usia = int(input("usia pembeli "))

# if usia < 18:
#     print("maaf usia belum mencukupi")
#     exit()
# else:
#     member = input("apakah pembeli memiliki member? : ") 
#     if member=="iya":
#         total_belanja = float(input("total belanja Rp "))
#         diskon = 15
#     if total_belanja >= 500000 and member == "iya":
#        diskon = 25
#     else :
#         total_belanja = float(input("total belanja Rp "))
#         member=="tidak"
#         total_belanja >= 500000
#         diskon = 10
# diskon_rupiah = total_belanja * diskon/100
# total_bayar = total_belanja - diskon_rupiah

# print("nama pembeli ",nama)
# print("diskon harga yang didapatkan:",diskon,"%")
# print("total harga sebelum diskon: ",total_belanja)
# print("total harga sesudah diskon: ",total_bayar)