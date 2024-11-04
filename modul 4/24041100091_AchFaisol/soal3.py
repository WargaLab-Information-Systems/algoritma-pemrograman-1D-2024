gajiharian = 100000
totalgajilembur = 0
totallembur = 0
gajilembur = 0
for i in range(7):
    if totallembur >= 40:
        print("lembur melebihi 40, akan dihentikan")
        break
    else:
        jamlembur = int(input(f"jamlembur hari ke {i+1}: "))
        if jamlembur > 8:
                gajilembur == 0
                print("maaf melebihi batas")
                continue
        while jamlembur <= 8:
            if jamlembur > 0 and jamlembur <= 3:
                gajilembur = jamlembur * 25000
                break
            elif jamlembur == 4 or jamlembur == 5:
                gajilembur = 100000
                break
            elif jamlembur == 6 or jamlembur == 7:
                gajilembur = 200000
                break
            elif jamlembur == 8:
                gajilembur = 300000
                break
        
        totalgajilembur += gajilembur
        totallembur += jamlembur
    

gajimingguan = gajiharian * 7
totalgaji = gajimingguan + totalgajilembur

print(f"total lembur selama satu minggu: {totallembur}")
print(f"total gaji lembur: Rp {totalgajilembur}")
print(f"gaji mingguan tanpa lembur: Rp {gajimingguan}")
print(f"total seluruh gaji: Rp {totalgaji}")
    

