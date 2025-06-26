"""
User interface functions for signup system.
"""

def get_username_input():
    return input("Enter your desired username: ").strip()


def display_signup_result(username, password, success):
    print("\n" + "="*50)
    if success:
        print("✅ SIGNUP SUCCESSFUL!")
        print(f"Username: {username}")
        print(f"Generated Password: {password}")
        print("Please save your password in a secure location.")
    else:
        print("❌ SIGNUP FAILED!")
        print("Unable to create account. Please try again.")
    print("="*50 + "\n")
