print("Добро пожаловать в Шифратор!")
text = input("Введите текст: ").replace("ё", "е")
shift = int(input("Введите сдвиг: "))
encrypted_text = ""
for char in text:
    if char.isalpha():
        if char.islower():
            encrypted_text += chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
        else:
            encrypted_text += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
    else:
        encrypted_text += char
print("Зашифрованный текст: ", encrypted_text)