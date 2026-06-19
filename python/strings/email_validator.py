email = input("Enter an email address: ")
has_at = "@" in email
has_dot = "." in email
not_starting_ending_with_symbols = not email.startswith(("@", ".")) and not email.endswith(("@", "."))
if has_at and has_dot and not_starting_ending_with_symbols:
    # extra check — @ should come before the last dot
    at_index = email.index("@")
    dot_index = email.rfind(".")
    if at_index < dot_index:
        print(email, "looks like a valid email")
    else:
        print(email, "is NOT a valid email")
else:
    print(email, "is NOT a valid email")