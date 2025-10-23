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


def tambah_produk(user_id):
  nama_barang = input("Masukkan nama produk: ")
  harga_barang = int(input("Masukkan harga: "))

  produk.append({
    "produk_id": len(produk),
    "user_id": user_id,
    "nama" : nama_barang,
    "harga" : harga_barang
  })

def list_produk(user_id):
  for x in produk:
    if x["user_id"] == user_id:
      print(f"{x["produk_id"]}. {x["nama"]} dengan harga {x["harga"]}")

def cek_transaksi():
  pass


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
      list_produk(data_user["user_id"])
    case "2":
      tambah_produk(data_user["user_id"])
    case "3":
      cek_transaksi()
    case "4":
      exit()
    case _:
      print("Maaf pilihan tidak ada di list")

while True:
  penjual(data)
