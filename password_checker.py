# Password Strength Checker
# -------------------------
# This program checks how strong a password is.
# It gives a score, a rating (Weak / Medium / Strong)
# and tips to make the password better.
#
# NOTE: The password is never saved or printed anywhere.

import string

# A small list of very common passwords (hackers try these first!)
COMMON_PASSWORDS = [
    "password", "123456", "12345678", "123456789", "qwerty",
    "abc123", "111111", "iloveyou", "admin", "welcome",
    "letmein", "monkey", "dragon", "football", "login",
    "password1", "passw0rd", "123123", "000000", "qwerty123",
]


def check_password(password):
    """
    Check the password and return two things:
    1. score (a number from 0 to 7)
    2. tips (a list of messages to help the user)
    """
    score = 0
    tips = []

    # 1. Check the length
    if len(password) >= 8:
        score = score + 1
    else:
        tips.append("Use at least 8 characters.")

    if len(password) >= 12:
        score = score + 1
    else:
        tips.append("12 or more characters is even better.")

    # 2. Check what kinds of characters are used
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for character in password:
        if character in string.ascii_lowercase:
            has_lower = True
        elif character in string.ascii_uppercase:
            has_upper = True
        elif character in string.digits:
            has_digit = True
        elif character in string.punctuation:
            has_special = True

    if has_lower:
        score = score + 1
    else:
        tips.append("Add lowercase letters (a-z).")

    if has_upper:
        score = score + 1
    else:
        tips.append("Add uppercase letters (A-Z).")

    if has_digit:
        score = score + 1
    else:
        tips.append("Add numbers (0-9).")

    if has_special:
        score = score + 1
    else:
        tips.append("Add special characters like ! @ # $ %.")

    # 3. Check if it is a common password
    if password.lower() in COMMON_PASSWORDS:
        score = 0  # a common password is always weak
        tips.append("This is a very common password. Do not use it!")
    else:
        score = score + 1

    # 4. Check for repeated characters like "aaa" or "111"
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            score = score - 1
            tips.append("Avoid repeating the same character 3 times in a row.")
            break  # we only need to warn once

    # The score should never go below 0
    if score < 0:
        score = 0

    return score, tips


def get_rating(score):
    """Change the score into a word."""
    if score <= 3:
        return "WEAK"
    elif score <= 5:
        return "MEDIUM"
    else:
        return "STRONG"


def show_result(password):
    """Check the password and print the result."""
    score, tips = check_password(password)
    rating = get_rating(score)

    print()
    print()
    print("Length :", len(password), "characters")
    print("Score  :", score, "/ 7")
    print("Rating :", rating)
    print()

    if len(tips) > 0:
        print("Tips to improve:")
        for tip in tips:
            print(" -", tip)
    else:
        print("Great job! No tips needed.")
    print()


def main():
    print()
    print("   PASSWORD STRENGTH CHECKER")
    print()
    print("Type a password to check it (it will be hidden).")
    print("Type 'q' to quit.")
    print()

    while True:
        password = input("Enter password: ")

        if password == "q":
            print("Goodbye!")
            break

        if password == "":
            print("You did not type anything. Try again.")
            continue

        show_result(password)


if __name__ == "__main__":
    main()
