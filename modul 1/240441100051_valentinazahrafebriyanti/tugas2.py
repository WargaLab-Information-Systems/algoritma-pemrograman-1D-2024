#2.Darmaji ingin mengetahui jumlah nilai dari 8 suku pertama dari sebuah deret aritmatika dengan keadaan suku ke-5 dari deret
# tersebut bernilai 11 dan jumlah nilai suku ke-8 dan suku ke 12 nya adalah 52.Buatlah program untuk membantu darmaji untuk
# menyelesaikan masalah tersebut!
#suku yang diketahui
a5 = 11 #suku ke-5
total_a8_a12 = 52
# #menghitung beda (d) dan suku pertama (a1)
# #persamaan 1: a_1 + (5-1) 4d  = 11
# # #dari persamaan 1: 11 - 4d

# # #persamaan 2; 52 = a+7d + a+ 11d
# #2a_1 + 18d =52 /2
# #substitusi nilai a_1 ke dalam persamaan 2
# # 26 = a_1 + 9d
# # 11 = a_1 + 4d
# # 15 = 5d
d = 3
a_1 = 11-4 * d #dari persamaan
# #menghitung jumlah dari 8 suku pertama
n = 8
s_8 = n / 2 * (2 * a_1 + (n-1) * d)
print("suku pertama:", a_1)
print("beda:", d)
print("jumlah nilai dari 8 suku pertama dari deret aritmatika adalah:", s_8)


# #4. Darsono merupakan seorang mandor yang ingin menyusun tim dari beberapa orang, ia memiliki total 7 orang dan ingin memilih 4 orang
# # untuk masuk kedalam timnya. Buatlah program yang dapat membantu darsono menghitung berapa banyak cara untuk membentuk tim tersebut

#c(7,4) = 7! / 4! (7-4) ! #c= kombinasi
   #    = 7! / 4! * 3!

# 7! = 7*6*5* # factorial
# 4! = 4*3*2
# c(7,4) =

factorial_7 = 7 * 6 * 5 
factorial_3 = 3*2

hasil_factorial = factorial_7 / factorial_3
print("jadi hasil", hasil_factorial, "cara untuk memilih 4 orang dari 7 orang")
