from pembeli import pembeli
from penjual import penjual
from data import database

panjangInisialDatabase = int(len(database))

def register():

    print("\n--- Registrasi ---")
    username = input("Username (tanpa spasi): ")
    
    # Cek username
    for cekUser in database:
        if cekUser["username"] == username:
            print("Username udah ada.")
            return
            
    password = input("Buat Password: ")
        
    # Pilih Role
    print("Role:\n1. Pembeli\n2. Penjual")
    RolePilihan = input("Pilih Role:")
    role = ""
    if RolePilihan == '1':
        role = "Pembeli"
    elif RolePilihan == '2':
        role = "Penjual"
    else:
        print("Pilih role yang benar")
        return
        
    # konstruksi data baru
    idUserBaru = len(database)
    userBaru = {
        "user_id": idUserBaru,
        "username": username,
        "password": password,
        "role": role,
        "saldo": 0
    }
    
    # masukkan ke database
    database.append(userBaru)
    print(f"Registrasi berhasil! Silakan login, {username}")


def login():
    print("\n--- Halaman Login ---")
    username = input("Username: ")
    password = input("Password: ")
    
    # Cari pengguna di database
    for cekUser in database:
        if cekUser["username"] == username and cekUser["password"] == password:
            print(f"Login berhasil! {username}")
            idnya = cekUser["user_id"]
            
            while True:
                # Ke menu sesuai role
                if cekUser["role"] == "Pembeli":
                    pembeli(database[idnya])

                elif cekUser["role"] == "Penjual":
                    penjual(database[idnya])
            
    # Kalau user dan password tidak ditemukan
    print("Username atau password salah.")
    
################################################################################################
# Bagian utama kode

while True:
    print('''
========================
|    Ini E-Commerce    |
========================
1. Login
2. Register
3. Keluar
''')

    pilihan = input("Pilih 1/2/3: ")
    if pilihan == '1':
        login()
    elif pilihan == '2':
        register()
    elif pilihan == '3':
        print("Terima kasih!")
        break 
        
    else:
        print("Pilihan tidak valid.")

