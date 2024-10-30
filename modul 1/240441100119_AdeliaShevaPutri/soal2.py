print("U5 = a + 4b = 11 ----> 2a + 8b = 22")
print("U8 + U12 = 2a + 18b = 52")
# mencari nilai b menggunakan persamaan
# 2a + 18b = 52
# 2a + 8b  = 22
#  0   10b = 30
#        b = 30/10 = 3
b = int(input("masukan nilai b = "))
# mencari nilai a
# a + 4b = 11
# a + 4(3)=11
# a + 12 = 11
# a      = 11 - 12 = -1
a = int(input("masukkan nilai a = "))
n = int(input("jumlah suku pertama yang ditambakan = "))
s_n = n/2 * (2*(a)+(n-1)*b)
print(f"jumlah dari 8 suku pertama adalah {s_n}")