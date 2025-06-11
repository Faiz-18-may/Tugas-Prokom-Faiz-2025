class Buku:
    def __init__(self, jenis, harga, warna, stok):
        self.jenis = jenis
        self.harga = harga
        self.warna = warna
        self.stok = stok

    def info_buku(self):
        print(f"Jenis Buku    : {self.jenis}")
        print(f"Harga         : Rp {self.harga}")
        print(f"Warna Sampul  : {self.warna}")
        print(f"Stok Tersedia : {self.stok}")
        print("______________________________")

class LSIKbookstore:
    def __init__(self):
        self.daftar_buku = [
            Buku("Novel", 75000, "Putih", 10),
            Buku("Pendidikan", 50000, "Putih", 15),
            Buku("Biografi", 35000, "Kuning", 20)
        ]
        self.daftar_awal = [Buku(b.jenis, b.harga, b.warna, b.stok) for b in self.daftar_buku]


    def tampilkan_buku(self):
        print("\n ===== DAFTAR BUKU AWAL =====")
        for buku in self.daftar_buku:
            buku.info_buku()


    def tambah_buku(self):
        Jenis = input("\nMasukkan jenis buku   : ")
        for buku in self.daftar_buku:
            if buku.jenis == Jenis:
                print(f" Buku '{Jenis}' sudah ada dalam daftar.")
                return
        Harga = int(input("Masukkan harga buku   : "))
        Sampul = input("Masukkan warna sampul : ")
        Stok = int(input("Masukkan jumlah stok  : "))
        
        buku_baru = Buku(Jenis, Harga, Sampul, Stok)

        self.daftar_buku.append(buku_baru)
        print(" Buku berhasil ditambahkan!")


    def hapus_buku(self):
        self.tampilkan_buku()
        indeks = int(input("\nMasukkan nomor buku yang ingin dihapus : ")) - 1
        if 0 <= indeks < len(self.daftar_buku):
            hapus_buku = self.daftar_buku[indeks]
            self.daftar_buku.pop(indeks)
            print(f" Buku '{hapus_buku.jenis}' berhasil dihapus.")
        else:
            print(" Mohon masukkan nomor buku yang valid!")


    def cari_buku(self):
        cari = input("\nMasukkan pencarian (jenis atau warna) : ")
        hasil = []
        for buku in self.daftar_buku:
            if cari == buku.jenis or cari.lower() == buku.warna.lower():
                hasil.append(buku)

        if hasil:
            print("<<< Hasil Pencarian >>>")
            for buku in hasil:
                buku.info_buku()
        else:
            print(" Buku tidak ditemukan.")


    def banding_data(self):
        print("\n ===== DAFTAR BUKU AWAL =====")
        for buku in self.daftar_awal:
            buku.info_buku()

        print("\n ===== DAFTAR BUKU TERBARU =====")
        for buku in self.daftar_buku:
            buku.info_buku()

toko = LSIKbookstore()
while True:
    print("\n<<<< MENU LSIK's BOOKSTORE >>>>")
    print(" 1. Tampilkan Daftar Buku")
    print(" 2. Tambah Buku")
    print(" 3. Hapus Buku")
    print(" 4. Cari Buku")
    print(" 5. Perbandingan Data Awal dan Terbaru")
    print(" 6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        toko.tampilkan_buku()
    elif pilihan == "2":
        toko.tambah_buku()
    elif pilihan == "3":
        toko.hapus_buku()
    elif pilihan == "4":
        toko.cari_buku()
    elif pilihan == "5":
        toko.banding_data()
    elif pilihan == "6":
        print("\n Terima kasih telah menggunakan program LSIK's BOOKSTORE.")
        break
    else:
        print(" Pilihan tidak valid. Silakan coba lagi.")