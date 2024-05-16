import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/users.txt'):
            with open('data/users.txt', 'w') as file:
                pass 
        with open('data/users.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                self.users[username] = password

    def save_users(self):
        with open('data/users.txt', 'w') as file:
            for username, password in self.users.items():
                file.write(f"{username},{password}\n")

    def validate_username(self, username):
        if len(username) < 4:
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True

    def register(self, username, password):
        if username in self.users:
            print ("Username already exist!")
            return False
        if not self.validate_username(username) or not self.validate_password(password):
            print("=======================================================================")
            print ("Username or password does not meet the requirements.")
            return False
        self.users[username] = password
        self.save_users()
        return True

    def login(self, username, password):
        if username not in self.users:
            print("=======================================================================")
            print ("Username not found.")
            return False 
        if self.users[username] != password:
            print("=======================================================================")
            print ("Incorrect Password.")
            return False 
        return True