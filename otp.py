"""A file to generate a unique otp code."""

import random
import string
from typing import List

# List to keep track of all previously generated OTP codes
used_otp: List[str] = []


def generate_otp():
    """This function generates a unique 6-character OTP code using a set of characters and checks if it
    already exists in a list of used codes.

    Returns:
      the generated OTP code as a string.
    """
    # Define the character set for the OTP code
    characters = string.ascii_letters + string.digits

    while True:
        # Generate a random 6-character code using the character set
        otp = "".join(random.choice(characters) for i in range(6))

        # Check if the OTP code already exists in the list of used codes
        if otp not in used_otp:
            # If the OTP code is unique, add it to the list of used codes and return it
            used_otp.append(otp)
            print("Your OTP is:", otp)

            return otp


if __name__ == "__main__":
    otp = generate_otp()
    print(otp)
