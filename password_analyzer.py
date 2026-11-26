import tkinter as tk
from tkinter import ttk
import re
import math
import random
import string
from tkinter import messagebox
# ------------------ Load Leaked Passwords ------------------

def load_leaked_passwords():
    try:
        with open("leaked_passwords.txt", "r") as file:
            return set(line.strip().lower() for line in file)
    except FileNotFoundError:
        return set()

LEAKED_PASSWORDS = load_leaked_passwords()


# ------------------ Entropy Calculation ------------------

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"[0-9]", password):
        charset += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)

    return round(entropy, 2)


# ------------------ Password Analysis ------------------

def analyze_password(password):

    score = 0
    suggestions = []

    # Length
    if len(password) >= 12:
        score += 20
    else:
        suggestions.append("Use at least 12 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 10
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 10
    else:
        suggestions.append("Add lowercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 10
    else:
        suggestions.append("Include numbers.")

    # Special Characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        suggestions.append("Use special characters.")

    # Common Password
    if password.lower() in LEAKED_PASSWORDS:
        suggestions.append("Password found in leaked password database.")
    else:
        score += 15

    # Weak Patterns
    weak_patterns = [
        "123",
        "password",
        "admin",
        "qwerty",
        "abc",
        "111",
        "000"
    ]

    if any(p in password.lower() for p in weak_patterns):
        suggestions.append("Avoid predictable patterns.")
    else:
        score += 10

    # Entropy
    entropy = calculate_entropy(password)

    if entropy >= 60:
        score += 10

    # Strength
    if score <= 20:
        strength = "Very Weak"
        color = "#ff0000"

    elif score <= 40:
        strength = "Weak"
        color = "#ff6600"

    elif score <= 60:
        strength = "Moderate"
        color = "#d4a017"

    elif score <= 80:
        strength = "Strong"
        color = "#008000"

    else:
        strength = "Very Strong"
        color = "#006400"

    return score, entropy, strength, color, suggestions


# ------------------ Button Functions ------------------

def check_password():

    password = password_entry.get()

    score, entropy, strength, color, suggestions = analyze_password(password)

    progress["value"] = score

    strength_label.config(
        text=f"Strength : {strength}",
        fg=color
    )

    score_label.config(
        text=f"Score : {score}/100"
    )

    entropy_label.config(
        text=f"Entropy : {entropy} bits"
    )

    length_label.config(
        text=f"Length : {len(password)} characters"
    )

    suggestion_box.delete("1.0", tk.END)

    if suggestions:
        for item in suggestions:
            suggestion_box.insert(tk.END, "• " + item + "\n")
    else:
        suggestion_box.insert(
            tk.END,
            "Excellent Password!\nNo improvements required."
        )


def clear_all():

    password_entry.delete(0, tk.END)

    progress["value"] = 0

    strength_label.config(
        text="Strength :"
    )

    score_label.config(
        text="Score :"
    )

    entropy_label.config(
        text="Entropy :"
    )

    length_label.config(
        text="Length :"
    )

    suggestion_box.delete("1.0", tk.END)


def toggle_password():

    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def generate_password():
    length = 16

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()_+-="
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )
# ------------------ GUI ------------------

root = tk.Tk()
root.title("AI Password Strength Analyzer")
root.geometry("600x700")
root.configure(bg="#F4F8FB")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="AI Password Strength Analyzer",
    font=("Arial", 20, "bold"),
    bg="#F4F8FB",
    fg="#1F3C88"
)
title.pack(pady=(20,5))

subtitle = tk.Label(
    root,
    text="Analyze password strength using rule-based security checks",
    font=("Arial", 10),
    bg="#F4F8FB",
    fg="gray"
)
subtitle.pack()

# Password Label
password_label = tk.Label(
    root,
    text="Enter Password",
    font=("Arial", 12, "bold"),
    bg="#F4F8FB"
)
password_label.pack(pady=(20,5))

# Password Entry
password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14),
    show="*",
    relief="solid",
    bd=2
)
password_entry.pack()

# Show Password Checkbox
show_password = tk.BooleanVar()

show_checkbox = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_password,
    command=toggle_password,
    bg="#F4F8FB",
    font=("Arial",10)
)
show_checkbox.pack(pady=5)

# Analyze Button
analyze_button = tk.Button(
    root,
    text="Analyze Password",
    font=("Arial",12,"bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=check_password
)
analyze_button.pack(pady=10)

# Clear Button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial",12,"bold"),
    bg="#E53935",
    fg="white",
    width=20,
    command=clear_all
)
clear_button.pack()
generate_button = tk.Button(
    root,
    text="Generate Strong Password",
    font=("Arial",12,"bold"),
    bg="#1976D2",
    fg="white",
    width=25,
    command=generate_password
)

generate_button.pack(pady=8)

# Progress Bar
progress = ttk.Progressbar(
    root,
    length=350,
    mode="determinate",
    maximum=100
)
progress.pack(pady=20)
generate_button.pack(pady=8)

copy_button = tk.Button(
    root,
    text="Copy Password",
    font=("Arial",12,"bold"),
    bg="#8E24AA",
    fg="white",
    width=25,
    command=copy_password
)

copy_button.pack(pady=5)

# Strength Label
strength_label = tk.Label(
    root,
    text="Strength :",
    font=("Arial",14,"bold"),
    bg="#F4F8FB"
)
strength_label.pack()

# Score Label
score_label = tk.Label(
    root,
    text="Score :",
    font=("Arial",12),
    bg="#F4F8FB"
)
score_label.pack()

# Entropy Label
entropy_label = tk.Label(
    root,
    text="Entropy :",
    font=("Arial",12),
    bg="#F4F8FB"
)
entropy_label.pack()

# Length Label
length_label = tk.Label(
    root,
    text="Length :",
    font=("Arial",12),
    bg="#F4F8FB"
)
length_label.pack()

# Suggestions Heading
suggestions_title = tk.Label(
    root,
    text="Suggestions",
    font=("Arial",13,"bold"),
    bg="#F4F8FB"
)
suggestions_title.pack(pady=(20,5))

# Suggestions Box
suggestion_box = tk.Text(
    root,
    width=60,
    height=10,
    font=("Arial",11),
    relief="solid",
    bd=2
)
suggestion_box.pack(pady=5)
# ------------------ Run Application ------------------

root.mainloop()