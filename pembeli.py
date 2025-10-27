from data import transaksi, produk

def cek_transaksi(user_id):
    # total transaksi
    total_transaksi = len(transaksi)  

    print("Total transaksimu adalah :")
    for i in range(0,total_transaksi):
        # cek  data transaksi berdasarkan id user
        if user_id == transaksi[i]["user_id"]:
            nama_produk = transaksi[i]["produk_id"]
            print(f"produk: {produk[nama_produk]["nama"]}, status: {transaksi[i]["status"]}")


def cek_saldo(saldo):
    print("============")
    print("anda di halaman saldo")
    print("1 : cek total saldo anda")
    print("2 : tambah saldo")
    pilihan = input("masukkan nomor pilihan anda: ")
    # saldo_sekarang = saldo

    match pilihan:
        case "1":
            print(f"saldo anda sekarang totalnya adalah : {saldo}")  
            print("============")       
        case "2":
            nominal_tambah = int(input("masukkan nominal tambahan saldo: "))
            saldo += nominal_tambah
            print(f"saldo anda sekarang totalnya adalah : {saldo}")
            print("============")
        case _:
            print("nomor yang anda masukkan tidak valid")
            print("============")

            
def cari_barang(user_id, saldo):
    print(f"seluruh barang yang tersedia saat ini : ")
    for i in range(len(produk)):
        nomor = i + 1
        print(f"no.{nomor} nama produk = {produk[i]["nama"]}, harga produk = {produk[i]["harga"]}")
    inputan_barang = int(input("masukkan nomor barang yang ingin dibeli: "))

    saldo_user = saldo

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
        print(transaksi)

# main function
def pembeli(data):
    # cek id dengan nama user
    id = data['user_id']
    saldo = data["saldo"]
    
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
            cari_barang(id, saldo)
        case "3":
            cek_saldo(saldo)
        case "4":
            pass
        case _:
            print("pilihan tidak tersedia")



# while True:
#     pembeli(data)
