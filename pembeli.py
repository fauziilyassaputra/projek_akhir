from data import transaksi, produk

def cek_transaksi(user_id):
    # total transaksi yang ada
    total_transaksi = len(transaksi)  

    print("Total transaksimu adalah :")
    for i in range(0,total_transaksi):
        # cek  data transaksi berdasarkan id user
        if user_id == transaksi[i]["user_id"]:
            nama_produk = transaksi[i]["produk_id"]
            print(f"produk: {produk[nama_produk]["nama"]}, status: {transaksi[i]["status"]}")


def cek_saldo(saldo):
    print("Anda di halaman saldo")
    print("1 : cek total saldo Anda")
    print("2 : tambah saldo")
    pilihan = input("masukkan nomor pilihan Anda: ")
   

    match pilihan:
        case "1":
            # cek saldo
            print(f"saldo Anda sekarang totalnya adalah : {saldo}")      
        case "2":
            # input jumlah saldo yang akan ditambahkan
            nominal_tambah = int(input("masukkan nominal tambahan saldo: "))
            if nominal_tambah > 0:
                saldo += nominal_tambah
                print(f"saldo Anda sekarang totalnya adalah : {saldo}")
            else:
                print("nominal yang Anda masukkan tidak valid")
            
        case _:
            print("nomor yang Anda masukkan tidak valid")
    # saldo di return untuk memperbarui jumlah saldo
    return saldo

            
def cari_barang(user_id, saldo):
    print(f"seluruh barang yang tersedia saat ini : ")
    for i in range(len(produk)):
        nomor = i + 1
        print(f"no.{nomor} nama produk = {produk[i]["nama"]}, harga produk = {produk[i]["harga"]}")
    inputan_barang = int(input("masukkan nomor barang yang ingin dibeli: "))

    saldo_user = saldo
    # cek jika saldo ternyata kurang 
    if saldo_user <  produk[inputan_barang - 1]["harga"]:
        print("maaf, saldo Anda tidak cukup")
        print("===================")
    
    # saldo yang dimiliki dikurangi dengan harga barang
    harga_produk = produk[inputan_barang - 1]["harga"]
    saldo_user -= harga_produk
    nama_barang = produk[inputan_barang - 1]["nama"]

    # buat dictionary pesanan
    pesanan_user = {
        "transaksi_id": len(transaksi),
        "user_id": user_id,
        "produk_id": inputan_barang - 1,
        "status": "Menunggu penjual"
    }

    # tambahkan datanya jika tidak ada error apapun
    if pesanan_user != False:
        transaksi.append(pesanan_user)
        print(f"\nSelamat! Anda berhasil memesan {nama_barang} dengan harga {harga_produk}")
        print("===================")
    
    # return untuk memperbarui saldo yang sudah dikurangi
    return saldo_user

# main function
def pembeli(data):
    #id dan saldo user
    id = data['user_id']
    saldo = data["saldo"]
    
    # informasi untuk input user
    print("\n=== Menu Utama Pembeli ====")
    print(f"Selamat datang, {data['username']}. Selamat berbelanja.")
    print("ketik nomor berikut untuk lanjut : ")
    print("1 : cek transaksi ")
    print("2 : cari barang untuk dibeli ")
    print("3 : cek saldo atau tambah saldo ")
    print("4 : Keluar")
    # input user
    pilihan = input("Masukkan nomormu: ")
    print("===================")
    
    match pilihan:
        # cek transaksi
        case "1":
            cek_transaksi(id)
        case "2":
            saldo_belanja = cari_barang(id, saldo)
            # perbarui dictionary di file data
            data["saldo"] = saldo_belanja
            # perbarui variable saldo diatas
            saldo = saldo_belanja
        case "3":
            saldo_baru = cek_saldo(saldo)
            # perbarui dictionary di file data
            data['saldo'] = saldo_baru
            # perbarui variable saldo diatas
            saldo = saldo_baru
        case "4":
            print("Terima kasih!")
            return "keluar"
        case _:
            print("pilihan tidak tersedia")

