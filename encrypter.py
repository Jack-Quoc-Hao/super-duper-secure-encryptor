from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = input("Enter text: ").encode()
encrypted = cipher.encrypt(message)

print("Key:", key.decode())
print("Encrypted:", encrypted.decode())
