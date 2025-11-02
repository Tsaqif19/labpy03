import random  
n = int(input("Masukkan jumlah bilangan acak (n): "))

if n <= 0:
    print("Jumlah bilangan harus lebih dari 0")
else:
    hitungan = 0

    while hitungan < n:
        angka = random.random()
        if angka < 0.5:
            print(f"bilangan ke {hitungan+1}:{angka}")
            hitungan += 1

        
