def encrypt(text, rot):
    new_text = ''
    for x in text:
        new_text += rotate_character(x, rot)
    return new_text

def alphabet_position(letter):
    return ord(letter.lower()) - 97

def rotate_character(char, rot):
    if char.isalpha():
        if char == char.upper():
            new_char = chr((ord(char) - 65 + rot) % 26 + 65)
        elif char == char.lower():
            new_char = chr((ord(char) - 97 + rot) % 26 + 97)
        return new_char
    else:
        return char
