"""
Database simulation functions for signup system.
Contains functions 12-13 from the project specification.
"""

def load_existing_users():
    """
    Return a list of existing usernames.
    """
    return [
        "admin",
        "user123",
        "testuser",
        "john_doe",
        "alice",
        "bob",
        "charlie",
        "demo",
        "guest",
        "sample"
    ]


def add_user_to_database(username, password, user_database):
    """
    Add a new username to the user database list and return the updated database.
    """
    user_database.append(username)
    return user_database

    user_database.append(username)
    
    # Return updated database
    return user_database 
