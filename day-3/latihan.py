print("PROGRAM MENGHITUNG LUAS DAN KELILING BANGUN DATAR")
print("BY : Tuti Nabila")


def hitung_persegi():
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print(f"Luas Persegi: {luas}")
    print(f"Keliling Persegi: {keliling}")

def hitung_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas Persegi Panjang: {luas}")
    print(f"Keliling Persegi Panjang: {keliling}")

def hitung_segitiga():
    alas = float(input("Masukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    sisi1 = float(input("Masukkan sisi pertama: "))
    sisi2 = float(input("Masukkan sisi kedua: "))
    sisi3 = float(input("Masukkan sisi ketiga: "))
    keliling = sisi1 + sisi2 + sisi3
    print(f"Luas Segitiga: {luas}")
    print(f"Keliling Segitiga: {keliling}")

def hitung_lingkaran():
    jari_jari = float(input("Masukkan jari-jari: "))
    math_pi = 3.14
    luas = math_pi * jari_jari * jari_jari
    keliling = 2 * math_pi * jari_jari
    print(f"Luas Lingkaran: {luas}")
    print(f"Keliling Lingkaran: {keliling}")

def hitung_belah_ketupat():
    diagonal1 = float(input("Masukkan diagonal pertama: "))
    diagonal2 = float(input("Masukkan diagonal kedua: "))
    luas = 0.5 * diagonal1 * diagonal2
    sisi = float(input("Masukkan panjang sisi: "))
    keliling = 4 * sisi
    print(f"Luas Belah Ketupat: {luas}")
    print(f"Keliling Belah Ketupat: {keliling}")

def main():
    while True:
        print("\n Mode Perhitungan:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Belah Ketupat")
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            hitung_persegi()
        elif pilihan == '2':
            hitung_persegi_panjang()
        elif pilihan == '3':
            hitung_segitiga()
        elif pilihan == '4':
            hitung_lingkaran()
        elif pilihan == '5':
            hitung_belah_ketupat()
        else:
            print("Pilihan tidak valid, coba lagi.")
            continue

ulangi = input("Apakah Anda ingin mengulangi perhitungan? (Ya/Tidak): ").lower()
if ulangi != 'ya':
        print("Terima kasih telah menggunakan program ini.")
        "break"

if __name__ == "__main__":
    main()