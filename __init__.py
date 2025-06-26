"""Password Generator Application

This package provides tools for generating secure, random passwords with user-defined constraints,
and includes functionality for validating usernames and managing user sign-ups.
"""

# Password generation
from .password_generator import generate_password

# Signup and user management utilities
from .signup import (
    is_valid_username,
    contains_forbidden_words,
    is_duplicate_username,
)

# Password strength assessment
from .Strength_checker import assess_password_strength

__all__ = [
    # Password generation
    "generate_password",

    # Username validation
    "is_valid_username",
    "contains_forbidden_words",
    "is_duplicate_username",

    # Password strength
    "assess_password_strength",
]
