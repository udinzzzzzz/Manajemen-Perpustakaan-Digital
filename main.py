from Manajemen_Buku  import DaftarBuku
from Manajemen_Antrian_Peminjam import AntrianPeminjam
from Penyimpanan_Buku  import simpan_ke_csv, baca_dari_csv

buku = DaftarBuku()
antrian = AntrianPeminjam()

# Load buku dari CSV
for b in baca_dari_csv():
    buku.tambah_buku(b['judul'], b['penulis'])

def menu():
    print("\n=== MENU PERPUSTAKAAN ===")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Lihat Daftar Buku")
    print("4. Tambah Antrian Peminjam")
    print("5. Layani Peminjam")
    print("6. Lihat Antrian")
    print("7. Simpan Buku ke CSV")
    print("8. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        buku.tambah_buku(judul, penulis)
        print("Buku ditambahkan.")

    elif pilihan == '2':
        judul = input("Judul buku yang ingin dihapus: ")
        buku.hapus_buku(judul)
        print("Buku dihapus.")

    elif pilihan == '3':
        daftar = buku.tampilkan_buku()
        if not daftar:
            print("Tidak ada buku.")
        else:
            for b in daftar:
                print(f"- {b['judul']} oleh {b['penulis']}")

    elif pilihan == '4':
        nama = input("Nama peminjam: ")
        antrian.tambah_peminjam(nama)
        print("Ditambahkan ke antrian.")

    elif pilihan == '5':
        nama = antrian.layani_peminjam()
        if nama:
            print(f"Melayani: {nama}")
        else:
            print("Tidak ada antrian.")

    elif pilihan == '6':
        antre = antrian.lihat_antrian()
        if not antre:
            print("Antrian kosong.")
        else:
            for i, n in enumerate(antre, 1):
                print(f"{i}. {n}")

    elif pilihan == '7':
        simpan_ke_csv(buku.tampilkan_buku())
        print("Data buku disimpan ke CSV.")

    elif pilihan == '8':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid.")
