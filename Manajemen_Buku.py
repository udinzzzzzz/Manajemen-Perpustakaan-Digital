class DaftarBuku:
    def __init__(self):
        self.buku = []

    def tambah_buku(self, judul, penulis):
        self.buku.append({'judul': judul, 'penulis': penulis})

    def hapus_buku(self, judul):
        self.buku = [b for b in self.buku if b['judul'].lower() != judul.lower()]

    def tampilkan_buku(self):
        return self.buku