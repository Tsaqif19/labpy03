modal_awal = 100000000  
total = 0

for bulan in range(1, 9):
    if bulan in [1, 2]:
        laba = 0
    elif bulan in [3, 4]:
        laba = 0.01 * modal_awal
    elif bulan in [5, 6, 7]:
        laba = 0.05 * modal_awal
    elif bulan == 8:
        laba = 0.03 * modal_awal

    print("Bulan ke-",bulan,"laba sebesar:",laba)
    total += laba

print("=================================")
print("Total laba selama 8 bulan:",total)
