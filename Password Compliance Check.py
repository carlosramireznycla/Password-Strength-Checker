import re

def check_password_compliance(password, username, common_passwords, min_length=10, require_uppercase=True, require_digit=True, require_special=True):
    # List of state names
    states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut",
        "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa",
        "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
        "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire",
        "new jersey", "new mexico", "new york", "north carolina", "north dakota", "ohio", "oklahoma",
        "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota", "tennessee",
        "texas", "utah", "vermont", "virginia", "washington", "west virginia", "wisconsin", "wyoming"
    ]

    # Construct a regex pattern to match any state name, case-insensitive
    state_pattern = r'(' + '|'.join(states) + r')'
    
    # Initialize compliance status and messages
    compliant = True
    messages = []

    # Check if password contains the username
    if username.lower() in password.lower():
        compliant = False
        messages.append("- Password must not contain your username.")

    # Check for state names
    if re.search(state_pattern, password, flags=re.IGNORECASE):
        compliant = False
        messages.append("- Password must not contain the name of any of the 50 United States.")

    if len(password) < min_length:
        compliant = False
        messages.append(f"- Password length must be at least {min_length} characters.")

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
    
    # Check for ascending or descending sequences like "1234" or "4321"
    for i in range(len(password) - 3):
        segment = password[i:i+4]
        if segment.isdigit() and (segment in '0123456789' or segment in '9876543210'):
            compliant = False
            messages.append("- Password must not contain sequences like '1234' or '4321'.")
            break

    # Check for repeated characters like "aaaa"
    for i in range(len(password) - 3):
        if password[i:i+4] == password[i] * 4:
            compliant = False
            messages.append("- Password must not contain repeated characters.")
            break

    if compliant:
        return True, "Password meets all complexity requirements."
    else:
        return False, "Password does not meet the following requirements:\n" + "\n".join(messages)

# Example usage:
username = input("Enter your username: ")
password = input("Enter your password: ")
common_passwords = ["password", "123456", "123456789", "qwerty", "abc123", "password1"]  # Add more common passwords as needed
compliant, message = check_password_compliance(password, username, common_passwords)
print(message)







