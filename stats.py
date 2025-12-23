def get_num_words(text):
    words = text.split()
    num_words = f"Found {len(words)} total words"
    return num_words

def get_char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars