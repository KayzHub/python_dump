def password_checker():
    import re
    import getpass
    print("Welcome to my password checker.")
    print("Please get ready to enter your password.")

    password_pattern = re.compile(
    r"""
    ^                   # start of string
    (?=.*[A-Z])         # at least one uppercase letter
    (?=.*[a-z])         # at least one lowercase letter
    (?=.*[@#$%])        # at least one special character (@, #, $, %)
    .{8,}               # at least 8 characters total
    $                   # end of string
    """,
    re.VERBOSE
)
    #The above "password_pattern" checks that the password is at least 8 characters long...
    #At and contains a special character that's either one of [@, #, $, %]
    while True:
        print("Please note that your password has to be at least 8 characters long and must contain one of the following special characters - '@', '#', '$' or '%'")
        user_password = getpass.getpass("Please enter your strong password: ")
        if not re.match(password_pattern, user_password):
            print("you have entered a weak password, please try again: ")
        else:
            print("Thank you for creating a strong password!")
            break

password_checker()
