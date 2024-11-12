# ## SOAL NO 3

n = int(input("Masukkan bilangan bulat non-negatif: "))
def faktorial():
  if n < 0:
    print("Error: Faktorial tidak terdefinisi untuk bilangan negatif.")
  elif n == 0:
    print("0! = 1")
  else:
    hasil = 1
    print(f"{n}! = ", end="")
    for i in range(n, 0, -1):
      hasil *= i
      print(i, end="")
      if i > 1:
        print(" x ", end="")
      else:
        print(" = ", end="")
    print(hasil)

# Memanggil fungsi faktorial
faktorial()








