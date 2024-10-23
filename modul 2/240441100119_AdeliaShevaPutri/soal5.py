nama = input("nama pembeli: ")
umur = int(input("usianya: "))
belanjaan = int(input("total belanjaan: "))
member = input("memakai member? ")
diskon = 0
if umur < 18:
    print("umur tidak mencukupi")
    exit()
else:
    if  belanjaan > 500000 and member == "tidak":
        diskon += 10
    
    if  belanjaan > 500000 and member == "iya":
        diskon += 25

diskonya = belanjaan * diskon/100
total = belanjaan - diskonya
 
print("harga sebelum diskon ",belanjaan)
print("diskon yang di dapat ",diskon,"%")
print("harga sesudah diskon ",total)

