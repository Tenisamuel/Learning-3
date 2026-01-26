from emoji_cipher import EmojiCipher

cipher = EmojiCipher()

message = input("Enter a message to encrypt: ")
encrypted = cipher.encrypt(message)
print("Encrypted:", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted)