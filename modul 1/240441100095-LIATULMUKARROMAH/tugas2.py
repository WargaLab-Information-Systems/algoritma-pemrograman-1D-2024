#soal 2
#diket: U5 =11
#diket: U8+U12 = 52
U5 = int(input("masukkan U5 :"))
U8+U12 = int(input("masukkan U8+U12 :"))
#keterangan menghitung beda
#11 = a+4*b
#52 = a+7*b+a+11*b
#52 = 2a+18*b
#26 = a+9*b - 11 = a+4*b
#15 = 5*b
b = 3
a = U5-4*b
suku ke_n = n/2*(2*a+(n-1)*b)
sukuke8 = 8/2*(2*a+(8-1)*b)
print(f"jumlah 8 suku pertama adalah :{sukuke8}")