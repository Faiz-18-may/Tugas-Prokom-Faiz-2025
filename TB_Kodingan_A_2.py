from tabulate import tabulate
from termcolor import colored

## Program 1: Menghitung Emisi Karbon Konsumen Rumah Tangga
class EmisiKarbonKonsumen:
    def __init__(self, listrik_konsumen, bensin_konsumen, solar_konsumen):
        self.listrik_konsumen = listrik_konsumen
        self.bensin_konsumen = bensin_konsumen
        self.solar_konsumen = solar_konsumen

    def hitung_emisi(self):
        # Faktor Emisi
        faktor_emisi_kosnsumen = {
            'listrik': 0.891,   # kg CO2 per KWh
            'bensin': 2.4,      # kg CO2 per liter
            'solar': 2.65       # kg CO2 per liter
        }

        # Perhitungan Emisi
        emisi_listrik_konsumen = self.listrik_konsumen * faktor_emisi_kosnsumen['listrik']
        emisi_bensin_konsumen = self.bensin_konsumen * faktor_emisi_kosnsumen['bensin']
        emisi_solar_konsumen = self.solar_konsumen * faktor_emisi_kosnsumen['solar']
        total_emisi_konsumen = emisi_listrik_konsumen + emisi_bensin_konsumen + emisi_solar_konsumen

        return emisi_listrik_konsumen, emisi_bensin_konsumen, emisi_solar_konsumen, total_emisi_konsumen

    def kategori_emisi_penduduk(self, total_emisi_konsumen):
        if total_emisi_konsumen <= 133:
            kategori = "🟢 HIJAU (Ideal)"
            rekomendasi_konsumen = [
                "Pertahankan gaya hidup ramah lingkungan yang sudah diterapkan.",
                "Pakai energi terbarukan seperti panel surya untuk lebih mengurangi jejak karbon.",
                "Terus gunakan peralatan listrik yang hemat energi dan perhatikan pola konsumsi listrik.",
                "Gunakan kendaraan listrik atau transportasi umum untuk mengurangi emisi.",
                "Teruskan kebiasaan memilah sampah dan mendaur ulang."
            ]
        elif 134 <= total_emisi_konsumen <= 267:
            kategori = "🟡 KUNING (Perlu Perhatian)"
            rekomendasi_konsumen = [
                "Kurangi konsumsi energi dengan mematikan perangkat yang tidak digunakan.",
                "Gunakan kendaraan yang lebih efisien bahan bakarnya atau kendaraan listrik.",
                "Mulailah mengeksplorasi opsi energi terbarukan seperti panel surya.",
                "Pertimbangkan untuk menggunakan transportasi umum lebih sering.",
                "Periksa kembali rute perjalanan dan frekuensi penggunaan kendaraan."
            ]
        else:
            kategori = "🔴 MERAH (Berlebihan)"
            rekomendasi_konsumen = [
                "Beralih ke energi terbarukan seperti panel surya untuk rumah tangga.",
                "Investasikan pada peralatan yang lebih efisien energi dan matikan perangkat elektronik yang tidak digunakan.",
                "Gunakan kendaraan yang lebih hemat bahan bakar atau pilih kendaraan listrik.",
                "Tingkatkan penggunaan transportasi umum atau berbagi kendaraan.",
                "Kurangi konsumsi bensin dan solar dengan memilih kendaraan efisien bahan bakar."
            ]
        return kategori, rekomendasi_konsumen

    def tampilkan_tabel(self, emisi_listrik_konsumen, emisi_bensin_konsumen, emisi_solar_konsumen, total_emisi_konsumen, kategori):
        tabel_data = [
            [emisi_listrik_konsumen, emisi_bensin_konsumen, emisi_solar_konsumen, total_emisi_konsumen, kategori]
        ]
        headers = ["Emisi Listrik (kg CO2)", "Emisi Bensin (kg CO2)", "Emisi Solar (kg CO2)", "Emisi Total (kg CO2)", "Kategori"]
        print(colored("\n=== Hasil Perhitungan Emisi Karbon Rumah Tangga ===", "blue"))
        print(tabulate(tabel_data, headers=headers, tablefmt="grid"))

