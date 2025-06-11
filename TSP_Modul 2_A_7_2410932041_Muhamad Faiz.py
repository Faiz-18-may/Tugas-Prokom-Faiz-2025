nama = str(input("Nama Penumpang \t\t\t\t: "))
print("Harga Tiket Rute Yang Tersedia")
print("\t - Medan \t= Rp 1.002.600")
print("\t - Jakarta \t= Rp 2.142.900")
print("\t - Batam \t= Rp 665.400")

tujuan = str(input("Pilih Rute Tujuan Anda \t\t\t: "))

PP = str(input("Pulang Pergi ? (ya/tidak) \t\t: "))

if tujuan == "Medan":
    harga1 = 1002600
    if PP == "ya":
        print("Harga Tiket Anda = Rp ", (harga1 * 2)*0.8)
        print("Selamat Menikmati Penerbangan Anda, Tn.", nama)
    elif PP == "tidak":
        print("Harga Tiket Anda = Rp ", harga1)
        print("Selamat Menikmati Penerbangan Anda, Tn.", nama)
    else:
        print("Pilihan Anda Tidak Tersedia!")

elif tujuan == "Jakarta":
    harga2 = 2142900
    if PP == "ya":
        print("Harga Tiket Anda = Rp ", (harga2 * 2)*0.8)
        print("Selamat Menikmati Penerbangan Anda, Tn.", nama)
    elif PP == "tidak":
        print("Harga Tiket Anda = Rp ", harga2)
        print("Selamat Menikmati Penerbangan Anda, Tn.", nama)
    else:
        print("Pilihan Anda Tidak Tersedia!")

elif tujuan == "Batam":
    harga3 = 665400
    if PP == "ya":
        print("Harga Tiket Anda = Rp ", (harga3 * 2)*0.8)
        print("Selamat Menikmati Penerbangan Anda, Tn.", nama)
    elif PP == "tidak":
        print("Harga Tiket Anda = Rp ", harga3)
        print("Selamat Menikmati Penerbangan Anda, Tn.", nama)
    else:
        print("Pilihan Anda Tidak Tersedia!")

else:
    print("Pilihan Anda Tidak Tersedia!")
