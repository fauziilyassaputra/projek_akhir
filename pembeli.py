data = [
    {
        "user_id":0,
        "username": "Zutto",
        "password": "password123",
    },
      {
        "user_id":1,
        "username": "damar",
        "password": "damar123",
    }
]

transaksi = [
    {
        "transaksi_id": 0,
        "user_id": 0,
        "produk_id": 0, 
        "status": "menunggu penjual"
    },
    {
        "transaksi_id": 1,
        "user_id": 0,
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
]





def pembeli(data):
    # cek id dengan nama user
    id = data["user_id"]
    print(id)
    print(f"selamat datang {user}, selamat berbelanja \n")
    print("ketik nomor berikut untuk lanjut : ")
    print("1 : cek transaksi ")
    print("2 : cari barang ")
    print("3 : cek saldo atau tambah saldo ")
    pilihan = int(input("masukkan nomormu :"))


    if pilihan == 1:
        print("cek transaksi")
        cek_transaksi(id)

   
while True:
    pembeli(data)
