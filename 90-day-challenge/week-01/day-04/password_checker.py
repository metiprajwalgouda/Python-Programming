"""Password rules: take a password string and check that it has at least 8 characters, contains a digit, contains an uppercase letter, and contains a special character such as !@#$. Print which rules failed. You can use a for loop over the characters, since you did loops yesterday."""
print("""
Password must be 8 characters
password should contain numbers in it
at least one upper case must be present in it
password must contan special character
""")
password=input("Enter Password : ")
if len(password)>=8:
    if password.isdigit():
        print()
    else:
        print("Password must contain any digit in it.")
else:
    print("Password must be 8 character.")