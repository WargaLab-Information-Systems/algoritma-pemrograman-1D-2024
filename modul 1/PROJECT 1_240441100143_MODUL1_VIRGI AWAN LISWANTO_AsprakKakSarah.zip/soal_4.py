#soal no4
#Rumus
# C(n,k) = n / k(n-k)
# C(7,4) = 7! / 4!(7-4)! = 7!/4!3!
# 7! = 7*6*5*4*3*2*1 = 5040
# 4=\times 3 \times 2\times 1= 24]
# 3= 3*2*1 = 6
#5040 / (24*6) = 5040 / 144 =35 
n = 7 #total orang
k = 4 #orang yang dipilih

print("kali ini kita akan membantu darsono untuk menyusun tim dari beberapa orang")
print("darsono disini memiliki total 7 orang dan ingin memilih 4 orang untuk masuk timnya")
print("disini darsono ingin tau berapa banyak cara untuk membentuk timnya, jadi mari kita bantu")
jumlah_orang = int(input(f"jika jumlah total orang: "))
memilih_orang = int(input(f"dang orang yang ingin dicari:"))

cara_membentuk_tim = 7*6*5*4*3*2*1 / (24*6)
print("jadi untuk menghitung beberapa cara membentuk tim:", cara_membentuk_tim, "cara")


 