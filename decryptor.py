from cryptography.fernet import Fernet

key = input("Enter key: ").strip().encode()
encrypted = input("Enter encrypted text: ").strip().encode()

cipher = Fernet(key)

try:
    decrypted = cipher.decrypt(encrypted)
    print("Decrypted:", decrypted.decode())
except Exception as e:
    print("Error type:", type(e).__name__)
    print("Error:", e)
