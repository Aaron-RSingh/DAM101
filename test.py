import random

def test_random():
    """Generate a random number between 1 and 100"""
    number = random.randint(1, 100)
    print(f"Random number: {number}")
    return number

if __name__ == "__main__":
    test_random()