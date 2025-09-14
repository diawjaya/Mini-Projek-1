d5 = []
d10 = []
d25 = []
d50= []

while(True):
    print('1. [Masukan Paket]')
    print('2. [Ambil Paket]')
    print('3. [List Paket]')
    print('4. [Quit]')
    menu = input('Pilih menu = ')
    if menu == '1':
        berat =float(input('Beratnya (kg)= '))
        if berat <= 5:
            di5kg = input("Nama barang = ")
            d5.append(di5kg)
            print('[Barang Dimasukan]')
        elif berat <= 10:
            di10kg = input("Nama barang = ")
            d10.append(di10kg)
            print('[Barang Dimasukan]')
        elif berat <= 25:
            di25kg = input("Nama barang = ")
            d25.append(di25kg)
            print('[Barang Dimasukan]')
        elif berat <= 50:
            dia50kg = input("Nama barang = ")
            d50.append(dia50kg)
            print('[Barang Dimasukan]')
        else :
            berat > 50
            print('[Barang keberatan]')
    elif menu == '3':
        print(" <= 5kg : ",d5," <= 10kg : ",d10," <= 25kg : ",d25," <= 50kg : ",d50)
    elif menu == '2':
        barang =float(input('Beratnya (kg)= '))
        if barang <= 5:
            adi5kg = input("Nama barang = ")
            d5.remove(adi5kg)
            print('[Barang Diambil]')
        elif barang <= 10:
            adi10kg = input("Nama barang = ")
            if adi10kg in d10:
                d10.remove(adi10kg)
                print('[Barang Diambil]')
            else:
                adi10kg not in d10
                print('Barang tidak ada')
        elif barang <= 25:
            adi25kg = input("Nama barang = ")
            if adi25kg in d25:
                d25.remove(adi25kg)
                print('[Barang Diambil]')
            else:
                adi25kg not in d25
                print('Barang tidak ada')
        elif barang <= 50:
            adia50kg = input("Nama barang = ")
            if adia50kg in d50:
                d50.remove(adia50kg)
                print('[Barang Diambil]')
            else:
                adia50kg not in d50
                print('Barang tidak ada')
        else:
            barang > 50
            print('[Error]')
    elif menu == '4':
        print("Dadah ( *・∀・)ノ゛")
        break
    else:
        print('[Error, Menu tidak tersedia]')