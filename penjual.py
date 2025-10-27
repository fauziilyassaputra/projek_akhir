from data import produk, transaksi

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

  if produk_penjual:
    for p in produk_penjual:
      produk_id, _, nama, harga = p.values()
      print(f"{produk_id}. {nama} - Rp {harga:,}")
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
    
  if transaksi_penjual:
    for t in transaksi_penjual:
      transaksi_id, user_id, produk_id, status = t.values()
      print(f"{transaksi_id}. {user_id} {produk_id} | Status : {status}")

def title_section(title):
  print(f"""
=====================================
    {title}
=====================================
""")

def penjual(data_user):
  print(f"""
Selamat datang {data_user["username"]}
        
Silakan pilih tugas anda:
  1. Lihat Produk kamu
  2. Tambah Produk
  3. Cek transaksi
  4. Keluar

""")
  task = input("Pilih tugas(1/2/3/4): ")

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
      exit()
    case _:
      print("Maaf pilihan tidak ada di list")

# while True:
#   penjual(data)
