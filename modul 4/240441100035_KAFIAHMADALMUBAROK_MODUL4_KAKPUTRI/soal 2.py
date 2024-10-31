bilangan_desimal =int(input("masukan bilangan desimal: "))

hasil_biner= ""
n = bilangan_desimal
while n > 0:
    hasil_biner = str(n % 2) + hasil_biner
    n = n // 2
if hasil_biner== "1":
    hasil_biner= "0"
print(f"bilangan biner: {hasil_biner}") 

#mencetak pola segitiga
print("pola segitiga")
pola=""
for digit in hasil_biner:
    pola += digit
    print(pola)

