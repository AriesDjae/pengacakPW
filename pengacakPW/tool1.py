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
def simpan(kata_asli, kata_acak, nama_file="pengacakPW/data/pw.csv"):
    # Menggunakan Path untuk memastikan path yang benar
    path = Path(nama_file).resolve()  
    os.makedirs(path.parent, exist_ok=True)  
    with open(path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([kata_asli, kata_acak])

print("")
print("Informasi:")
print("")
print("- Kata harus memiliki minimal 8 karakter")
print("- Ketik 'keluar' untuk berhenti")
print("- Kata tidak boleh mengandung spasi")
print("")

while True:
    kata = input("Masukkan kata : ")
    print("")

    if kata.lower() == 'keluar':
        print("Proses dibatalkan.")
        break

    if not kata.strip():
        print("Anda belum memasukkan kata. Silakan coba lagi.")
        continue

    if len(kata) < 8:
        print("Kata harus memiliki minimal 8 karakter. Silakan coba lagi.")
        continue

    if ' ' in kata:
        print("Kata tidak boleh mengandung spasi. Silakan coba lagi.")
        continue

    if kata_sudah_ada(kata):
        print("Kata sudah disimpan sebelumnya. Silakan coba kata lain.")
        continue

    kata_acak = acak_huruf(kata)
    
    simpan(kata, kata_acak)
    
    print(f"Kata asli: {kata}, Kata acak: {kata_acak}")
