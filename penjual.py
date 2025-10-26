data = {
  "user_id": 1,
  "username": "Lux",
  "saldo" : 0
}

produk = [
  {'produk_id': 0, 'user_id': 1, 'nama': 'Sabun', 'harga': 9000},
  {'produk_id': 1, 'user_id': 1, 'nama': 'Barang', 'harga': 5000},
  {'produk_id': 2, 'user_id': 2, 'nama': 'Baju', 'harga': 10000}
]

transaksi = [
  {"transaksi_id": 0, "user_id": 0, "produk_id": 0, "status": "Menunggu penjual"},
  {"transaksi_id": 1, "user_id": 0, "produk_id": 1, "status": "Menunggu penjual"}
]

# Tambah produk ke database Produk
def tambah_produk(id):
  nama_barang = input("Masukkan nama produk: ")
  harga_barang = int(input("Masukkan harga: "))

  produk_baru = {
    "produk_id": len(produk),
    "user_id": id,
    "nama" : nama_barang,
    "harga" : harga_barang
  }
  produk.append(produk_baru)
  print(f"Produk {nama_barang.capitalize()} berhasil ditambahkan dengan harga Rp{harga_barang:,}")

# Cek data produk sesuai id penjual/user
def list_produk(id):
  produk_penjual = [x for x in produk if x["user_id"] == id]

  if produk_penjual:
    for x in produk_penjual:
      produk_id, _, nama, harga = x.values()
      print(f"{produk_id}. {nama} - Rp {harga:,}")
  else:
    print("Produk tidak tersedia")

# Cek transaksi produk penjual
def cek_transaksi():
  pass

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
      cek_transaksi()
    case "4":
      print("Terima kasih!")
      exit()
    case _:
      print("Maaf pilihan tidak ada di list")

while True:
  penjual(data)
