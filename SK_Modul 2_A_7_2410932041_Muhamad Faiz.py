#Program Menghitung Nilai MataKuliah

nama = str(input("Nama \t\t\t: "))
nim = int(input("NIM \t\t\t: "))
matkul = str(input("MataKuliah \t\t: "))
nilai = int(input("Nilai MataKuliah \t: "))

if(100 >= nilai >= 80):
    print("Predikat nilai Anda = A")
    print("Anda Lulus!")
elif(80 > nilai >= 75):
    print("Predikat Nilai Anda = A-")
    print("Anda Lulus!")
elif(75 > nilai >= 70):
    print("Predikat Nilai Anda = B+")
    print("Anda Lulus!")
elif(70 > nilai >= 65):
    print("Predikat Nilai Anda = B")
    print("Anda Lulus!")
elif(65 > nilai >= 60):
    print("Predikat Nilai Anda = B-")
    print("Anda Lulus!")
elif(60 > nilai >= 55):
    print("Predikat Nilai Anda = C+")
    print("Anda Lulus!")
elif(55 > nilai >= 50):
    print("Predikat Nilai Anda = C")
    print("Anda Lulus!")
elif(50 > nilai >= 45):
    print("Predikat Nilai Anda = D")
    print("Anda Tidak Lulus! Silahkan mengulang tahun depan:)")
elif(45 > nilai >= 0):
    print("Predikat Nilai Anda = E")
    print("Anda Tidak Lulus! Silahkan mengulang tahun depan:)")
else:
    print("Pilihan Anda Tidak Tersedia")

print("Semangat Terus Kuliahnya!")