import os
import base64
import hashlib  # kept from your original imports, no longer used directly for hashing the password
import datetime

from tkinter import (
    Tk, Label, Entry, Button, Text, filedialog, END,
    Frame, StringVar, font as tkfont, PhotoImage
)
import tkinter as tk
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# --------- Colour palette (dark terminal theme) --------
BG_DARK      = "#0d1117"   # main background — near-black
BG_PANEL     = "#161b22"   # slightly lighter panels / cards
BG_INPUT     = "#21262d"   # input fields
ACCENT       = "#00d4aa"   # teal — the one bold colour used throughout
ACCENT_HOVER = "#00b894"   # darker teal for hover states
TEXT_PRIMARY = "#e6edf3"   # off-white body text
TEXT_MUTED   = "#7d8590"   # secondary / placeholder text
BORDER       = "#30363d"   # subtle borders
DANGER       = "#f85149"   # red — used only for error states
SUCCESS      = "#3fb950"   # green — used only for success confirmations


# --------- key derivation from master password --------

# A "salt" is a random value mixed into the password before hashing.
# It doesn't need to be secret, but it DOES need to be the same every
# time you derive a key, or you'll get a different key each run and
# decryption will fail. So we save it to a file once, then reuse it.
SALT_FILE = "salt.bin"


def get_or_create_salt() -> bytes:
    # If we've already generated a salt before, reuse it from disk.
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    # Otherwise, generate a fresh random salt and save it for next time.
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    return salt


def derive_key_from_password(password: str) -> bytes:
    # Derive a Fernet key from a password using PBKDF2 with a salt.
    # PBKDF2 deliberately runs the hash thousands of times in a row,
    # which makes brute-force password guessing much slower for an
    # attacker, unlike a single plain SHA-256 hash (which is fast,
    # and therefore weaker for this purpose).
    salt = get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480_000,  # higher = slower to brute-force, slower to compute
    )
    digest = kdf.derive(password.encode("utf-8"))
    return base64.urlsafe_b64encode(digest)


# ----------- Encryption / Decryption helpers ------

def encrypt_bytes(data: bytes, key: bytes) -> bytes:
    # Encrypts raw bytes using the given Fernet key.
    f = Fernet(key)
    return f.encrypt(data)


def decrypt_bytes(data: bytes, key: bytes) -> bytes:
    # Decrypts raw bytes using the given Fernet key.
    f = Fernet(key)
    return f.decrypt(data)


def encrypt_file(path: str, key: bytes):
    # Reads a file's raw bytes, encrypts them, and writes the result
    # to a new file with ".enc" appended to the name.
    with open(path, "rb") as f:
        plaintext = f.read()
    ciphertext = encrypt_bytes(plaintext, key)
    with open(path + ".enc", "wb") as f:
        f.write(ciphertext)


def decrypt_file(path: str, key: bytes):
    # Reads an encrypted file and writes the decrypted bytes back out.
    # If the file ends in ".enc", that suffix is stripped for the output
    # name; otherwise ".dec" is appended so we don't overwrite anything.
    with open(path, "rb") as f:
        ciphertext = f.read()
    plaintext = decrypt_bytes(ciphertext, key)
    if path.endswith(".enc"):
        out_path = path[:-4]
    else:
        out_path = path + ".dec"
    with open(out_path, "wb") as f:
        f.write(plaintext)


# --------- Reusable styled button --------

class StyledButton(tk.Button):
    """A Button that mimics a modern flat style with hover feedback."""
    def __init__(self, parent, text, command, style="primary", **kwargs):
        if style == "primary":
            bg, fg, hover = ACCENT, BG_DARK, ACCENT_HOVER
        else:  # secondary
            bg, fg, hover = BG_INPUT, TEXT_PRIMARY, BORDER

        super().__init__(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=fg,
            activebackground=hover,
            activeforeground=fg,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=8,
            bd=0,
            **kwargs
        )
        self._bg = bg
        self._hover = hover
        self.bind("<Enter>", lambda e: self.config(bg=hover))
        self.bind("<Leave>", lambda e: self.config(bg=bg))


# --------- Tkinter UI ---------

