def split_text(text, max_len=200):
    return [text[i:i+max_len] for i in range(0, len(text), max_len)]