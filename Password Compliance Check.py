import re
import tkinter as tk
from tkinter import messagebox

def check_password_compliance(password, username, common_passwords, min_length=10, require_uppercase=True, require_digit=True, require_special=True):
    states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut",
        "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa",
        "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
        "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire",
        "new jersey", "new mexico", "new york", "north carolina", "north dakota", "ohio", "oklahoma",
        "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota", "tennessee",
        "texas", "utah", "vermont", "virginia", "washington", "west virginia", "wisconsin", "wyoming"
    ]

    state_pattern = r'(' + '|'.join(states) + r')'
    
    compliant = True
    messages = []

    if username.lower() in password.lower():
        compliant = False
        messages.append("- Password must not contain your username.")

    if re.search(state_pattern, password, flags=re.IGNORECASE):
        compliant = False
        messages.append("- Password must not contain the name of any of the 50 United States.")

    if len(password) < min_length:
        compliant = False
        messages.append("- Password length must be at least {} characters.".format(min_length))

    if require_uppercase and not re.search(r'[A-Z]', password):
        compliant = False
        messages.append("- Password must contain at least one uppercase letter.")

    if require_digit and not re.search(r'\d', password):
        compliant = False
        messages.append("- Password must contain at least one digit.")

    if require_special and not re.search(r'[!@#$%^&*(),]', password):
        compliant = False
        messages.append("- Password must contain at least one special character.")

    if password.lower() in common_passwords:
        compliant = False
        messages.append("- Password is too common and easy to guess.")
    
    for i in range(len(password) - 3):
        segment = password[i:i+4]
        if segment.isdigit() and (segment in '0123456789' or segment in '9876543210'):
            compliant = False
            messages.append("- Password must not contain sequences like '1234' or '4321'.")
            break

    for i in range(len(password) - 3):
        if password[i:i+4] == password[i] * 4:
            compliant = False
            messages.append("- Password must not contain repeated characters.")
            break

    if compliant:
        return True, "Password meets all complexity requirements."
    else:
        return False, "Password does not meet the following requirements:\n" + "\n".join(messages)

def check_password():
    username = username_entry.get()
    password = password_entry.get()
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123", "password1"]

    compliant, message = check_password_compliance(password, username, common_passwords)
    messagebox.showinfo("Password Compliance", message)

app = tk.Tk()
app.title("Password Compliance Checker")

tk.Label(app, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(app)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(app, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

check_button = tk.Button(app, text="Check Password", command=check_password)
check_button.grid(row=2, column=0, columnspan=2, pady=20)

app.mainloop()








