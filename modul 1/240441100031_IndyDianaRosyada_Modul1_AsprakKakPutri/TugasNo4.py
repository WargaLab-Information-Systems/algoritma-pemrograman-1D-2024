#tugas 4
#menggunakan rumus faktorial c(n,r) = n! / r! (n - r)!
#c(7,4) = 7! / 4! (7 - 4)!
#       = 7! / 4! * 3!

faktorial_n = 7*6*5
faktorial_r = 3*2

hasil_faktorial = faktorial_n / faktorial_r
print(f"Banyak cara untuk membentuk tim dari 7 orang dengan memilih 4 orang adalah: {hasil_faktorial}")