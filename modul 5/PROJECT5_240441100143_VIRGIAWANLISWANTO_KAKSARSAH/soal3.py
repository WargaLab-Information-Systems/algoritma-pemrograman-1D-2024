# def factorial(n):
#     while True:
#         if n == 0:
#             return 1
#         if n > 0:
#             return n * factorial(n - 1) 
# print("5! =" ,factorial(5))
# print("3! =" ,factorial(3))  
# print("2! =" ,factorial(2))  
# print("0! =" ,factorial(0))  

# nilai = int(input("masukan nilai: "))
def faktorial(nilai):
    hasil = 1
    for i in range(1, nilai+1):
        hasil *= i
        if i == nilai:
            print(i, end=" = ")
        else:
            print(i, end=" x ")
    return hasil
hasilfaktorial = faktorial (5)
print(f"{5}! {hasilfaktorial}")