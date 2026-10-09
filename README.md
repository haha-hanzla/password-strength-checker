# Password Strength Checker

A simple Python program that checks how strong a password is. It gives a score out of 7, a rating (**Weak**, **Medium** or **Strong**) and tips to make the password better.

> This project is for learning purposes. The password you type is hidden and is **never saved or sent anywhere**.

## Features

- Hidden password input (nothing shows on screen while typing)
- Checks the length (8+ and 12+ characters)
- Checks for lowercase, uppercase, numbers and special characters
- Compares the password with a list of common passwords
- Warns about repeated characters like `aaa`
- Gives a score, a rating and helpful tips
- Can check many passwords in one run

## What You Need

- Python 3 (no extra libraries needed)

## How to Use

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
python password_checker.py
```

Type a password and press Enter. Type `q` to quit.

## Example Output

```
========================================
   PASSWORD STRENGTH CHECKER
========================================
Type a password to check it (it will be hidden).
Type 'q' to quit.

Enter password:

----------------------------------------
Length : 8 characters
Score  : 4 / 7
Rating : MEDIUM
----------------------------------------
Tips to improve:
 - 12 or more characters is even better.
 - Add uppercase letters (A-Z).
 - Add special characters like ! @ # $ %.
```

## How the Score Works

| Check | Points |
|-------|--------|
| 8 or more characters | +1 |
| 12 or more characters | +1 |
| Has lowercase letters | +1 |
| Has uppercase letters | +1 |
| Has numbers | +1 |
| Has special characters | +1 |
| Not a common password | +1 |
| Repeats a character 3 times in a row | -1 |

| Score | Rating |
|-------|--------|
| 0 - 3 | WEAK |
| 4 - 5 | MEDIUM |
| 6 - 7 | STRONG |

A password from the common password list always gets a score of 0.

## Project Files

```
password-strength-checker/
├── password_checker.py   # main program
├── requirements.txt      # libraries needed (none)
├── .gitignore
└── README.md
```

## What I Learned

- Using `if`, `elif` and `else` to make decisions
- Looping through the characters of a string
- Using lists and functions
- Using the `string` and `getpass` modules

## Tips for a Good Password

- Use a long password or a passphrase (for example, 4 random words)
- Do not use your name, birthday or common words
- Use a different password for every account
- Use a password manager

## Future Ideas

- Estimate how long it would take to crack the password
- Load a bigger list of common passwords from a file
- Add a password generator
- Build a simple GUI with Tkinter

## License

MIT License
