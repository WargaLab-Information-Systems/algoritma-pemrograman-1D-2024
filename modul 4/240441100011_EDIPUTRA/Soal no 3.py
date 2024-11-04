total_jam_lembur = 0          
total_gaji_lembur = 0        

for hari in range(1, 7+1):
    if total_jam_lembur  >= 40:
        print("Total lembur dalam seminggu telah mencapai atau melebihi 40 jam, lembur dihentikan.")
        break

    else:
        print(f"\nHari ke-{hari}")
        jam_lembur = int(input("Masukkan jam lembur hari ini: "))
        
        if jam_lembur > 8 :
            print("Lembur melebihi batas, tidak dihitung.")
            continue
    
        while jam_lembur <= 8:
            if jam_lembur == 0:
                gaji_lembur_harian = 0
                break
                
            elif jam_lembur > 0 and jam_lembur <= 3:
                gaji_lembur_harian = 25000 * jam_lembur
                break
                
            elif jam_lembur >= 4 and jam_lembur < 6:
                gaji_lembur_harian = 100000
                break
              
            elif jam_lembur >= 6 and jam_lembur < 8:
                gaji_lembur_harian = 200000
                break
              
            elif jam_lembur == 8:
                gaji_lembur_harian = 300000
                break
            
        total_gaji_lembur += gaji_lembur_harian 
        total_jam_lembur += jam_lembur
        print(f"Lembur hari ini: {jam_lembur} jam, Uang lembur: Rp {gaji_lembur_harian}")

total_gaji_mingguan = 100000 * 7 
total_gaji_mingguan_termasuk_lembur = total_gaji_mingguan + total_gaji_lembur 

print("\n--- Rekapitulasi Gaji Mingguan Mas Ironi ---")
print(f"Total lembur selama 1 minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_mingguan}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan_termasuk_lembur}")
