# validate user input
# 1. username is no more than 12 character
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username is invalid (more than 12 characters)")
elif username.count(" ") > 0:
    print("Username is invalid (contain space/s)")
elif username.isalpha() != True:
    print("Username is invalid (contain digit/s)")
else:
    print("Username is correct")