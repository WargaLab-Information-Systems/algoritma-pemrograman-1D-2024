# input total belanja 
total_belanja = int(input("masukan total belanja anda: "))
nama_pembeli = input("masukan nama pembeli: ")
member = (input("apakah mempunyai member?, (ya/tidak): "))
usia_pembeli = int(input("masukan usia anda: "))

diskon = 0
# if member =="ya" and total_belanja > 500000:
    
if member == "ya":
    diskon += 15  # Diskon 15% untuk member
 

if total_belanja > 500000:
    diskon += 10   # Diskon tambahan 10% jika total belanja lebih dari Rp500.000

total_harga_diskon = total_belanja - (diskon / 100 * total_belanja)

if (usia_pembeli < 18):
    print("maaf usia anda belum mencukupi")

else: 
    print (nama_pembeli)
    print (total_belanja)
    print ("diskon yang anda dapatkan", diskon)
    print ("total harga setelah diskon :", total_harga_diskon)

