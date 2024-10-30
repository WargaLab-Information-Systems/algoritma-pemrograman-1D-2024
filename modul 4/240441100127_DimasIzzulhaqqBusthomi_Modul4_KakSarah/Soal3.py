gajiPerhari = 100000
gajiPerminggu = gajiPerhari * 7
maxLemburMingguan = 40
totalGajiLembur = 0 
totalJamLembur = 0
lemburlebih = 0

p = int(input("Masukkan hari : "))

for hari in range (1,p + 1):

    if totalJamLembur >= maxLemburMingguan:
        print()
        print("Sudah Mencapai batas Lembur, sekarang pulanglah kerumah, semua orang disana menunggumu")
        print()
        print("Total jam lembur adalah :",totalJamLembur + lemburlebih,"jam, tapi gajimu hanya terhitung 40 jam lembur")
        break
    
    jamLembur = int(input(f"Masukkan berapa jam lembur pada hari ke-{hari} : "))
    
    if jamLembur < 0 :
        jamLembur = 0 
    # if jamLembur > 0 :
    if jamLembur > 8:
        lemburlebih += jamLembur - 8

    if jamLembur > 8 :
        print("Jam lembur melebihi batas, tidak dihitung.")
        jamLembur = 8

    totalJamLembur += jamLembur 

    gajiLemburHarian = 0

    if jamLembur == 0 :
        gajiLemburHarian = 0
    elif jamLembur < 4 :
        gajiLemburHarian += 25000
    elif jamLembur == 4 :
        gajiLemburHarian += 100000
    elif jamLembur == 5 :
        gajiLemburHarian += 100000 + 25000
    elif jamLembur == 6 :
        gajiLemburHarian += 200000
    elif jamLembur == 7 :
        gajiLemburHarian += 200000 + 25000
    elif jamLembur == 8 : 
        gajiLemburHarian += 300000
    
    totalGajiLembur += gajiLemburHarian

    print(f"Hari ke-{hari}: jam lembur {jamLembur}, gaji lembur harian dari total sebelumnya {totalGajiLembur}")
    print("=================================================")
    # else:
    #     print("Kamu tidak lembur")

if totalJamLembur < 40 :
    print()
    print("Total jam lembur adalah :",totalJamLembur,"jam")

totalGajiRegulerLembur = gajiPerminggu + totalGajiLembur

print()
print("=================================================")
print("Total gaji hasil lembur : Rp.",totalGajiLembur)
print("Gaji murni tanpa lembur : Rp.",gajiPerminggu)
print("Total semua gaji        : Rp.",totalGajiRegulerLembur)
