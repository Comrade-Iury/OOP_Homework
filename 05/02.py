def check_password(func):
    right_password = "ah-618"
    password = input("Enter password: ")
    if password == right_password:
        return func
    print("Access denied")
    return lambda x: None

