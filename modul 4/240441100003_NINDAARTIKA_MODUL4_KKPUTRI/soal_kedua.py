angka_desimal = int(input("Masukkan bilangan desimal: "))
biner = ""
n = angka_desimal

while n > 0:
    biner = str(n % 2) + biner
    n //= 2

print(f"Bilangan biner dari {angka_desimal} adalah: {biner}")

# Menampilkan pola segitiga
for i in range(1, len(biner) + 1):
    print(biner[:i])
    