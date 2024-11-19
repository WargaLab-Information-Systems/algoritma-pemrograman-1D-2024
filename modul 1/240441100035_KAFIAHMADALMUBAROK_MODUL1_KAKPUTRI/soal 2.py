# un = a+(n-1)b
# u5 = a+4b = 11 ----> 2a+8b = 12
# u8+12 = (a+7b)(a+11b) = 2a+18b = 52
# persamaan
# 2a+18b = 52
# 2a+8b = 22
#    10 = 30
# b = 30/10 = 3
b = 3

input("masukan nilai b: ")
# 11 = a+4b
# 11 + a+12
# 11 - 12 = a
# -1 = a
a = -1
input("masukan nilai a: ")
n = 8
sn = n/2 * (2*a + (n-1)*b)
print(sn)