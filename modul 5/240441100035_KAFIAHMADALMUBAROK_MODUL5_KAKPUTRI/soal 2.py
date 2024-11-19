#bilangan fibonacci = 0,1,1,2,3,5,8,13,21,34,55,89.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# memeriksa input yang valid
while True:
    n =int(input("masukan bilangan bulat : "))

    if n < 0:
        print("harap masukkan bilangan bulat non negatif.")
    else:
        print(f"bilangan fibonacci ke {n} adalah : {fibonacci(n)}")

    ulang = input("apakah anda ingin mengulangi? (ya/tidak): ").lower()
    if  ulang != "ya":
        print("program selesai")
        break