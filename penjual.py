from data import produk, transaksi, database

# Tambah produk ke database Produk
def tambah_produk(user_id):
  nama_barang = input("Masukkan nama produk: ")
  harga_barang = int(input("Masukkan harga: "))

  produk_baru = {
    "produk_id": len(produk),
    "user_id": user_id,
    "nama" : nama_barang,
    "harga" : harga_barang
  }
  produk.append(produk_baru)
  print(f"Produk {nama_barang.capitalize()} berhasil ditambahkan dengan harga Rp{harga_barang:,}")

# Cek data produk sesuai id penjual/user
def list_produk(user_id):
  produk_penjual = [p for p in produk if p["user_id"] == user_id]

  # Menampilkan produk penjual dengan id,nama dan harga produk
  if produk_penjual:
    for p in produk_penjual:
      produk_id, _, nama, harga = p.values()
      print(f"ID produk {produk_id}, {nama} dengan harga Rp {harga:,}")
  else:
    print("Produk tidak tersedia")

# Cek transaksi produk penjual
def cek_transaksi(id):
  transaksi_penjual = []

  # Mencari transaksi sesuai produk penjual
  for t in transaksi:
    for p in produk: 
      if t["produk_id"] == p["produk_id"] and p["user_id"] == id:
        transaksi_penjual.append(t)
        break
    
  # Menampilkan transaksi beserta user pembeli dan produk penjual apa yang di beli
  if transaksi_penjual:
    for t in transaksi_penjual:
      transaksi_id, user_id, produk_id, status = t.values()
      nama_user = database[user_id]["username"]
      barang = produk[produk_id]
      print(f"ID transaksi {transaksi_id}. {nama_user}, {barang["nama"]} dengan harga {barang["harga"]} | Status : {status}")

    # Mau ubah status transaksi?
    ubah_status = input("Mau ubah status transaksi? (y/n) ")
    if ubah_status == "y":
      title_section("""
        Ubah status transaksi
                
1. Status: Sedang di proses
2. Status: Sedang dalam pengiriman
                """)
      id_transaksi_input = int(input("Masukkan ID transaksi yang akan di ubah: "))

    # Cek apakah id transaksi yang di input ada di dalam transaksi penjual
      found = False
      for t in transaksi_penjual:
        if t["transaksi_id"] == id_transaksi_input:
          found = True
          break

      if found:
      # Memilih tipe status yang akan di ubah
        pilih_status = int(input(f"Ubah status \'{transaksi[id_transaksi_input]["status"]}\' menjadi (1/2) : "))
      
        match pilih_status:
          case 1:
            transaksi[id_transaksi_input]["status"] =  "Sedang di proses"
            print(f"Status transaksi dengan ID {id_transaksi_input} berhasil di ubah \'Sedang di proses\'")
          case 2:
            transaksi[id_transaksi_input]["status"] =  "Sedang dalam pengiriman"
            print(f"Status transaksi dengan ID {id_transaksi_input} berhasil di ubah \'Sedang dalam   pengiriman\'")
          case _:
            print("Pilihan status tidak tersedia, silakan cek kembali")
      else:
        print("Transaksi dengan ID tersebut tidak ditemukan.")
  else:
    print("Tidak ada transaksi dengan produk kamu")

  


def title_section(title):
  print(f"""
=====================================
    {title}
=====================================
""")

def penjual(data_user):
  print("\n======== Menu Utama Penjual =========")
  print(f"""\
Selamat datang, {data_user["username"]}
Silakan pilih tugas anda:
  1. Lihat Produk kamu
  2. Tambah Produk
  3. Cek transaksi
  4. Keluar
""")
  task = input("Pilih tugas (1/2/3/4): ")

  match task:
    case "1":
      title_section("Daftar Produk kamu")
      list_produk(data_user["user_id"])
    case "2":
      title_section("Tambah Produk baru")
      tambah_produk(data_user["user_id"])
    case "3":
      title_section("Cek transaksi produk kamu")
      cek_transaksi(data_user["user_id"])
    case "4":
      print("Terima kasih!")
      return "keluar"
    case _:
      print("Maaf pilihan tidak ada di list")

# while True:
#   penjual(data)
