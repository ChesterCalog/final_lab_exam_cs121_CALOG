from utils.dice_game import DiceGame
  
def main():
    try:
        game = DiceGame()
        while True:
            END = '\33[0m'
            COLOR_CYAN = '\33[36m'
            
            print(COLOR_CYAN + """
 ______   ___   _______  _______    _______  _______  __   __  _______ 
|      | |   | |       ||       |  |       ||   _   ||  |_|  ||       |
|  _    ||   | |       ||    ___|  |    ___||  |_|  ||       ||    ___|
| | |   ||   | |       ||   |___   |   | __ |       ||       ||   |___ 
| |_|   ||   | |      _||    ___|  |   ||  ||       ||       ||    ___|
|       ||   | |     |_ |   |___   |   |_| ||   _   || ||_|| ||   |___ 
|______| |___| |_______||_______|  |_______||__| |__||_|   |_||_______| \n""" + END)
            print("============================ ♡ MAIN MENU ♡ ============================")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                register_user(game)
            elif choice == '2':
                login_user(game)
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print("An error occurred:", e)

def register_user(game):
    try:
        print("============================ ♡ REGISTER ♡ =============================")
        username = input("Enter username (must be 4 characters or above): ")
        password = input("Enter password (must be 8 characters or above): ")
        if game.user_manager.register(username, password):
            print("=======================================================================")
            print("Registration successful.")
        else:
            print("=======================================================================")
            print("Registration failed. Please try again.")
    except Exception as e:
        print("=======================================================================")
        print("An error occurred:", e)

def login_user(game):
    try:                                                 
        print("============================== ♡ LOGIN ♡ ==============================")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if game.user_manager.login(username, password):
            game.current_user = username
            game.menu()
        else:
            print("Invalid username or password.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()