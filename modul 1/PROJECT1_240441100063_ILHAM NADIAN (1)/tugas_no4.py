n = 7
r = 4

faktorial_n = 1
for i in range(1, n + 1):
    faktorial_n = faktorial_n * i

faktorial_r = 1
for i in range(1, r + 1):
    faktorial_r *= i

faktorial_n_minus_r = 1
for i in range(1, n - r + 1):
    faktorial_n_minus_r *= i

kombinasi = faktorial_n // (faktorial_r * faktorial_n_minus_r)

print("Banyak cara untuk membebntuk tim:", kombinasi)