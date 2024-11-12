def faktorial():
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif"
    elif n == 0:
        return "0! = 1"
    else:
        hasil_faktorial = 1
        proses = ""
        for i in range(n, 0, -1):
            hasil_faktorial *= i
            if i > 1:
                proses += f"{i} × "
            else:
                proses += f"{i} = "
        return f"{n}! = {proses}{hasil_faktorial}"

while True:
    n = int(input("Masukkan bilangan : "))
    print(faktorial())

    tanya = input("Apakah kamu ingin menghitung faktorial lagi? (ya/tidak) ")
    if tanya == "tidak":
        print("Terima kasih sudah memnggunakan jasa kami")
        break