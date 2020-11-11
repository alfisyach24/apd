import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Start():
    clear_screen()
    print('SELAMAT DATANG DI APLIKASI LAUNDRY')
    print('Aplikasi Jasa Laundry \n1. Laundry Kiloan \n2. Laundry Satuan \n3. Keluar')
    a = int(input('Masukan Pilihan Anda! = '))
    if a == 1 :
        hargakiloan()
        loop1()
    if a == 2 :
        hargasatuan()
        loop1()
    if a == 3:
        End()

def hargakiloan():
    clear_screen()
    print('1. Cuci Kering = Rp6.000/kg \n2. Cuci Lipat = Rp7.000/kg \n3. Setrika = Rp8.000/kg \n4. Cuci komplit = Rp10.000/kg \n5. Gorden = Rp15.000/Kg')
    pil = int(input('Masukan Pilihan Anda! = '))
    kiloan = float(input('Masukan Berapa Kilo Cucian Anda! = '))
    if pil == 1:
        harga = 6000 * kiloan
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargakiloan()
    if pil == 2:
        harga = 7000 * kiloan
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargakiloan()
    if pil == 3:
        harga = 8000 * kiloan
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargakiloan()
    if pil == 4:
        harga = 10000 * kiloan
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargakiloan()
    if pil == 5:
        harga = 15000 * kiloan
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargakiloan()

def hargasatuan():
    clear_screen()
    print('1. Jas         = Rp25.000 \n2. Jacket           = Rp25.000 \n3. BedCover         = Rp35.000 \n4. Selimut          = Rp25.000 \n5. Sepatu Kets          = Rp50.000 \n6. Sprei            = Rp28.000 \n7. Sandal           = Rp20.000 \n8. Tas          = Rp30000 \n9. Box Bayi             = Rp.200.000')
    pil = int(input('Masukan Pilihan Anda! = '))
    pcs = int(input('Masukan Berapa pcs = '))
    if pil == 1:
        harga = 25000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 2:
        harga = 25000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 3:
        harga = 35000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 4:
        harga = 25000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 5:
        harga = 50000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 6:
        harga = 28000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 7:
        harga = 20000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 8:
        harga = 30000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
    if pil == 9:
        harga = 200000 * pcs
        print('Harga Cucian Anda = Rp. %d' % (harga))
        bayar = float(input("Bayar> "))
        if bayar >= harga:
            print("Kembalian: Rp. %d" % (bayar-harga))
            print("Keterangan: Lunas")
        else:
            print("Uang anda tidak cukup!")
            time.sleep(2)
            hargasatuan()
   
def loop1() :
    answer = str(input(" Apakah Anda ingin Kembali Ke menu utama? [Ya/Tidak] "))
    if answer == ("Ya") :
        Start()
    elif answer == ("Tidak") :
        End()

def End() :
    clear_screen()
    print (" TERIMA KASIH SUDAH MENCUCI DI TEMPAT KAMI :) ")
    time.sleep(2)

Start()
