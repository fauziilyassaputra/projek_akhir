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
            print("============")       
        case "2":
            nominal_tambah = int(input("masukkan nominal tambahan saldo: "))
            saldo_sekarang += nominal_tambah
            print(f"saldo anda sekarang totalnya adalah : {saldo_sekarang}")
            print("============")
        case _:
            print("nomor yang anda masukkan tidak valid")
            print("============")

            
def cari_barang(user_id):
    print(f"seluruh barang yang tersedia saat ini : ")
    for i in range(len(produk)):
        nomor = i + 1
        print(f"no.{nomor} nama produk = {produk[i]["nama"]}, harga produk = {produk[i]["harga"]}")
    inputan_barang = int(input("masukkan nomor barang yang ingin dibeli: "))

    saldo_user = data["saldo"]

    if saldo_user <  produk[inputan_barang - 1]["harga"]:
        print("maaf, saldo anda tidak cukup")
        print("============")
    pesanan_user = {
        "transaksi_id": len(transaksi),
        "produk_id": inputan_barang - 1,
        "user_id": user_id,
        "status": "Menunggu penjual"
    }

    if pesanan_user != False:
        transaksi.append(pesanan_user)
        print("selamat anda berhasil memesan")
        print("============")

# main function
def pembeli(data):
    # cek id dengan nama user
    id = data['user_id']
    
    # informasi untuk input user
    print(f"selamat datang {data['username']}, selamat berbelanja \n")
    print("ketik nomor berikut untuk lanjut : ")
    print("1 : cek transaksi ")
    print("2 : cari barang untuk dibeli ")
    print("3 : cek saldo atau tambah saldo ")
    # input user
    pilihan = input("masukkan nomormu :")

    # cek transaksi
    match pilihan:
        case "1":
            cek_transaksi(id)
        case "2":
            cari_barang(id)
        case "3":
            saldo()
        case "4":
            pass
        case _:
            print("pilihan tidak tersedia")



while True:
    pembeli(data)
