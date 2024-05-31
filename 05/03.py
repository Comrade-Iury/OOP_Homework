def check_password(right_password: str):
    def certain_check_password(func):
        password = input("Enter password: ")
        if password == right_password:
            return func
        print("Access denied")
        return lambda x: None
    return certain_check_password

