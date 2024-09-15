import random
import csv
import os
from pathlib import Path

# Fungsi untuk mengacak huruf dalam kata
def acak_huruf(kata):
    huruf_list = list(kata)
    random.shuffle(huruf_list)
    return ''.join(huruf_list)

# Fungsi untuk memeriksa apakah kata sudah ada dalam file CSV
def kata_sudah_ada(kata, nama_file="pengacakPW/data/pw.csv"):
    if not os.path.exists(nama_file):
        return False
    
    with open(nama_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == kata:
                return True
    return False

# Fungsi untuk menyimpan data ke dalam file CSV
def simpan_csv(kata_asli, kata_acak, nama_file="pengacakPW/data/pw.csv"):
    path = Path(nama_file).resolve()
    os.makedirs(path.parent, exist_ok=True)  # Membuat direktori jika belum ada
    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([kata_asli, kata_acak])

# Fungsi untuk menampilkan kata yang sudah disimpan
def tampilkan_kata(nama_file="pengacakPW/data/pw.csv"):
    if not os.path.exists(nama_file):
        print("File tidak ditemukan.")
        return
    
    with open(nama_file, mode='r') as file:
        reader = csv.reader(file)
        print("Daftar kata yang sudah disimpan:")
        print("")
        for row in reader:
            print(row[0])

# Fungsi untuk menghapus kata dari file CSV
def hapus_kata(kata_hapus, nama_file="pengacakPW/data/pw.csv"):
    if not os.path.exists(nama_file):
        print("File tidak ditemukan.")
        return

    with open(nama_file, mode='r') as file:
        rows = list(csv.reader(file))

    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != kata_hapus:
                writer.writerow(row)
    print("")
    print(f"Kata '{kata_hapus}' telah dihapus.")
    print("")

# Fungsi untuk menampilkan informasi
def help():
    print("")
    print("Informasi:")
    print("")
    print("Kata tidak boleh mengandung spasi.")
    print("Kata harus memiliki minimal 8 karakter.")
    print("Kata yang sudah disimpan tidak bisa digunakan lagi.")
    print("Ketik 'keluar' untuk berhenti.")
    print("Ketik 'ls' untuk menampilkan kata.")
    print("Ketik 'hapus' untuk menghapus kata.")
    print("Ketik 'help' untuk menampilkan informasi.")
    print("")


#informasi start program
print("")
print("Informasi:")
print("")
print("Tidak boleh mengandung spasi.")
print("Kata harus memiliki minimal 8 karakter.")
print("Kata yang sudah disimpan tidak bisa digunakan lagi.")
print("Ketik 'keluar' untuk berhenti.")
print("Ketik 'ls' untuk menampilkan kata.")
print("Ketik 'hapus' untuk menghapus kata.")
print("Ketik 'help' untuk menampilkan informasi.")
print("")

while True:
    perintah = input("Masukkan perintah atau kata: ").strip()
    
    if perintah.lower() == 'keluar':
        print("")
        print("Proses dibatalkan.")
        print("")
        break

    if perintah.lower() == 'ls':
        print("")
        tampilkan_kata()
        print("")
        continue

    if perintah.lower().startswith('hapus '):
        print("")
        kata_hapus = perintah[6:]  # Mengambil kata setelah 'hapus '
        hapus_kata(kata_hapus)
        print("")
        continue

    if perintah.lower() == 'help':
        print("")
        help()
        print("")
        continue

    if not perintah or ' ' in perintah:
        print("")
        print("Kata tidak boleh mengandung spasi dan harus ada isinya.")
        print("")
        continue
    
    if len(perintah) < 8:
        print("")
        print("Kata harus memiliki minimal 8 karakter. Silakan coba lagi.")
        print("")
        continue

    if kata_sudah_ada(perintah):
        print("")
        print("Kata sudah disimpan sebelumnya. Silakan coba kata lain.")
        print("")
        continue

    

    kata_acak = acak_huruf(perintah)
    

    simpan_csv(perintah, kata_acak)
    
    print(f"Kata asli: {perintah}, Kata acak: {kata_acak}")
    

    break
