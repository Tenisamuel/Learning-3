USERS = {
    "alice": "password123",
    "bob": "qwerty",
    "admin": "admin123"
}

def login(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False