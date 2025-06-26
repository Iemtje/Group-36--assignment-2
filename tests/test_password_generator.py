import string
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from password_generator import generate_password 


def test_default_length():
    """Test that default password length is 13."""
    pw = generate_password()
    assert len(pw) == 13

def test_custom_length():
    """Test that custom password length works."""
    pw = generate_password(length=20)
    assert len(pw) == 20

def test_only_digits():
    """Test password generation with only digits."""
    pw = generate_password(
        length=15,
        include_uppercase=False,
        include_lowercase=False,
        include_special=False,
        include_digits=True,
        required_types=True
    )
    assert len(pw) == 15
    assert all(ch in string.digits for ch in pw)

def test_required_types():
    """Test that required character types are included when required_types=True."""
    pw = generate_password(
        length=8,
        include_uppercase=True,
        include_lowercase=True,
        include_digits=True,
        include_special=False,
        required_types=True
    )
    assert len(pw) == 8
    assert any(ch in string.ascii_uppercase for ch in pw)
    assert any(ch in string.ascii_lowercase for ch in pw)
    assert any(ch in string.digits for ch in pw)

def test_no_char_types_error():
    """Test that ValueError is raised when no character types are selected."""
    with pytest.raises(ValueError, match="At least one character type must be selected"):
        generate_password(
            include_uppercase=False,
            include_lowercase=False,
            include_digits=False,
            include_special=False
        )

def test_length_too_short_error():
    """Test that ValueError is raised when length is too short for required types."""
    with pytest.raises(ValueError, match="Length too short for required character types"):
        generate_password(
            length=2,  # Too short for 3 required character types
            include_uppercase=True,
            include_lowercase=True,
            include_digits=True,
            include_special=False,
            required_types=True
        )

def test_exclude_similar():
    """Test that similar characters are excluded when exclude_similar=True."""
    pw = generate_password(
        length=20,
        exclude_similar=True,
        include_digits=True,
        include_uppercase=True,
        include_lowercase=True
    )
    similar_chars = "0O1lI"
    assert not any(ch in similar_chars for ch in pw)

def test_custom_special_chars():
    """Test password generation with custom special characters."""
    custom_special = "@#$%"
    pw = generate_password(
        length=20,
        special_chars=custom_special,
        include_special=True,
        include_uppercase=False,
        include_lowercase=False,
        include_digits=False
    )
    assert all(ch in custom_special for ch in pw)

def test_debug_output(capsys):
    """Test that debug output shows character sets when debug=True."""
    generate_password(debug=True)
    captured = capsys.readouterr()
    assert "Included char sets:" in captured.out

def test_generate_password_character_types():
    """Test password generation with specific character types."""
    # Test with only uppercase
    password = generate_password(
        length=10,
        include_uppercase=True,
        include_lowercase=False,
        include_digits=False,
        include_special=False
    )
    assert all(c in string.ascii_uppercase for c in password)
    
    # Test with only digits
    password = generate_password(
        length=10,
        include_uppercase=False,
        include_lowercase=False,
        include_digits=True,
        include_special=False
    )
    assert all(c in string.digits for c in password)

def test_generate_password_invalid_inputs():
    """Test password generation with invalid inputs."""
    # Test with no character types
    with pytest.raises(ValueError, match="At least one character type must be selected"):
        generate_password(
            include_uppercase=False,
            include_lowercase=False,
            include_digits=False,
            include_special=False
        )
    
    # Test with invalid length
    with pytest.raises(ValueError, match="Password length must be positive"):
        generate_password(length=0)
    
    # Test with length too short for required types
    with pytest.raises(ValueError, match="Length too short for required character types"):
        generate_password(length=2, required_types=True)

def test_generate_password_exclude_similar():
    """Test password generation with similar characters excluded."""
    similar_chars = "0O1lI"
    password = generate_password(
        length=20,
        exclude_similar=True
    )
    assert not any(c in similar_chars for c in password)

def test_generate_password_custom_special():
    """Test password generation with custom special characters."""
    custom_special = "@#$%"
    password = generate_password(
        length=20,
        special_chars=custom_special
    )
    special_chars_in_password = [c for c in password if c in custom_special]
    assert len(special_chars_in_password) > 0
    assert all(c in custom_special for c in special_chars_in_password) 
