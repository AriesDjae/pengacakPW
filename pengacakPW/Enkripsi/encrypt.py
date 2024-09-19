import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt_password(password, key):
    # Menghasilkan kunci 32 byte dari input key menggunakan SHA-256
    key = SHA256.new(key.encode()).digest()

    # Padding password agar panjangnya kelipatan 16 byte
    password = password.encode()
    padding = AES.block_size - (len(password) % AES.block_size)
    password += bytes([padding]) * padding

    # Membuat initialization vector (IV)
    iv = Random.new().read(AES.block_size)

    # Membuat objek cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Melakukan enkripsi
    encrypted = cipher.encrypt(password)

    # Menggabungkan IV dan hasil enkripsi, lalu encode dengan base64
    return base64.b64encode(iv + encrypted).decode('utf-8')

def decrypt_password(encrypted_password, key):
    # Menghasilkan kunci 32 byte dari input key menggunakan SHA-256
    key = SHA256.new(key.encode()).digest()

    # Decode base64 dan pisahkan IV dan encrypted password
    encrypted = base64.b64decode(encrypted_password.encode('utf-8'))
    iv = encrypted[:AES.block_size]
    encrypted_password = encrypted[AES.block_size:]

    # Membuat objek cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Melakukan dekripsi
    decrypted = cipher.decrypt(encrypted_password)

    # Menghapus padding
    padding = decrypted[-1]
    decrypted = decrypted[:-padding]

    return decrypted.decode('utf-8')

# Contoh penggunaan
password = input("Masukkan kata sandi: ")
key = input("Masukkan kunci enkripsi: ")

encrypted_password = encrypt_password(password, key)
print(f"Kata sandi terenkripsi: {encrypted_password}")
print("")
# Untuk memverifikasi, kita bisa mencoba mendekripsi
decrypted_password = decrypt_password(encrypted_password, key)
print(f"Kata sandi terdekripsi: {decrypted_password}")