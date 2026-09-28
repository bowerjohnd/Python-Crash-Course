from pathlib import Path

# path = Path('pi_digits.txt')
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

def check_for_birthday_in_pi(birthday):
    if birthday in pi_string:
        index = pi_string.find(birthday)
        print("Your birthday\033[32m DOES\033[0m appear in the first million digits of pi! " +
            f"between\033[32m {index}-{index + len(birthday)-1}\033[0m" )
    else:
        print("Your birthday\033[33m DOES NOT\033[0m appear in the first million digits of pi.\n")


birthday = input("\nEnter your birthday, in the form mmddyy: ")

try:
    checkint = int(birthday)
    check_for_birthday_in_pi(birthday)
except ValueError:
    print(f"Your input, {birthday}, contains non-numbers.")
    print("Please use numbers only. For example: 012399")

