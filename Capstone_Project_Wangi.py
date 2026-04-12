# MEMBUAT APLIKASI PEMBELAN TIKET BIOSKOP

# Data Awal
id_film = [1, 2, 3, 4]
judul_film = ['Avengers', 'The Conjuring', 'Harry Potter', 'Titanic']
genre_film = ['Action', 'Horor', 'Fantasy', 'Romance']
harga_tiket = [50000, 65000, 75000, 80000 ]
jumlah_kursi_tersedia = [100, 150, 125, 200]

# ========== HELPER FUNCTION ==========

# Memastikan inputan user adalah angka
def input_angka(prompt, message="Harap masukkan angka yang valid!"):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f" {message}")

# ========== FUNCTION ==========

# Menampilkan Film
def tampilkan_film():
    print("\n" + "="*80) 
    print("DAFTAR FILM".center(80))
    print("="*80)

    # Header Table
    print(f"{'No':<4} {'ID':<4} {'Judul Film':<20} {'Genre':<10} {'Harga':<12} {'Kursi':<6}")
    print('-'*80)

    # Isi Table
    for i in range(len(id_film)):
        print(f"{i+1:<4} {id_film[i]:<4} {judul_film[i]:<20} {genre_film[i]:<10} Rp{harga_tiket[i]:<8} {jumlah_kursi_tersedia[i]:<6}")

    print("="*80)

# Menambahkan Film
def tambah_film():
    print("\n== TAMBAH FILM ==")
    nomor_id = input_angka("Masukkan ID: ")
    judul = input("Masukkan judul film: ")
    genre = input("Masukkan genre film: ")
    harga = input_angka("Masukkan harga tiket: ")
    kursi = input_angka("Masukkan jumlah kursi: ")

    id_film.append(nomor_id)
    judul_film.append(judul)
    genre_film.append(genre)
    harga_tiket.append(harga)
    jumlah_kursi_tersedia.append(kursi)

    print("Film berhasil ditambahkan!")

# Menghapus Film
def hapus_film():
    print("\n== HAPUS FILM ==")
    for i in range(len(judul_film)):
        print(f"{i+1}. {judul_film[i]}")
    hapus= input_angka("Masukkan nomor ID film yang ingin dihapus: ")

    if hapus in id_film:
        idx = id_film.index(hapus)  # cari index berdasarkan ID, bukan nomor urut
        del id_film[idx]
        del judul_film[idx]
        del genre_film[idx]
        del harga_tiket[idx]
        del jumlah_kursi_tersedia[idx]
        print("Film berhasil dihapus!")
    else:
        print("ID tidak ditemukan!")

# Mengubah Data Film
def update_film():
    print("\n" + "="*80) 
    print("DAFTAR FILM".center(80))
    print("="*80)

    # Header Table
    print(f"{'No':<4} {'ID':<4} {'Judul Film':<20} {'Genre':<10} {'Harga':<12} {'Kursi':<6}")
    print('-'*80)

    # Isi Table
    for i in range(len(id_film)):
        print(f"{i+1:<4} {id_film[i]:<4} {judul_film[i]:<20} {genre_film[i]:<10} Rp{harga_tiket[i]:<8} {jumlah_kursi_tersedia[i]:<6}")
    print("="*80)

    pilih = input_angka("Masukkan ID film yang ingin diupdate: ")
    if pilih in id_film:
        idx = id_film.index(pilih)

        print("\nPilih data yang ingin diupdate: ")
        print("1. Judul Film")
        print("2. Genre")
        print("3. Harga Tiket")
        print("4. Jumlah Kursi")

        pilihan_update = input_angka("Masukkan pilihan: ")

        if pilihan_update == 1:
            judul_film[idx] = input("Masukkan judul baru: ")
        elif pilihan_update == 2:
            genre_film[idx] = input("Masukkan genre baru: ")
        elif pilihan_update == 3:
            harga = input_angka("Masukkan harga baru: ")
            harga_tiket[idx] = harga
        elif pilihan_update == 4:
            kursi = input_angka("Masukkan jumlah kursi baru: ")
            jumlah_kursi_tersedia[idx] = kursi
        else:
            print("Pilihan tidak valid")
            return
        
        print("\nData berhasil di update!")

        # tampilkan data terbaru
        print("\n" + "="*80) 
        print("DAFTAR FILM".center(80))
        print("="*80)

        # Header Table
        print(f"{'No':<4} {'ID':<4} {'Judul Film':<20} {'Genre':<10} {'Harga':<12} {'Kursi':<6}")
        print('-'*80)

        # Isi Table
        for i in range(len(id_film)):
            print(f"{i+1:<4} {id_film[i]:<4} {judul_film[i]:<20} {genre_film[i]:<10} Rp{harga_tiket[i]:<8} {jumlah_kursi_tersedia[i]:<6}")

        print("="*80)

    else:print("Nomor film tidak valid")

