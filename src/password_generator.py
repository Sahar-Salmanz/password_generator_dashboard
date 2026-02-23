import random
import string
from abc import ABC, abstractmethod

import nltk
nltk.download('words')


class PasswordGenerator(ABC):
    """Abstract base class for password generators.
    """
    @abstractmethod
    def generate(self):
        """Subclasses should override this method to generate password.
        """
        pass


class PINGenerator(PasswordGenerator):
    """Generates a random PIN code consisting of digits only.
    """
    def __init__(self, length: int = 4):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    """Generates a random password consisting of letters, and optionally numbers and symbols.
    """
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.chars = string.ascii_letters
        if include_numbers:
            self.chars += string.digits
        if include_symbols:
            self.chars += string.punctuation
        
    def generate(self):
        return ''.join([random.choice(self.chars) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator): 
    """Generates a memorable password by combining random words from a given vocabulary, with options for capitalization and custom separators.
    """
    def __init__(
        self, 
        num_of_words: int = 4, 
        separator: str = '-', 
        capitalize: bool = False, 
        vocabulary : list = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        
        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.separator = separator
        self.capitalize = capitalize

    def generate(self):
        password_words = random.choices(self.vocabulary, k=self.num_of_words)
        if self.capitalize:
            password_words = [word.upper() for word in password_words]
        return self.separator.join(password_words)


# Test cases
def test_pin_generator():
    pin_gen = PINGenerator(length=4)
    pin = pin_gen.generate()
    print(f"Generated PIN: {pin}")
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)


def test_random_password_generator():
    random_gen = RandomPasswordGenerator(length=16, include_numbers=True, include_symbols=True)
    password = random_gen.generate()
    print(f"Generated Random Password: {password}")
    assert len(password) == 16
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)


def test_memorable_password_generator():
    memorable_gen = MemorablePasswordGenerator(num_of_words=4, separator='_', capitalize=True)
    memorable_pass = memorable_gen.generate()
    print(f"Generated Memorable Password: {memorable_pass}")
    assert len(memorable_pass.split('_')) == 4 
    assert all(word[0].isupper() for word in memorable_pass.split('_'))


def main():
    print("Testing PIN Generator...")
    test_pin_generator()
    print("Testing Random Password Generator...")
    test_random_password_generator()
    print("Testing Memorable Password Generator...")
    test_memorable_password_generator()
    print("All tests passed!")  


if __name__ == "__main__":
    main()