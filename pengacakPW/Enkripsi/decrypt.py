import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

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

# Meminta input dari pengguna
encrypted_password = input("Masukkan kata sandi terenkripsi: ")
key = input("Masukkan kunci dekripsi: ")

try:
    # Mencoba mendekripsi kata sandi
    decrypted_password = decrypt_password(encrypted_password, key)
    print(f"Kata sandi terdekripsi: {decrypted_password}")
except Exception as e:
    print(f"Terjadi kesalahan saat mendekripsi: {e}")
    print("Pastikan kata sandi terenkripsi dan kunci dekripsi yang Anda masukkan benar.")