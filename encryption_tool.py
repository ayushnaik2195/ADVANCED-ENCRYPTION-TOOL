import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# -----------------------------
# Generate or Load Key
# -----------------------------
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return open("secret.key", "rb").read()

key = load_key()
cipher = Fernet(key)

# -----------------------------
# Encrypt File
# -----------------------------
def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

    messagebox.showinfo("Success", "File Encrypted Successfully!")

# -----------------------------
# Decrypt File
# -----------------------------
def decrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    try:
        with open(file_path, "rb") as file:
            data = file.read()

        decrypted_data = cipher.decrypt(data)

        with open(file_path, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", "File Decrypted Successfully!")
    except:
        messagebox.showerror("Error", "Invalid Key or File!")

# -----------------------------
# GUI Design
# -----------------------------
root = tk.Tk()
root.title("Advanced Encryption Tool (AES-256)")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="🔐 Advanced Encryption Tool", font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(root, text="Encrypt File", width=20, command=encrypt_file).pack(pady=10)
tk.Button(root, text="Decrypt File", width=20, command=decrypt_file).pack(pady=10)

tk.Label(root, text="AES-256 File Encryption", font=("Arial", 10)).pack(pady=20)

root.mainloop()
