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
