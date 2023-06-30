#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

class Bangun:
    def hitung_luas(self):
        pass

class Trapesium(Bangun):
    def hitung_luas(self):
        a = float(input("Masukkan panjang sisi atas: "))
        b = float(input("Masukkan panjang sisi bawah: "))
        t = float(input("Masukkan tinggi: "))
        luas = (a + b) * t / 2
        print("Luas trapesium: ", luas)

class Lingkaran(Bangun):
    def hitung_luas(self):
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas = math.pi * r**2
        print("Luas lingkaran: ", luas)

class Balok(Bangun):
    def hitung_luas(self):
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        t = float(input("Masukkan tinggi: "))
        luas = 2 * (p*l + p*t + l*t)
        print("Luas balok: ", luas)

class Segitiga(Bangun):
    def hitung_luas(self):
        a = float(input("Masukkan panjang alas: "))
        t = float(input("Masukkan tinggi: "))
        luas = 0.5 * a * t
        print("Luas segitiga: ", luas)

class PersegiPanjang(Bangun):
    def hitung_luas(self):
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        luas = p * l
        print("Luas persegi panjang: ", luas)

class Persegi(Bangun):
    def hitung_luas(self):
        s = float(input("Masukkan panjang sisi: "))
        luas = s**2
        print("Luas persegi: ", luas)

# Fungsi utama
def main():
    print("Program Menghitung Luas Bangun\n")
    print("Pilih bangun yang ingin dihitung luasnya:")
    print("1. Trapesium")
    print("2. Lingkaran")
    print("3. Balok")
    print("4. Segitiga")
    print("5. Persegi Panjang")
    print("6. Persegi")

    pilihan = int(input("Masukkan pilihan (1-6): "))

    if pilihan == 1:
        bangun = Trapesium()
        bangun.hitung_luas()
    elif pilihan == 2:
        bangun = Lingkaran()
        bangun.hitung_luas()
    elif pilihan == 3:
        bangun = Balok()
        bangun.hitung_luas()
    elif pilihan == 4:
        bangun = Segitiga()
        bangun.hitung_luas()
    elif pilihan == 5:
        bangun = PersegiPanjang()
        bangun.hitung_luas()
    elif pilihan == 6:
        bangun = Persegi()
        bangun.hitung_luas()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()


# In[ ]:




