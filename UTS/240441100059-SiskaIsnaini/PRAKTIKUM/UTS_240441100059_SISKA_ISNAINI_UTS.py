makan = print (input("Apakah kamu sudah makan? (ya/tidak) ")) 
mandi = print (input("Apakah kamu sudah mandi? (ya/tidak) ")) 
transportasi = (input("mau jalan kaki apa motor? ")) 

total_waktu =''
keterlambatan = ''

if makan == "tidak":
    total_waktu += '15'
if mandi == "tidak":
    total_waktu += '10'
if transportasi == "motor":
    total_waktu += '15'
if transportasi == "jalan kaki":
    total_waktu += '30'
    if keterlambatan >= '15':
        print("kamu tepat waktu")
    if keterlambatan >= '60':
        print("kamu telat")
else:
    print(f"Total waktu persiapan dan perjalanan:{total_waktu}menit")

