pin = "932041"
attempt = 0
limit = 3

while limit > 0:
    PIN = input("Masukkan PIN ATM Anda : " )

    if pin == PIN:
        print("\n Selamat Datang ATM SOKUL \n")
        break
    else:
        limit -= 1
        print("PIN Anda Salah! \n")

if limit == attempt:
    print("Proses Login Gagal! Silahkan coba beberapa saat lagi!")
    print("Terimakasih Telah menggunakan layanan kami!\n ")
    exit()

print("===============================================================")
print("=========================  ATM SOKUL  ==========================")

while True:
    print("Jenis Transaksi Yang Tersedia :")
    print("1. Tarik Tunai")
    print("2. Transfer")
    print("3. Setor Tunai \n")
    transaksi = (input("Pilih Jenis Transaksi (1/2/3): "))

    if transaksi == "1":
        print("\n ==Tarik Tunai==")
        tarik = int(input("Masukkan Nominal Penarikan :\n Rp "))
        saldo_awal = 2410932041
        sisa_saldo = print(f"Transaksi Berhasil! Sisa Saldo Anda, Rp {saldo_awal - tarik}")
    elif transaksi == "2":
        print("\n ==Transfer==")
        tf = int(input("Masukkan Nominal Transfer :\n Rp "))
        saldo_awal = 2410932041
        sisa_saldo = print(f"Transaksi Berhasil! Sisa Saldo Anda, Rp {saldo_awal - tf}")
    elif transaksi == "3":
        print("\n ==Setor Tunai==")
        setor = int(input("Masukkan Nominal :\n Rp "))
        saldo_awal = 2410932041
        sisa_saldo = print(f"Transaksi Berhasil! Sisa Saldo Anda, Rp {saldo_awal - setor}")
    else:
        print("Jenis Transaksi Anda Tidak Tersedia!")


    while True:
        lanjut = input("\n Apakah Anda Ingin Melakukan Transaksi Lagi (Ya/Tidak) ?  ")
        
        if lanjut == "Ya":
            break
        elif lanjut == "Tidak":
            print("Transaksi Selesai! Terimakasih Telah menggunakan layanan kami! \n ")
            exit()
        else:
            print("Pilihan Anda Tidak tersedia!Terimakasih Telah menggunakan layanan kami! \n ")