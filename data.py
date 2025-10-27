database = [
    {"user_id": 0, "username": "Zutto", "password": "password123", "role": "Pembeli", "saldo": 50000},
    {"user_id": 1, "username": "damar", "password": "damar123", "role": "Penjual", "saldo": 0},
    {"user_id": 2, "username": "Lux", "password": "admin123", "role": "Penjual", "saldo": 0}
]

produk = [
  {'produk_id': 0, 'user_id': 1, 'nama': 'Sabun', 'harga': 9000},
  {'produk_id': 1, 'user_id': 1, 'nama': 'Pena', 'harga': 5000},
  {'produk_id': 2, 'user_id': 2, 'nama': 'Baju', 'harga': 10000}
]

transaksi = [
  {"transaksi_id": 0, "user_id": 0, "produk_id": 0, "status": "Menunggu penjual"},
  {"transaksi_id": 1, "user_id": 0, "produk_id": 1, "status": "Menunggu penjual"},
  {"transaksi_id": 2, "user_id": 0, "produk_id": 2, "status": "Menunggu penjual"}
]