## Program 2: Pengelolaan Lokasi dan Data Lingkungan Pemerintah
class PerhitunganLokasi:
    def __init__(self, nama):
        self.nama = nama
        self.emisi = 0
        self.emisi_per_kapita = 0
        self.kategori_emisi_penduduk = ""
        self.wqi = 0
        self.kategori_air = ""
        self.skor_kebakaran = 0
        self.risiko_kebakaran = ""

    def hitung_emisi(self, bbm, listrik, limbah, penduduk):
        faktor_emisi_bbm = 2.31
        faktor_emisi_listrik = 0.85
        faktor_emisi_limbah = 1.2

        emisi_bbm = bbm * faktor_emisi_bbm / 1000
        emisi_listrik_konsumen = listrik * faktor_emisi_listrik / 1000
        emisi_limbah = limbah * faktor_emisi_limbah
        self.emisi = emisi_bbm + emisi_listrik_konsumen + emisi_limbah
        self.emisi_per_kapita = self.emisi / penduduk if penduduk > 0 else 0

        if self.emisi_per_kapita < 2:
            self.kategori_emisi_penduduk = "Baik"
        elif self.emisi_per_kapita <= 5:
            self.kategori_emisi_penduduk = "Sedang"
        else:
            self.kategori_emisi_penduduk = "Tinggi"

    def hitung_wqi(self, pH, DO, BOD):
        skor_pH = 90 if 6.5 <= pH <= 8.5 else 70 if 5.5 <= pH <= 9.5 else 40
        skor_DO = 90 if DO >= 7 else 70 if DO >= 5 else 40
        skor_BOD = 90 if BOD <= 3 else 70 if BOD <= 5 else 40

        self.wqi = round(skor_pH * 0.3 + skor_DO * 0.4 + skor_BOD * 0.3, 2)

        if self.wqi >= 90:
            self.kategori_air = "Sangat Baik"
        elif self.wqi >= 70:
            self.kategori_air = "Baik"
        elif self.wqi >= 50:
            self.kategori_air = "Cukup"
        elif self.wqi >= 25:
            self.kategori_air = "Buruk"
        else:
            self.kategori_air = "Sangat Buruk"

    def potensi_kebakaran(self, suhu, hujan, kelembaban, angin, vegetasi, aktivitas):
        skor_suhu = 5 if suhu >= 35 else 4 if suhu >= 30 else 3 if suhu >= 25 else 2 if suhu >= 20 else 1
        skor_hujan = 5 if hujan < 1 else 4 if hujan < 5 else 3 if hujan < 10 else 2 if hujan < 20 else 1
        skor_kelembaban = 5 if kelembaban < 20 else 4 if kelembaban < 40 else 3 if kelembaban < 60 else 2 if kelembaban < 80 else 1
        skor_angin = 5 if angin > 40 else 4 if angin > 30 else 3 if angin > 20 else 2 if angin > 10 else 1

        total = skor_suhu + skor_hujan + skor_kelembaban + \
            skor_angin + vegetasi + aktivitas
        self.skor_kebakaran = total

        if total >= 26:
            self.risiko_kebakaran = "Sangat Tinggi"
        elif total >= 21:
            self.risiko_kebakaran = "Tinggi"
        elif total >= 15:
            self.risiko_kebakaran = "Sedang"
        else:
            self.risiko_kebakaran = "Rendah"

