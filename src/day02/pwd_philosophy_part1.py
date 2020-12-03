import re


def get_and_format_input():
    policies_and_passwords = []
    with open("pwd_philosophy_input.txt", "r") as passwords_file:
        for password in passwords_file.readlines():
            policy_and_password = re.search("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", password.strip()).groups()
            policies_and_passwords.append(policy_and_password)

    return policies_and_passwords


def count_valid_passwords():
    policies_and_passwords = get_and_format_input()
    valid_password_count = 0

    for policy_and_password in policies_and_passwords:
        min_count, max_count, letter, password = policy_and_password
        min_count = int(min_count)
        max_count = int(max_count)
        letter_count = 0

        for c in password:
            if c == letter:
                letter_count += 1

        if min_count <= letter_count <= max_count:
            valid_password_count += 1

    return valid_password_count


def main():
    print(count_valid_passwords())


if __name__ == "__main__":
    main()
