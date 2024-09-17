# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Pembagian dengan nol tidak diperbolehkan"

# Program utama
def kalkulator():
    print("Pilih Operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    # Memastikan input adalah operasi yang valid
    if pilihan in ['1', '2', '3', '4']:
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print(f"Hasil: {x} + {y} = {tambah(x, y)}")
        elif pilihan == '2':
            print(f"Hasil: {x} - {y} = {kurang(x, y)}")
        elif pilihan == '3':
            print(f"Hasil: {x} * {y} = {kali(x, y)}")
        elif pilihan == '4':
            print(f"Hasil: {x} / {y} = {bagi(x, y)}")
    else:
        print("Pilihan tidak valid!")

# Memanggil fungsi kalkulator
kalkulator()
