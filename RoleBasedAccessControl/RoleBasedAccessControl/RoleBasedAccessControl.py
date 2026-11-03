users = {
    "Alice": {"role": "admin"},
    "Bob": {"role": "user"},
    }

def admin_dashboard(role):
    if role == "admin":
        print("Welcome to the admin dashboard!")
    else:
        print("Access denied! You do not have admin privileges.")

def user_dashboard(role):
    if role == "user":
        print("Welcome to the user dashboard!")
    else:
        print("Access denied! You do not have user privileges.")

def main():
    username = "Bob"

    if username in users:
        print("Login successful!")
        role = users[username]["role"]
        print("Role:", role)

        admin_dashboard(role)
        user_dashboard(role)
    else:
        print("Login failed! User not found.")


if __name__ == "__main__":
    main()


