def faktorial():
    n = int(input("masukkan angka :"))
    faktorial = 1

    for i in range(1, n+1):
        faktorial = faktorial * i
        print(faktorial,end=" ")

faktorial()