print("Saldo saat ini: Rp 1000000")

saldo_awal = 1000000

while True:
    print("Apa yang mau anda lakukan?")
    print("1. Tarik Uang")
    print("2. Keluar")
    print("===============================")
    menu = input("pilih menu (1/2): ")

    if menu == "1":
        a = int(input("Masukkan Jumlah penarikan: "))
        if a <= 0:
            print("Jumlah penarikan harus lebih dari 0 Rp")

        elif a > saldo_awal:
            print(" SALDO ANDA TIDAK MENCUKUPI")
            break
        
        else:
            sisa_saldo = saldo_awal - a
            print("Penarikan Berhasil!")
            print(f"Saldo saat ini: Rp {sisa_saldo}")
            saldo_awal = sisa_saldo

            if sisa_saldo == 0:
                print("Saldo anda sudah habis!")
                break
                
    elif menu == "2":
        print("Terimakasih telah menggunakan ATM!")
        break

    else:
        print("Pilihan tidak valid")
        



    