# Kelas untuk Menu Pemerintah
class MenuPemerintah:
    def __init__(self):
        self.lokasi_list = []

    def daftar_lokasi(self):
        if not self.lokasi_list:
            print(colored("\nTidak ada data lokasi yang tersedia.", "magenta"))
            return
        print(colored("\n=== Daftar Lokasi ===", "blue"))
        
        tabel_data = []

        for i in range(len(self.lokasi_list)):
            lokasi = self.lokasi_list[i]
            tabel_data.append([
                i + 1,
                lokasi.nama, 
                f"{lokasi.emisi:.2f} ton CO2 ({lokasi.kategori_emisi_penduduk})", 
                f"WQI {lokasi.wqi} ({lokasi.kategori_air})", 
                f"Skor {lokasi.skor_kebakaran} ({lokasi.risiko_kebakaran})"
            ])

        headers = ["No", "Daftar Lokasi", "Emisi Karbon", "Kualitas Sumber Air", "Potensi Kebakaran"]
        print(tabulate(tabel_data, headers=headers, tablefmt="grid"))

    def rekomendasi(self):
        if not self.lokasi_list:
            print(colored("Silakan tambah lokasi terlebih dahulu.", "magenta"))
            return

        while True:
            try:
                no = int(input("\nMasukkan nomor lokasi yang ingin dilihat rekomendasi (0 untuk kembali): "))
                if no == 0:
                    return
                if 1 <= no <= len(self.lokasi_list):
                    lokasi_terpilih = self.lokasi_list[no-1]
                    self.tampilkan_rekomendasi_lokasi(lokasi_terpilih)
                else:
                    print(colored("Lokasi tidak ditemukan.", "magenta"))
                break
            except ValueError:
                print(colored("Input harus berupa angka.", "red"))

    def tampilkan_rekomendasi_emisi(self, kategori_emisi_penduduk):
        if kategori_emisi_penduduk == "Baik":
            rekomendasi_emisi = [
                "Pertahankan gaya hidup ramah lingkungan yang sudah diterapkan.",
                "Lanjutkan penggunaan energi terbarukan dan efisien.",
                "Perbanyak kampanye pengurangan emisi karbon kepada masyarakat."
            ]
        elif kategori_emisi_penduduk == "Sedang":
            rekomendasi_emisi = [
                "Kurangi konsumsi energi dan gunakan teknologi yang lebih efisien.",
                "Perbanyak penggunaan transportasi umum atau kendaraan listrik.",
                "Mulai beralih ke sumber energi terbarukan."
            ]
        else: 
            rekomendasi_emisi = [
                "Segera beralih ke energi terbarukan seperti panel surya.",
                "Gunakan kendaraan listrik dan perbaiki efisiensi energi di sektor industri.",
                "Tingkatkan kesadaran masyarakat tentang pentingnya pengurangan emisi."
            ]
        
        print(colored("\n=== Rekomendasi Emisi Karbon ===", "cyan"))
        for i in rekomendasi_emisi:
            print(f">> {i}")

    def tampilkan_rekomendasi_kualitas_air(self, kategori_air):
        if kategori_air == "Sangat Baik":
            rekomendasi_air = [
                "Pertahankan kualitas air yang baik dengan pengelolaan yang bijaksana.",
                "Perbanyak konservasi dan restorasi sumber daya air.",
                "Penyuluhan kepada masyarakat agar tidak mencemari sumber air."
            ]
        elif kategori_air == "Baik":
            rekomendasi_air = [
                "Perbaiki sistem pengolahan air dan pengawasan kualitasnya.",
                "Perbanyak program penanaman pohon di sekitar sumber air.",
                "Lakukan pemantauan kualitas air secara rutin."
            ]
        elif kategori_air == "Cukup":
            rekomendasi_air = [
                "Segera lakukan peningkatan kualitas air melalui teknologi filtrasi.",
                "Kurangi pencemaran dengan pengelolaan limbah yang lebih baik.",
                "Perbanyak edukasi untuk menjaga kebersihan sumber air."
            ]
        elif kategori_air == "Buruk":
            rekomendasi_air = [
                "Lakukan pengolahan air secara intensif untuk mengurangi polusi.",
                "Perbaiki sanitasi dan sistem drainase untuk menghindari pencemaran.",
                "Segera buat kebijakan pengelolaan air yang berkelanjutan."
            ]
        else: 
            rekomendasi_air = [
                "Segera lakukan pemulihan total terhadap sumber daya air.",
                "Perbanyak pembangunan fasilitas pengolahan air bersih.",
                "Lakukan upaya pemulihan ekosistem sungai atau danau yang tercemar."
            ]
        
        print(colored("\n=== Rekomendasi Kualitas Sumber Air ===", "cyan"))
        for i in rekomendasi_air:
            print(f">> {i}")

    def tampilkan_rekomendasi_potensi_kebakaran(self, risiko_kebakaran):
        if risiko_kebakaran == "Sangat Tinggi":
            rekomendasi_kebakaran = [
                "Segera lakukan upaya pencegahan kebakaran dengan membatasi aktivitas di area rawan.",
                "Bangun sistem deteksi dini kebakaran dan pelatihan untuk warga.",
                "Bersihkan vegetasi yang mudah terbakar dan kelola lahan dengan bijak."
            ]
        elif risiko_kebakaran == "Tinggi":
            rekomendasi_kebakaran = [
                "Lakukan pemantauan cuaca dan suhu secara rutin untuk deteksi dini.",
                "Pertahankan jalur evakuasi yang jelas dan mudah diakses.",
                "Perbanyak penyuluhan kepada masyarakat untuk mencegah kebakaran."
            ]
        elif risiko_kebakaran == "Sedang":
            rekomendasi_kebakaran = [
                "Sediakan akses air yang memadai untuk pencegahan kebakaran.",
                "Jaga kebersihan hutan dan lahan dari bahan yang mudah terbakar.",
                "Lakukan patroli di area rawan kebakaran."
            ]
        else:  # risiko_kebakaran == "Rendah"
            rekomendasi_kebakaran = [
                "Tetap waspada dan awasi area yang memiliki potensi kebakaran.",
                "Lakukan pengelolaan lahan secara berkelanjutan untuk mengurangi potensi kebakaran."
            ]
        
        print(colored("\n=== Rekomendasi Potensi Kebakaran ===", "cyan"))
        for i in rekomendasi_kebakaran:
            print(f">> {i}")

    def tampilkan_rekomendasi_lokasi(self, lokasi):
        print(colored(f"\n=== Rekomendasi untuk Lokasi: {lokasi.nama} ===", "yellow"))
        self.tampilkan_rekomendasi_emisi(lokasi.kategori_emisi_penduduk)
        self.tampilkan_rekomendasi_kualitas_air(lokasi.kategori_air)
        self.tampilkan_rekomendasi_potensi_kebakaran(lokasi.risiko_kebakaran)

    def tambah_lokasi(self):
        print(colored("\n=== Tambah Lokasi ===", "blue"))
        nama = input("\nMasukkan nama lokasi : ")
        l = PerhitunganLokasi(nama)

        # Emisi Karbon
        print(colored("\n-- Data Emisi Karbon --", "cyan"))
        while True:
            try:
                bbm = float(input("Konsumsi BBM per tahun (liter)   : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                listrik = float(input("Konsumsi listrik per tahun (kWh) : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                limbah = float(input("Volume limbah per tahun (ton)    : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                penduduk = int(input("Jumlah penduduk                  : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))
        
        l.hitung_emisi(bbm, listrik, limbah, penduduk)

        # Kualitas Air
        print(colored("\n-- Data Kualitas Sumber Air --", "cyan"))
        while True:
            try:
                pH = float(input("pH (1-14)  : "))
                
                if 1 <= pH <= 14:
                    break
                else:
                    print(colored("\nInput tidak valid. Masukkan nilai pH antara 1 sampai 14.", "red"))
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                DO = float(input("DO (mg/L)  : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                BOD = float(input("BOD (mg/L) : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        l.hitung_wqi(pH, DO, BOD)

        # Potensi Kebakaran
        print(colored("\n-- Data Potensi Kebakaran --", "cyan"))
        while True:
            try:
                suhu = float(input("Suhu udara (°C)          : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                hujan = float(input("Curah hujan (mm/hari)    : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                kelembaban = float(input("Kelembaban (%)           : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                angin = float(input("Kecepatan angin (km/jam) : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                print("\n1. Air / Tidak ada vegetasi")
                print("2. Tanah kosong")
                print("3. Padang rumput")
                print("4. Semak belukar")
                print("5. Hutan kering / Lahan gambut / Hutan tropis")
                vegetasi = int(input("Jenis vegetasi (1-5) : "))

                if 1 <= vegetasi <= 5:
                    break
                else:
                    print(colored("\nInput tidak valid. Masukkan angka antara 1 sampai 5.", "red"))
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))
                
        while True:
            try:
                print("\n1. Tidak ada aktivitas")
                print("2. Aktivitas kecil")
                print("3. Sedang")
                print("4. Tinggi")
                print("5. Sangat tinggi (pembukaan lahan, pembakaran, dll)")
                aktivitas = int(input("Aktivitas manusia (1-5): "))
        
                if 1 <= aktivitas <= 5:
                    break
                else:
                    print(colored("\nInput tidak valid. Masukkan angka antara 1 sampai 5.", "red"))
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))
                
        l.potensi_kebakaran(suhu, hujan, kelembaban, angin, vegetasi, aktivitas)

        self.lokasi_list.append(l)
        print(colored(f"\nLokasi '{nama}' berhasil ditambahkan.\n", "green"))

    def hapus_lokasi(self):
        if not self.lokasi_list:
            return
        while True:
            try:
                no = int(input("\nMasukkan nomor lokasi yang akan dihapus: "))
                if 1 <= no <= len(self.lokasi_list):
                    nama = self.lokasi_list[no-1].nama
                    del self.lokasi_list[no-1]
                    print(colored(f"Lokasi '{nama}' dihapus.", "green"))
                else:
                    print(colored("Lokasi tidak ditemukan.", "magenta"))
                break
            except ValueError:
                print(colored("Input harus berupa angka.", "red"))

    def menu(self):
        while True:
            print(colored("\n=== Menu Pemerintah ===", "blue"))
            print("1. Daftar Lokasi")
            print("2. Tambah Lokasi")
            print("3. Hapus Lokasi")
            print("4. Selesai")
            pilihan = input("Pilih menu (1-4): ")

            if pilihan == "1":
                self.daftar_lokasi()
                self.rekomendasi()
            elif pilihan == "2":                
                self.tambah_lokasi()
            elif pilihan == "3":
                self.daftar_lokasi()
                self.hapus_lokasi()
            elif pilihan == "4":
                print(colored("\nProgram selesai.", "green"))
                break
            else:
                print(colored("Pilihan tidak valid.", "red"))

class Pengguna:
    def __init__(self, jenis):
        self.jenis = jenis

    def tampilkan_menu(self):
        pass

class KonsumenRumahTangga(Pengguna):
    def __init__(self):
        self.jenis = "Konsumen Rumah Tangga"

    def tampilkan_menu(self):
        print(colored("\n=== Menu Konsumen Rumah Tangga ===", "blue"))
        username = (input("Masukkan username : "))
        print(colored(f"Selamat datang, {username}!\n", "green"))

        while True:
            try:
                listrik_konsumen = float(input("Masukkan penggunaan listrik (KWh) / bulan  : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                bensin_konsumen = float(input("Masukkan penggunaan bensin (Liter) / bulan : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        while True:
            try:
                solar_konsumen = float(input("Masukkan penggunaan solar (Liter) / bulan  : "))
                break
            except ValueError:
                print(colored("\nInput tidak valid. Pastikan memasukkan angka yang benar.", "red"))

        emisi = EmisiKarbonKonsumen(listrik_konsumen, bensin_konsumen, solar_konsumen)
        emisi_listrik_konsumen, emisi_bensin_konsumen, emisi_solar_konsumen, total_emisi_konsumen = emisi.hitung_emisi()
        kategori, rekomendasi_konsumen = emisi.kategori_emisi_penduduk(total_emisi_konsumen)
        emisi.tampilkan_tabel(emisi_listrik_konsumen, emisi_bensin_konsumen, emisi_solar_konsumen, total_emisi_konsumen, kategori)

        print(colored("\n=== Rekomendasi ===", "yellow"))
        for r in rekomendasi_konsumen:
            print(f"- {r}")

class Pemerintah(Pengguna):
    def __init__(self):
        self.jenis = "Pemerintah"

    def tampilkan_menu(self):
        print(colored("\n=== Menu Login Pemerintah ===", "blue"))
        # Username dan password Pemerintah
        valid_username = "admin"
        valid_password = "admin123"
        kesempatan = 0

        while kesempatan < 3:
            username = input("Masukkan username : ")
            password = input("Masukkan password : ")
            if username == valid_username and password == valid_password:
                print(colored("Login berhasil!", "green"))
                menu_pemerintah = MenuPemerintah()
                menu_pemerintah.menu()
                break
            else:
                kesempatan += 1
                if kesempatan < 3:
                    print(colored(f"Username atau password salah! Sisa kesempatan: {3 - kesempatan}", "red"))
                else:
                    print(colored("Kesempatan habis. Login gagal.", "red"))
                    return

class MenuLogin:
    def __init__(self):
        pass

    def login(self):
        while True:
            print(colored("\n=== Menu Login ===", "blue"))
            print("1. Konsumen Rumah Tangga")
            print("2. Pemerintah")
            print("3. Keluar")
            pilihan = input("Pilih jenis pengguna (1-3) : ")

            if pilihan == "1":
                konsumen = KonsumenRumahTangga()
                konsumen.tampilkan_menu()

                ulang = input("\nIngin login ulang? (y/n) : ")
                if ulang.lower() != 'y':
                    break

            elif pilihan == "2":
                pemerintah = Pemerintah()
                pemerintah.tampilkan_menu()

                ulang = input("\nIngin login ulang? (y/n) : ")
                if ulang.lower() != 'y':
                    break

            elif pilihan == "3":
                print(colored("\nProgram selesai.", "green"))
                break

            else:
                print(colored("Pilihan tidak valid.", "red"))

if __name__ == "__main__":
    menu_login = MenuLogin()
    menu_login.login()