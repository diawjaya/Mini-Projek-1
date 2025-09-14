# Mini-Projek-1
Dhiyya Rizky Akhmad Wijaya
2509116042

# Program Sistem Penyortiran Paket Berdasarkan Berat

Program sederhana berbasis Phyton untuk menyortir paket berdasarkan berat

# Alur Program

## Home Page
> Homepage akan ditampilkan saat program pertama kali dijalankan dan menampilkan semua opsi yang tersedia

User bisa mengetik input nomor untuk memilih, jika opsi tidak tersedia maka akan menampilkan "Menu Tidak Tersedia"

<img width="167" height="105" alt="Screenshot 2025-09-14 213527" src="https://github.com/user-attachments/assets/95851f2f-8dcc-45bd-b5d3-b811db7541c4" />
<img width="261" height="47" alt="wada" src="https://github.com/user-attachments/assets/e4ed8d49-3969-423b-b5e0-535bb087ffa1" />

## Opsi Tambah
> Untuk menambah barang baru kedalam list

1. Input Berat barang
2. Input Nama barang
3. Menampilkan "Barang Dimasukan"
4. Jika barang melebihi berat 50 kg maka barang tidak akan dimasukkan

<img width="187" height="85" alt="Screenshot 2025-09-14 214022" src="https://github.com/user-attachments/assets/8cfbcc8f-03e2-43c4-9c6c-b5509697a6a8" />
<img width="183" height="63" alt="dwada" src="https://github.com/user-attachments/assets/769f4ee3-1628-4a10-9890-006be97d5681" />

## Opsi Hapus
> Untuk menghapus barang yang sudah ada di dalam list

1. Input Berat barang
2. Input Nama barang
3. Jika barang ada di dalam list maka barang akan dihapus
4. Menampilkan "Barang Diambil"
5. Jika barang tidak ada maka akan menampilkan "Barang Tidak ada"

<img width="195" height="91" alt="Screenshot 2025-09-14 215115" src="https://github.com/user-attachments/assets/8343e656-ad3f-415b-882c-6a5b4952dc72" />
<img width="186" height="87" alt="Screenshot 2025-09-14 215809" src="https://github.com/user-attachments/assets/7604422b-7922-4360-a7d9-6a3049820011" />

## Opsi List Paket
> Untuk melihat semua list paket yang sudah dimasukan berdasarkan kategori berat

<img width="732" height="45" alt="dwa" src="https://github.com/user-attachments/assets/5df31f51-1d56-45a4-b307-3bc0423867b6" />

## Opsi Keluar

> Untuk menghentikan loop dan keluar dair program

<img width="588" height="71" alt="adada" src="https://github.com/user-attachments/assets/42a97818-065d-4814-ba2c-ac8893efd8b9" />

# Penjelasan Code
> List dan Menu
``` python
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
```

Variable berupa list yang berisi elemen nama barang yang dibedakan berdasarkan berat, kemudian menjalankan infinite loop agar menampilkan menu terus menerus hingga user memilih Quit

> Menu Masukkan barang
``` python
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
```
Untuk menginput berat barang dalam float agar menentukan barang masuk ke list apa, kemudian menginput nama barang dan memasukan ke dalam list lalu menampilkan '[Barang Dimasukan]'. Jika barang lebih dari 50kg maka barang tidak dimasukkan dan menampilkan '[Barang keberatan]'

> Menu Mengambil barang
``` python
    elif menu == '2':
        barang =float(input('Beratnya (kg)= '))
        if barang <= 5:
            adi5kg = input("Nama barang = ")
            if adi5kg in d5:
                d5.remove(adi5kg)
                print('[Barang Diambil]')
            else:
                adi5kg not in d5
                print('Barang tidak ada')
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
```

ntuk menginput berat barang dalam float agar menentukan barang masuk ke list apa, kemudian menginput nama barang dan me remove barang dari list lalu menampilkan '[Barang Diambil]', jika barang tidak ada maka akan menampilkan'Barang tidak ada' . Jika barang lebih dari 50kg maka barang tidak diambil dan menampilkan Error

> Menu List paket
``` python
    elif menu == '3':
        print(" <= 5kg : ",d5," <= 10kg : ",d10," <= 25kg : ",d25," <= 50kg : ",d50)
```
Menampilkan semua list dan barang yang sudah dimasukkan

> Menu Quit
``` python
    elif menu == '4':
        print("Dadah ( *・∀・)ノ゛")
        break
```
Saat memilih keluar, Menampilkan pesan Dadah dan menghentikan loop dengan break

``` python
    else:
        print('[Error, Menu tidak tersedia]')
```
Menampilkan Error saat menu tidak valid dan menampilkan ulang menu utama

# Flochart

<img width="2019" height="1240" alt="as drawio" src="https://github.com/user-attachments/assets/cc831159-5f1c-4cea-a166-f9145ec2a996" />
