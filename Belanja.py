def daftar_belanja():
    belanja = []

    while True:
        print("\n=== Daftar Belanja ===")
        print("1. Tambah item")
        print("2. Hapus item")
        print("3. Lihat daftar belanja")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            item = input("Masukkan item: ")
            belanja.append(item)
            print(f"'{item}' ditambahkan ke daftar belanja.")
        elif pilihan == '2':
            item = input("Masukkan item yang ingin dihapus: ")
            if item in belanja:
                belanja.remove(item)
                print(f"'{item}' dihapus dari daftar belanja.")
            else:
                print(f"'{item}' tidak ditemukan.")
        elif pilihan == '3':
            print("\nDaftar Belanja:")
            for i, item in enumerate(belanja, 1):
                print(f"{i}. {item}")
        elif pilihan == '4':
            print("Keluar dari program. Selamat berbelanja!")
            break
        else:
            print("Pilihan tidak valid!")

daftar_belanja()
