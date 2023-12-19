import re
import time

def is_reverse_consecutive(s):
    return any(ord(s[i]) - 1 == ord(s[i + 1]) and ord(s[i + 1]) - 1 == ord(s[i + 2]) for i in range(len(s) - 2))

def is_consecutive(s):
    return any(ord(s[i]) + 1 == ord(s[i + 1]) and ord(s[i + 1]) + 1 == ord(s[i + 2]) for i in range(len(s) - 2))

def contains_non_alphanumeric(s):
    return any(not c.isalnum() for c in s)

def contains_uppercase(s):
    return any(c.isupper() for c in s)

def contains_lowercase(s):
    return any(c.islower() for c in s)

def contains_digit(s):
    return any(c.isdigit() for c in s)

def contains_repeated_character(s):
    return any(s[i] == s[i+1] == s[i+2] for i in range(len(s) - 2))

def valid_password(password):
    if len(password) < 8:
        return "too short"
    if len(password) > 72: # BCRYPT max length 72
        return "too long"
    if not contains_uppercase(password):
        return "must contain uppercase"
    if not contains_lowercase(password):
        return "must contain lowercase"
    if not contains_digit(password):
        return "must contain digit"
    if not contains_non_alphanumeric(password):
        return "must contain non alphanumeric"
    if contains_repeated_character(password):
        return "no repeated charakters e.g. aaa, 111"
    if is_consecutive(password):
        return "no consecutive chars e.g. abc, 123"
    if is_reverse_consecutive(password):
        return "no reverse consecutive chars e.g. cba, 321"
    return "valid password"


def main():
    with open("xato-net-10-million-passwords-1000000.txt", "r") as source_file:
        with open("8-plus.txt", "w") as target_file:
            for password in source_file:
                password = password.rstrip("\n")
                if valid_password(password) == "valid password":
                    target_file.write(password+"\n")

def makePHP():
    with open("8-plus.txt", "r") as source_file:
        with open("8-plus.php", "w") as target_file:
            target_file.write("<?php\n")
            target_file.write("$passwords = array(\n")
            for password in source_file:
                password = password.replace("'", "\\'")
                password = password.rstrip("\n")
                target_file.write("'" + password + "',\n")
            target_file.write(");\n")
            # target_file.write("?>\n")

if __name__ == '__main__':
    start_time = time.time()
    main()
    makePHP()
    print("--- %s seconds ---" % (time.time() - start_time))