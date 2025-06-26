import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from username_validation import validate_username_length, validate_username_characters, check_username_exists
from password_generation import generate_secure_password, validate_password_requirements
from database import load_existing_users


class TestInitialCases(unittest.TestCase):

    def test_validate_username_length_ValidInput_ReturnsTrue(self):
        valid_username = "testuser"
        result = validate_username_length(valid_username)
        self.assertTrue(result)

        min_valid = "abc"
        max_valid = "a" * 20

        self.assertTrue(validate_username_length(min_valid))
        self.assertTrue(validate_username_length(max_valid))

    def test_generate_secure_password_ValidLength_MeetsRequirements(self):
        password_length = 12
        generated_password = generate_secure_password(password_length)
        self.assertEqual(len(generated_password), password_length)
        self.assertTrue(validate_password_requirements(generated_password))
        self.assertIsInstance(generated_password, str)

    def test_check_username_exists_ExistingUser_ReturnsTrue(self):
        user_database = load_existing_users()

        existing_username = "admin"
        result = check_username_exists(existing_username, user_database)
        self.assertTrue(result)

        uppercase_existing = "ADMIN"
        result_case = check_username_exists(uppercase_existing, user_database)
        self.assertTrue(result_case)

        non_existing_username = "definitely_not_existing_user_12345"
        result_not_exist = check_username_exists(non_existing_username, user_database)
        self.assertFalse(result_not_exist)


if __name__ == '__main__':
    unittest.main()
