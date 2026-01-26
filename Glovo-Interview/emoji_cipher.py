import string

class EmojiCipher:
    def __init__(self):
        letters = string.ascii_lowercase

        emojis = [
            "😀","😃","😄","😁","😆","😅","😂","🤣","😊","😇",
            "🙂","🙃","😉","😌","😍","🥰","😘","😗","😙","😚",
            "😋","😛","😝","😜","🤪","🤨","🧐","🤓","😎","🥸",
            "🤩","🥳","😏","😒","😞","😔","😟","😕","🙁","☹️",
            "😣","😖","😫","😩","🥺","😢","😭","😤","😠","😡",
            "🤬","🤯","😳","🥵","🥶","😱","😨","😰","😥","😓",
            "🤗","🤔","🤭","🤫","🤥","😶","😐","😑","😬","🙄",
            "😯","😦","😧","😮","😲","🥱","😴","🤤","😪","😵",
            "🤐","🥴","🤢","🤮","🤧","😷","🤒","🤕","🤑","🤠"
        ]

        # Map letters to emojis
        self.encode_map = dict(zip(letters, emojis))
        # Reverse mapping for decoding
        self.decode_map = {v: k for k, v in self.encode_map.items()}

    def encrypt(self, text):
        result = ""
        for char in text.lower():
            if char in self.encode_map:
                result += self.encode_map[char]
            else:
                result += char  # keep spaces, punctuation
        return result

    def decrypt(self, emoji_text):
        result = ""
        buffer = ""
        for char in emoji_text:
            buffer += char
            if buffer in self.decode_map:
                result += self.decode_map[buffer]
                buffer = ""
        return result