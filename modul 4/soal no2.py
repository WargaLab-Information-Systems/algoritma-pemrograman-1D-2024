# Masukkan bilangan desimal
desimal = int(input("Masukkan bilangan desimal: "))

# Konversi Desimal ke Biner
biner = ""
n = desimal
while n > 0:
    biner = str(n % 2) + biner
    n = n // 2

biner = biner if biner else "0"  # Jika desimal adalah 0, hasil biner adalah "0"

# Tampilkan hasil biner
print(f"\nBilangan biner: {biner}")
print("\nPola Segitiga:")

# Menampilkan Pola Segitiga
panjang = len(biner)
for i in range(1, panjang + 1):
    print(biner[:i])