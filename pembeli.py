data =   {
        "user_id":0,
        "username": "Zutto",
        "password": "password123",
        "saldo": 50_000
    }


transaksi = [
    {
        "transaksi_id": 0,
        "user_id": 0,
        "produk_id": 0, 
        "status": "menunggu penjual"
    },
    {
        "transaksi_id": 1,
        "user_id": 1,
        "produk_id": 1, 
        "status": "menunggu penjual"
    },
]

produk = [
    {
        "produk_id": 0,
        "user_id": 1,
        "nama": "sabun",
        "harga": 5000
    },
    {
        "produk_id": 1,
        "user_id": 1,
        "nama": "sikat",
        "harga": 5000
    },
    {
        "produk_id": 2,
        "user_id": 2,
        "nama": "sikat",
        "harga": 5000
    },
     {
        "produk_id": 2,
        "user_id": 2,
        "nama": "sikat",
        "harga": 5000
    },
]



def cek_transaksi(user_id):
    # total transaksi
    total_transaksi = len(transaksi)  

    for i in range(0,total_transaksi):
        # cek  data transaksi berdasarkan id user
        if user_id == transaksi[i]["user_id"]:
            print("\n")
            print("transaksimu adalah :")
            print(f"produk: {produk[i]["nama"]}, status: {transaksi[i]["status"]}")
            print("\n")


def saldo():
    print("============")
    print("anda di halaman saldo")
    print("1 : cek total saldo anda")
    print("2 : tambah saldo")
    pilihan = input("masukkan nomor pilihan anda: ")
    saldo_sekarang = data["saldo"]

    match pilihan:
        case "1":
            print(f"saldo anda sekarang totalnya adalah : {saldo_sekarang}")         
        case "2":
            nominal_tambah = int(input("masukkan nominal tambahan saldo: "))
            saldo_sekarang += nominal_tambah
            print(f"saldo anda sekarang totalnya adalah : {saldo_sekarang}")
        case _:
            print("nomor yang anda masukkan tidak valid")

            
    





# main function
def pembeli(data):
    # cek id dengan nama user
    id = data['user_id']
    
    # informasi untuk input user
    print(f"selamat datang {data['username']}, selamat berbelanja \n")
    print("ketik nomor berikut untuk lanjut : ")
    print("1 : cek transaksi ")
    print("2 : cari barang ")
    print("3 : cek saldo atau tambah saldo ")
    # input user
    pilihan = input("masukkan nomormu :")

    # cek transaksi
    match pilihan:
        case "1":
            cek_transaksi(id)
        case "2":
            pass
        case "3":
            saldo()
        case "4":
            pass
        case _:
            print("pilihan tidak tersedia")




pembeli(data)
