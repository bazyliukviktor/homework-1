text = "hello"
shift = 3

encrypted_text = ""

for char in text:
    new_code = ord(char) + shift

    # Циліндричне закольцьовування після 'z'
    if new_code > ord('z'):
        new_code -= 26

    encrypted_text += chr(new_code)

print('Зашифрований текст:', encrypted_text)