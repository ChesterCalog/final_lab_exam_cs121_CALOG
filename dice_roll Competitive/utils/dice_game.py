import os
import random
from utils.score import Score  
from utils.user_manager import UserManager

class DiceGame:
    def __init__(self):
        self.user_manager = UserManager()
        self.scores = []
        self.current_user = None
        self.load_scores()

    def load_scores(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/rankings.txt'):
            with open('data/rankings.txt', 'w') as file:
                pass
        else:
            with open('data/rankings.txt', 'r') as file:
                for line in file:
                    username, game_id, points, wins = line.strip().split(',')
                    score = Score(username, game_id, int(points), int(wins))
                    self.scores.append(score)

    def save_score(self, score):
        with open('data/rankings.txt', 'a') as file:
            file.write(f"{score.username},{score.game_id},{score.points},{score.wins}\n")

    def play_game(self):
        print("Let's play the dice game against the CPU!")
        total_points = 0
        total_stages_won = 0

        while True:
            stage_points = 0
            for stage in range(3): 
                print(f"\nStage {stage + 1}:")
                player_score = self.roll_dice()
                cpu_score = self.roll_dice()

                print(f"You rolled: {player_score}")
                print(f"CPU rolled: {cpu_score}")

                if player_score > cpu_score:
                    print("You win this round!")
                    stage_points += 1
                elif player_score < cpu_score:
                    print("CPU wins this round!")
                    stage_points -= 1
                else:
                    print("It's a tie! Roll again...")

            if stage_points > 0:
                total_stages_won += 1
                total_points += 3
                print("You win this stage!")
                choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                if choice != '1':
                    break
            else:
                print("Game over! Try again next time.")
                break

        print(f"Total points earned: {total_points}")
        print(f"Number of stages won: {total_stages_won}")

        if self.current_user:
            self.update_scores(total_stages_won)
            self.menu()

    def roll_dice(self):
        return random.randint(1, 6)

    def update_scores(self, player_wins):
        user_score = None
        for score in self.scores:
            if score.username == self.current_user and score.game_id == "dice_game":
                user_score = score
                break
            
        if user_score is None:
            user_score = Score(self.current_user, "dice_game", 0, 0)
            self.scores.append(user_score)

        if player_wins > 0:  
            user_score.points += player_wins * 3 
            user_score.wins += player_wins  

        self.save_score(user_score)

    def show_top_scores(self):
        if not self.scores:
            print("=======================================================================")
            print("No scores available.")
            self.menu()
            return

        print("=======================================================================")
        print("Top 10 Scores:")
        sorted_scores = sorted(self.scores, key=lambda x: x.points, reverse=True)[:10]
        for i, score in enumerate(sorted_scores, 1):
            print(f"{i}. Username: {score.username}, Points: {score.points}, Wins: {score.wins}")
            
        self.menu()

    def logout(self):
        self.current_user = None

    def menu(self):
        if self.current_user:
            print("=======================================================================")
            print(f"Hello, {self.current_user}!")
            print("Welcome to Dice Roll Game!")
            print("1. Start Game")
            print("2. Show Top Scores")
            print("3. Log out")

        choice = input("Enter your choice: ")
        if choice == '1':
            self.play_game()
        elif choice == '2':
            self.show_top_scores()
        elif choice == '3':
            self.logout()
        else:
            print("Invalid choice. Please try again.")