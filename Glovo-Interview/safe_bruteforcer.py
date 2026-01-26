from fake_auth_system import login

def brute_force(username, password_list):
    successful_logins = []

    for password in password_list:
        print(f"Trying: {username} / {password}")

        if login(username, password):
            print(f"[SUCCESS] Found password: {password}")
            successful_logins.append((username, password))

    return successful_logins


if __name__ == "__main__":
    username_to_test = "admin"

    passwords = [
        "123456",
        "password",
        "admin",
        "admin123",
        "letmein"
    ]

    results = brute_force(username_to_test, passwords)

    with open("successful_logins.txt", "w") as file:
        for user, pwd in results:
            file.write(f"{user}:{pwd}\n")

    print("\nSaved successful logins to successful_logins.txt")