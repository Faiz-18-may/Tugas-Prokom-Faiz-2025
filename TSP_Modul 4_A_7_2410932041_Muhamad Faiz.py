# Data awal pemain dalam bentuk list of dictionaries
data_player = [
    {"Nama": "Vinicius Junior", "Umur": "24", "Durasi Kontrak": "3", "Nilai Pasar": "3.476,33"},
    {"Nama": "Rodrygo", "Umur": "24", "Durasi Kontrak": "4", "Nilai Pasar": "1.738,16"},
    {"Nama": "Arda Guler", "Umur": "19", "Durasi Kontrak": "5", "Nilai Pasar": "782,17"},
    {"Nama": "Brahim Diaz", "Umur": "25", "Durasi Kontrak": "3", "Nilai Pasar": "608,36"},
    {"Nama": "Kylian Mbappe", "Umur": "26", "Durasi Kontrak": "5", "Nilai Pasar": "2.781,06"}
]

print("<<<< DATA AWAL PEMAIN MADRID FC >>>>")
for plyr in data_player:            # Menampilkan Data Awal
    print(f"Nama Pemain     : {plyr['Nama']}")
    print(f"Umur            : {plyr['Umur']} Tahun")
    print(f"Drurasi Kontrak : {plyr['Durasi Kontrak']} Tahun")
    print(f"Nilai Pasar     : Rp {plyr['Nilai Pasar']} M")
    print("-----------------------------------")


while True:
    print("\n==== MENU DATA ====")
    print("1. Hapus Pemain")
    print("2. Tambah Pemain")
    print("3. Ubah Data Pemain")
    print("4. Keluar & Tampilkan data terbaru")
    pilihan = input(" Pilih Opsi (1-4) : ")

    if pilihan == "1":          # Pindahnya Rodrygo
        hapus_player = input("\n Masukkan nama Pemain yang akan dihapus : ")
        found = False
        for plyr in data_player:
            if plyr['Nama'] == hapus_player:
                data_player.remove(plyr)
                found = True
                print(f"Data {hapus_player}, Berhasil dihapus!")

        if not found:
            print("Data Pemain Tidak Ditemukan!")

    elif pilihan == "2":          # Masuknya Erling Haaland
        add_player = input("\n Nama Pemain yang ingin ditambahkan : ")
        umur_player = int(input(" Umur Pemain (Tahun)                : "))
        lama_kontrak = int(input(" Durasi Kontrak (Tahun)             : "))
        harga_pasar = float(input(" Harga Pasar saat ini (M)           : Rp "))

        player_baru = {
            "Nama" : add_player,
            "Umur" : umur_player,
            "Durasi Kontrak" : lama_kontrak,
            "Nilai Pasar" : harga_pasar
        }
        data_player.append(player_baru)
        print("Data Pemain Baru Berhasil ditambahkan!")
        print("======================================================")

    elif pilihan == "3":            # Perpanjangan Kontrak Vinicius Junior
        ubah_data = input("\n Pemain yang ingin diubah datanya : ")
        found = False

        for plyr in data_player:
            if ubah_data == plyr["Nama"]:
                found = True

                print("Silahkan isi data berikut.")
                umur_baru = int(input(" Umur (Tahun)           : "))
                kontrak_baru = int(input(" Durasi kontrak (Tahun) : "))
                nilai_baru = float(input(" Nilai Pasar (M)        : Rp "))

                plyr["Umur"] = umur_baru
                plyr["Durasi Kontrak"] = kontrak_baru
                plyr["Nilai Pasar"] = nilai_baru
                print(f"Data {ubah_data}, Berhasil diubah!")
                print("======================================================")

    elif pilihan == "4":            # Tampilkan Data Terbaru dan Keluar Program
        print("\n====== ====== ============================== ====== ======")
        print("<<<< DATA TEBARU PEMAIN MADRID FC >>>>")
        for plyr in data_player:
            print(f"Nama Pemain     : {plyr['Nama']}")
            print(f"Umur            : {plyr['Umur']} Tahun")
            print(f"Drurasi Kontrak : {plyr['Durasi Kontrak']} Tahun")
            print(f"Nilai Pasar     : Rp {plyr['Nilai Pasar']} M")
            print("---------------------------------------------")

        print("\nTerimakasih telah mengakses program, Sampai Jumpa Kembali!\n")
        break

    else:
        print("Pilihan Tidak Tersedia!")
