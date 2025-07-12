from collections import deque

class AntrianPeminjam:
    def __init__(self):
        self.queue = deque()

    def tambah_peminjam(self, nama):
        self.queue.append(nama)

    def layani_peminjam(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def lihat_antrian(self):
        return list(self.queue)
