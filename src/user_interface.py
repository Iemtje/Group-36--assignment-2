"""
User interface functions for signup system.
"""

def get_username_input():
    """
    Prompt user for username and return cleaned input.
    """
    username = input("Enter your desired username: ").strip()
    return username


def display_signup_result(username, password, success):
    """
    Show registration outcome with appropriate messages.
    """
    print("\n" + "="*50)
    if success:
        print("✅ SIGNUP SUCCESSFUL!")
        print(f"\nUsername: {username}")
        print(f"Generated Password: {password}")
        print("Please save your password in a secure location.")
    else:
        print("❌ SIGNUP FAILED!")
        print("Unable to create account. Please try again.")
    print("="*50 + "\n")