class EncryptionApp:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("PyVault — Personal Encryption Tool")
        self.root.configure(bg=BG_DARK)
        self.root.minsize(620, 560)
        self.root.resizable(True, True)

        # ---- fonts ----
        # Monospace for the cipher/text area; clean sans-serif for UI chrome
        self.font_ui    = tkfont.Font(family="Segoe UI",   size=10)
        self.font_label = tkfont.Font(family="Segoe UI",   size=9,  weight="normal")
        self.font_mono  = tkfont.Font(family="Consolas",   size=10)
        self.font_title = tkfont.Font(family="Segoe UI",   size=13, weight="bold")
        self.font_log   = tkfont.Font(family="Consolas",   size=8)

        self._build_ui()

    # ------------------------------------------------------------------
    def _build_ui(self):
        # ---- header bar ----
        header = Frame(self.root, bg=BG_PANEL, pady=12)
        header.pack(fill="x")

        Label(
            header,
            text="🔒  PyVault",
            bg=BG_PANEL,
            fg=ACCENT,
            font=self.font_title,
        ).pack(side="left", padx=20)

        Label(
            header,
            text="AES-128 · PBKDF2 · Fernet",
            bg=BG_PANEL,
            fg=TEXT_MUTED,
            font=self.font_label,
        ).pack(side="right", padx=20)

        # thin accent line under header
        Frame(self.root, bg=ACCENT, height=2).pack(fill="x")

        # ---- main body ----
        body = Frame(self.root, bg=BG_DARK, padx=20, pady=16)
        body.pack(fill="both", expand=True)
        body.columnconfigure(1, weight=1)

        # -- master password row --
        self._section_label(body, "MASTER PASSWORD", row=0)

        Label(
            body,
            text="Password",
            bg=BG_DARK,
            fg=TEXT_MUTED,
            font=self.font_label,
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=(0, 2))

        pw_frame = Frame(body, bg=BG_INPUT, highlightbackground=BORDER,
                         highlightthickness=1)
        pw_frame.grid(row=1, column=1, sticky="ew", padx=(8, 0), pady=(0, 16))

        self.password_entry = Entry(
            pw_frame,
            show="●",
            bg=BG_INPUT,
            fg=TEXT_PRIMARY,
            insertbackground=ACCENT,
            relief="flat",
            font=self.font_mono,
            bd=6,
        )
        self.password_entry.pack(fill="x")
        self.password_entry.bind("<FocusIn>",  lambda e: pw_frame.config(highlightbackground=ACCENT))
        self.password_entry.bind("<FocusOut>", lambda e: pw_frame.config(highlightbackground=BORDER))

        # -- text area --
        self._section_label(body, "TEXT / SNIPPET", row=2)

        text_frame = Frame(body, bg=BG_INPUT, highlightbackground=BORDER,
                           highlightthickness=1)
        text_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(0, 12))
        body.rowconfigure(3, weight=1)

        self.text_area = Text(
            text_frame,
            height=10,
            bg=BG_INPUT,
            fg=TEXT_PRIMARY,
            insertbackground=ACCENT,
            selectbackground=ACCENT,
            selectforeground=BG_DARK,
            relief="flat",
            font=self.font_mono,
            padx=10,
            pady=8,
            wrap="word",
            bd=0,
        )
        self.text_area.pack(fill="both", expand=True)
        self.text_area.bind("<FocusIn>",  lambda e: text_frame.config(highlightbackground=ACCENT))
        self.text_area.bind("<FocusOut>", lambda e: text_frame.config(highlightbackground=BORDER))

        # -- button row --
        btn_row = Frame(body, bg=BG_DARK)
        btn_row.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 4))
        for i in range(4):
            btn_row.columnconfigure(i, weight=1)

        StyledButton(btn_row, "Encrypt Text", self.encrypt_text, style="primary",
                     font=self.font_ui).grid(row=0, column=0, sticky="ew", padx=(0, 4))

        StyledButton(btn_row, "Decrypt Text", self.decrypt_text, style="secondary",
                     font=self.font_ui).grid(row=0, column=1, sticky="ew", padx=(0, 8))

        Frame(btn_row, bg=BORDER, width=1).grid(row=0, column=2, sticky="ns", padx=6)

        StyledButton(btn_row, "Encrypt File", self.encrypt_file_dialog, style="primary",
                     font=self.font_ui).grid(row=0, column=3, sticky="ew", padx=(0, 4))

        StyledButton(btn_row, "Decrypt File", self.decrypt_file_dialog, style="secondary",
                     font=self.font_ui).grid(row=0, column=4, sticky="ew")

        btn_row.columnconfigure(4, weight=1)

        # ---- status / audit log strip ----
        log_outer = Frame(self.root, bg=BG_PANEL, highlightbackground=BORDER,
                          highlightthickness=1)
        log_outer.pack(fill="x", side="bottom")

        Label(
            log_outer,
            text="AUDIT LOG",
            bg=BG_PANEL,
            fg=TEXT_MUTED,
            font=self.font_log,
            anchor="w",
            padx=12,
            pady=4,
        ).pack(fill="x")

        self.log_text = Text(
            log_outer,
            height=4,
            bg=BG_PANEL,
            fg=TEXT_MUTED,
            font=self.font_log,
            relief="flat",
            state="disabled",
            padx=12,
            pady=4,
            bd=0,
            wrap="word",
        )
        self.log_text.pack(fill="x")

        # colour tags for the log
        self.log_text.tag_config("ok",  foreground=SUCCESS)
        self.log_text.tag_config("err", foreground=DANGER)
        self.log_text.tag_config("ts",  foreground=TEXT_MUTED)

        self._log("PyVault initialised. Enter your master password to begin.", "ok")

    # ------------------------------------------------------------------
    def _section_label(self, parent, text, row):
        """Renders a small all-caps muted section heading."""
        Label(
            parent,
            text=text,
            bg=BG_DARK,
            fg=TEXT_MUTED,
            font=tkfont.Font(family="Segoe UI", size=8, weight="bold"),
            anchor="w",
        ).grid(row=row, column=0, columnspan=2, sticky="w", pady=(8, 4))

    def _log(self, message: str, kind: str = "ok"):
        """Appends a timestamped line to the audit log strip."""
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        self.log_text.config(state="normal")
        self.log_text.insert(END, f"[{ts}] ", "ts")
        self.log_text.insert(END, message + "\n", kind)
        self.log_text.see(END)
        self.log_text.config(state="disabled")

    # ---- helper to grab and derive the key from whatever's in the password field ----
    def _get_key(self) -> bytes:
        password = self.password_entry.get()
        if not password:
            raise ValueError("Enter a master password first.")
        return derive_key_from_password(password)

    # ---- text button handlers ----
    def encrypt_text(self):
        try:
            key = self._get_key()
            plaintext = self.text_area.get("1.0", END).strip().encode("utf-8")
            ciphertext = encrypt_bytes(plaintext, key)
            self.text_area.delete("1.0", END)
            self.text_area.insert("1.0", ciphertext.decode("utf-8"))
            self._log("Text encrypted successfully.", "ok")
        except Exception as e:
            self._log(f"Encrypt text failed — {e}", "err")

    def decrypt_text(self):
        try:
            key = self._get_key()
            ciphertext = self.text_area.get("1.0", END).strip().encode("utf-8")
            plaintext = decrypt_bytes(ciphertext, key)
            self.text_area.delete("1.0", END)
            self.text_area.insert("1.0", plaintext.decode("utf-8"))
            self._log("Text decrypted successfully.", "ok")
        except InvalidToken:
            self._log("Decrypt failed — wrong password or corrupted ciphertext.", "err")
        except Exception as e:
            self._log(f"Decrypt text failed — {e}", "err")

    # ---- file button handlers ----
    def encrypt_file_dialog(self):
        path = filedialog.askopenfilename(title="Select a file to encrypt")
        if not path:
            return
        try:
            key = self._get_key()
            encrypt_file(path, key)
            self._log(f"File encrypted → {os.path.basename(path)}.enc", "ok")
        except Exception as e:
            self._log(f"Encrypt file failed — {e}", "err")

    def decrypt_file_dialog(self):
        path = filedialog.askopenfilename(title="Select a .enc file to decrypt")
        if not path:
            return
        try:
            key = self._get_key()
            decrypt_file(path, key)
            out = path[:-4] if path.endswith(".enc") else path + ".dec"
            self._log(f"File decrypted → {os.path.basename(out)}", "ok")
        except Exception as e:
            self._log(f"Decrypt file failed — {e}", "err")


if __name__ == "__main__":
    root = Tk()
    app = EncryptionApp(root)
    root.mainloop()