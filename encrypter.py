from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = input("Enter text: ").encode()
encrypted = cipher.encrypt(message)

print("Encrypted key:", key.decode())
print("Encrypted message:", encrypted.decode())
