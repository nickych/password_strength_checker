import tkinter as tk
from tkinter import scrolledtext
import re

def check_password_strength(password, log):
    log.delete(1.0, tk.END)
    log.insert(tk.END, "Checking password strength...\n")
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        log.insert(tk.END, "[WARNING] Password should be at least 8 characters long.\n")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        log.insert(tk.END, "[WARNING] Password should contain at least one uppercase letter.\n")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        log.insert(tk.END, "[WARNING] Password should contain at least one lowercase letter.\n")
    
    if re.search(r"[0-9]", password):
        score += 1
    else:
        log.insert(tk.END, "[WARNING] Password should contain at least one number.\n")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        log.insert(tk.END, "[WARNING] Password should contain at least one special character.\n")
    
    strength = "Weak" if score <= 2 else "Moderate" if score <= 4 else "Strong"
    log.insert(tk.END, f"\nPassword Strength: {strength}\n")

def toggle_theme(root, log, entry, check_button, theme_button):
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        root.configure(bg="#1e1e1e")
        log.configure(bg="#252526", fg="white", insertbackground="white")
        entry.configure(bg="#444", fg="white")
        check_button.configure(bg="#555", fg="white")
        theme_button.configure(bg="#333", fg="white", text="Light Mode")
    else:
        root.configure(bg="white")
        log.configure(bg="white", fg="black", insertbackground="black")
        entry.configure(bg="#ddd", fg="black")
        check_button.configure(bg="#ccc", fg="black")
        theme_button.configure(bg="#bbb", fg="black", text="Dark Mode")

def main():
    global dark_mode
    dark_mode = False
    
    root = tk.Tk()
    root.title("Chibz Password Strength Checker")
    root.geometry("500x300")
    
    entry_label = tk.Label(root, text="Enter Password:")
    entry_label.pack()
    entry = tk.Entry(root, width=40, show="*")
    entry.pack(pady=10)
    
    log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
    log.pack(pady=10)
    
    check_button = tk.Button(root, text="Check Password", command=lambda: check_password_strength(entry.get(), log))
    check_button.pack()
    
    theme_button = tk.Button(root, text="Dark Mode", command=lambda: toggle_theme(root, log, entry, check_button, theme_button))
    theme_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
