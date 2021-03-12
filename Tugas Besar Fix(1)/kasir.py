import csv
import os

namaFile = 'ayam.csv'

def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('username kasir : ')
    import getpass
    password = getpass.getpass()
    if username == 'admin' and password == 'adminpass' :
        print('login berhasil...\n\n')
        menu()
    else:
        print('login gagal coba lagi..')
        get_login()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()

    print("=" * 62)
    print("**** WELCOME TO FILAI's CHICKENS and MILKSHAKE RESTAURANT ****")
    print("=" * 62)
    print("=" * 23, " Menu Pilihan ", "=" * 23)
    print("[1] Pemesanan Makanan dan Minuman")
    print("[2] Daftar Pesanan")
    print("[3] Hapus Pesanan")
    print("[0] Exit")
    print("-" * 62)
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        pemesananmakanandanminuman()
    elif(selected_menu == "2"):
        daftarpesanan()
    elif(selected_menu == "3"):
        hapuspesanan()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu()

def menumakanan() :
    print("\n")
    print("=" * 18, " M E N U  M A K A N A N  d a n  M I N U M A N ", "=" * 18)
    print("-" * 85)
    print("  Jenis Ayam \t   Harga \t\t\t Minuman \t\t   Harga")
    print("-" * 85)
    print("Ayam Goreng \t Rp. 15000 \t|\t Milkshake Chocolate \t\t Rp. 9000")
    print("Ayam Bakar \t Rp. 15000 \t|\t Milkshake Strawberry \t\t Rp. 9000")
    print("Ayam Betutu \t Rp. 15000 \t|\t Milkshake Vanilla \t\t Rp. 9000")
    print("Ayam Panggang \t Rp. 15000 \t|\t Milkshake Capuccino \t\t Rp. 9000")
    print("Ayam Kecap \t Rp. 15000 \t|\t Milkshake Banana \t\t Rp. 9000")
    print("Ayam Geprek \t Rp. 17000 \t|\t Milkshake Tiramisu \t\t Rp. 9000")
    print("Ayam Rica-Rica \t Rp. 18000 \t|\t Milkshake Caramel \t\t Rp. 9000")
    print("Ayam Taliwang \t Rp. 18000 \t|\t Milkshake Green Tea \t\t Rp. 9000")
    print("-" * 85)
    print("Silahkan Input Makanan dan Minuman yang Akan Dipesan")
    print("-" * 85)

def pemesananmakanandanminuman():
    list_pesanan = []
    clear_screen()
    menumakanan()
    total = 0

    command = input("Pilihan(pesan/selesai):\n")

    while True :
        if command == "pesan" :
            dict_baru = dict()
            jenisAyam = input("Masukkan jenis ayam : ")
            hargaMakanan = int(input("Masukkan harga : Rp. "))
            porsi = int(input("Porsi : "))
            totalMakanan = hargaMakanan * porsi
            total += totalMakanan

            minuman = input("Masukkan minuman : ")
            hargaMinuman = int(input("Masukkan harga : Rp. "))
            gelas = int(input("Berapa gelas : "))
            totalMinuman = hargaMinuman * gelas
            total += totalMinuman
            print("-" * 85)
            print("Total Harga Makanan : ", totalMakanan) 
            print("Total Harga Minuman : ", totalMinuman)
            print("\n")
            dict_baru["Jenis Ayam"] = jenisAyam 
            dict_baru["Harga Makanan"] = hargaMakanan
            dict_baru["Porsi"] = porsi
            dict_baru["Total Harga Makanan"] = totalMakanan
            dict_baru["Minuman"] = minuman
            dict_baru["Harga Minuman"] = hargaMinuman
            dict_baru["Gelas"] = gelas
            dict_baru["Total Harga Minuman"] = totalMinuman
            dict_baru["Total Harga Keseluruhan"] = total
            list_pesanan.append(dict_baru)

        elif command == 'selesai' :
            print("-" * 85)
            print("Total Harga Keseluruhan : ",format(total))
            print("-" * 85)
            daftar = ["Jenis Ayam", "Harga Makanan", "Porsi", "Total Harga Makanan", "Minuman", "Harga Minuman", "Gelas", "Total Harga Minuman", "Total Harga Keseluruhan"]
            for data in list_pesanan:
                with open(namaFile, 'a', newline="\n") as file: 
                    writer = csv.DictWriter(file, fieldnames=daftar)
                    writer.writerow(data)
            back_to_menu()
            break

        else:
            print("Inputan Yang Anda Masukkan Salah!!!")
            input("Tekan Enter Untuk Lanjut...")
            pemesananmakanandanminuman()
        print("-" * 85)

        

        

        command = input('Apakah ada yang dipesan lagi(pesan/selesai)? : ')


def hapuspesanan():
    clear_screen()

    daftar = ["Jenis Ayam", "Harga Makanan", "Porsi", "Total Harga Makanan", "Minuman", "Harga Minuman", "Gelas", "Total Harga Minuman", "Total Harga Keseluruhan"]

    dataPembelian = []

    with open(namaFile, "r") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            dataPembelian.append(row)

    print("=" * 65, " D E T A I L   P E S A N A N ", "=" * 65)
    print("=" * 161)
    print("Jenis Ayam \t| Harga Makanan | Porsi |  Total Harga Makanan  |\t Minuman \t| Harga Minuman | Gelas |  Total Harga Minuman  | Total Harga Keseluruhan")
    print("=" * 161)

    for data in dataPembelian:
         print(f'{data["Jenis Ayam"]} \t| {data["Harga Makanan"]} \t|   {data["Porsi"]} \t|\t {data["Total Harga Makanan"]}\t\t| {data["Minuman"]} \t| {data["Harga Minuman"]} \t\t|   {data["Gelas"]} \t|\t {data["Total Harga Minuman"]}\t\t|\t {data["Total Harga Keseluruhan"]}')
    print("=" * 161)     
    
    pesananYangdihapus = input("Masukkan jenis ayam yang ingin dihapus : ")
    list_penampung = []

    with open(namaFile, 'r') as file:   
        reader = csv.DictReader(file, delimiter=',')
        for data in reader :  
            if data["Jenis Ayam"] == pesananYangdihapus :
                continue 
            else :
                list_penampung.append(data)

    with open(namaFile, 'w', newline='') as file: 
        writer = csv.DictWriter(file, fieldnames=daftar)
        writer.writeheader()
        writer.writerows(list_penampung)

    print("-" * 56)
    print("\n")
    print("Data yang anda pilih berhasil dihapus!")
    back_to_menu()

def daftarpesanan():
    clear_screen()      
    dataPembelian= []  
    with open(namaFile, "r", newline='') as file:  
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            dataPembelian.append(row)

        labels = dataPembelian.pop(0)

        print("=" * 63, " D E T A I L   T R A N S A K S I ", "=" * 63)
        print("=" * 161)
        print(f'{labels[0]} \t| {labels[1]} | {labels[2]} |  {labels[3]}  |\t {labels[4]} \t| {labels[5]} | {labels[6]} |  {labels[7]}  | {labels[8]}')
        print("=" * 161)
        for i in dataPembelian:
            print(f'{i[0]} \t| {i[1]} \t|   {i[2]} \t|\t {i[3]}\t\t| {i[4]} \t| {i[5]} \t\t|   {i[6]} \t|\t {i[7]}\t\t|\t {i[8]}')
        print("=" * 161)
    back_to_menu()

if __name__=='__main__':
    get_login()