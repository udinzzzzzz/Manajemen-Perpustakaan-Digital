import csv

CSV_FILE = 'data_buku.csv'

def simpan_ke_csv(daftar_buku):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Judul', 'Penulis'])
        for buku in daftar_buku:
            writer.writerow([buku['judul'], buku['penulis']])

def baca_dari_csv():
    daftar = []
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                daftar.append({'judul': row['Judul'], 'penulis': row['Penulis']})
    except FileNotFoundError:
        pass
    return daftar