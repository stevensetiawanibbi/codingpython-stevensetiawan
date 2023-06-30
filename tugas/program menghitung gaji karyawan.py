#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hitung_gaji_pokok(golongan):
    if golongan == "A":
        gaji_pokok = 10000000
    elif golongan == "B":
        gaji_pokok = 7000000
    elif golongan == "C":
        gaji_pokok = 5000000
    elif golongan == "D":
        gaji_pokok = 3000000
    else:
        gaji_pokok = 0

    return gaji_pokok

def hitung_gaji_total(golongan, jam_kerja):
    gaji_pokok = hitung_gaji_pokok(golongan)

    if jam_kerja <= 40:
        gaji_total = gaji_pokok
    else:
        gaji_lembur = (jam_kerja - 40) * (gaji_pokok / 40) * 1.5
        gaji_total = gaji_pokok + gaji_lembur

    return gaji_total

# Fungsi utama
def main():
    print("Program Menghitung Gaji Karyawan\n")

    while True:
        golongan = input("Masukkan golongan (A/B/C/D): ")
        jam_kerja = int(input("Masukkan jumlah jam kerja per bulan: "))

        gaji_total = hitung_gaji_total(golongan, jam_kerja)
        print("Gaji Pokok: Rp.", hitung_gaji_pokok(golongan))
        print("Gaji Total: Rp.", gaji_total)

        ulangi = input("Apakah ingin menghitung gaji karyawan lagi? (y/n): ")
        if ulangi.lower() != "y":
            break

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




