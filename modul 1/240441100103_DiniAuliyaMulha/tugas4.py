#soal nomor 4
print("mencari banyak cara untuk membenetuk tim menggunakan rumus kombinasi")
print("rumus C=n!/(r!*(n-r)!)")
n=7
r=4
q=n-r
print("diketahui n,r,(n-r) adalah",n,r,n-r)
#faktorial
faktorial_n= 7*6*5*4*3*2*1
faktorial_r= 4*3*2*1
faktorial_q= 3*2*1
print("faktorial dari n=",n,"adalah",faktorial_n)
print("faktorial dari r=",r,"adalah",faktorial_r)
print("faktorial dari (n-r)=",n-r,"adalah",faktorial_q)
#menghitung kombinasi
kombinasi = faktorial_n / (faktorial_r * faktorial_q)
print(f"terdapat {kombinasi} cara Darsono membentuk tim")