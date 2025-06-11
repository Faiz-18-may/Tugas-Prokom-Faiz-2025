# Program Login
print("==== LOGIN ACCOUNT ====")

username = "Faizz ajahh"
password = "808080"

attemp = 0
limit = 3
while limit > 0:
    uname = input("Username : ")
    pw = input("Password : ")

    if username.lower() == uname.lower() and password == pw:
        print("Welcome!", uname)
        break
    else:
        limit -= 1
        print(f"Username or Password is Incorrect, Remaining Attemps = {limit - attemp}")
if limit == attemp:
    print("Your Login was Unseccesful! Please Try Again Later")
    exit()

print("______________________________________________________________________________________________")
# Program SK Modul 2
print("==== PROGRAM KALKULASI NILAI MATA KULIAH ====")

while True:
    nama = str(input("Nama              : "))
    nim = int(input("NIM               : "))
    matkul = str(input("Mata Kuliah       : "))
    nilai = int(input("Nilai Mata Kuliah : "))

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
        print("Anda Tidak Lulus! Silahkan mengulang tahun depan")
    elif(45 > nilai >= 0):
        print("Predikat Nilai Anda = E")
        print("Anda Tidak Lulus! Silahkan mengulang tahun depan")
    else:
        print("Pilihan Anda Tidak Tersedia")

    print("Semangat Terus Kuliahnya!")

    while True:
        next = input("Apakah Anda ingin Menginput Nilai lainnya? (y/n) : ")
        if next == "y":
            break
        elif next == "n":
            exit()
        else:
            print("Your answer is invalid")