# Membeli Tiket Film
def beli_tiket():
    cart_id = []
    cart_jumlah = []
    total_harga = 0

    while True:
        print("\n" + "="*50)
        print("BELI TIKET".center(50))
        print("="*50)

        # Tampilkan daftar film
        for i in range(len(id_film)):
            print(f"{i+1}. {judul_film[i]:<20} | Rp{harga_tiket[i]:,} | Kursi: {jumlah_kursi_tersedia[i]}")

        print("-"*50)
        beli= input("Pilih nomor ID film (ketik 'selesai'untuk bayar): ")

        if beli.lower() == 'selesai':
            break
        try:
            beli = int(beli)
        except ValueError:
            print("Harap masukkan angka untuk nomor film!")
            continue
    
        if beli in id_film:
            idx = id_film.index(beli)  # cari index yang benar berdasarkan ID
            jumlah = input_angka("Jumlah Tiket: ")

            if jumlah <= jumlah_kursi_tersedia[idx]:
                cart_id.append(idx)
                cart_jumlah.append(jumlah)
                total_harga += jumlah * harga_tiket[idx]
                print("Tiket berhasil ditambahkan ke keranjang!")
            else:
                print("Kursi tidak cukup")
        else:
            print("ID tidak valid!")
    
    # ========== STRUK ==========
    print("\n" + "="*50)
    print("STRUK PEMBELIAN".center(50))
    print("="*50)

    for i in range(len(cart_id)):
        idx = cart_id[i]
        subtotal = cart_jumlah[i] * harga_tiket[idx]
        print(f"{judul_film[idx]:<20} x {cart_jumlah[i]} = Rp{subtotal:,}")

    print("-"*50)
    print(f"{"TOTAL":<25} Rp{total_harga:,}")

    # ========== PEMBAYARAN ==========
    while True:
        uang = input_angka("Masukkan jumlah uang: ")
        if uang >= total_harga:
            kembalian = uang - total_harga
            print(f"Kembalian: Rp{kembalian:,}")

            # Update Kursi
            for i in range(len(cart_id)):
                idx = cart_id[i]
                jumlah_kursi_tersedia[idx] -= cart_jumlah[i]

            print("Transaksi berhasil!")
            break
        else:
            print("Uang tidak cukup!")

# ========== MAIN PROGRAM ==========

while True:
    print("\n== BIOSKOP PURWADHIKA ==")
    print("1. Tampilkan Daftar Film")
    print("2. Tambah Film")
    print("3. Hapus Film")
    print("4. Update Film")
    print("5. Beli Tiket")
    print("6. Exit")

    menu = input("Pilih nomor menu: ")

    if menu == '1':
        tampilkan_film()
    elif menu =='2':
        tambah_film()
    elif menu == '3':
        hapus_film()
    elif menu =='4':
        update_film()
    elif menu == '5':
        beli_tiket()
    elif menu == '6':
        print("Terima Kasih!")
        break
    else:
        print("Menu tidak valid!")
