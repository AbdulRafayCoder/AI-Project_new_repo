import csv
import os
from command import Command
from buttons import Buttons

class Bot:

    def __init__(self):
        self.my_command = Command()
        self.buttn = Buttons()
        self.csv_file = "new_move_log.csv"
        self.write_csv_header()

    def write_csv_header(self):
        """Write the header row to the CSV file if it doesn't exist."""
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    "timer", "has_round_started", "is_round_over",
                    "Player1_ID", "Player1_health", "Player1_x", "Player1_y",
                    "Player1_up", "Player1_down", "Player1_right", "Player1_left",
                    "Player1_Y", "Player1_B", "Player1_X", "Player1_A", "Player1_L", "Player1_R",
                    "Player1_in_move", "Player1_move_id", "Player1_jumping", "Player1_crouching",
                    "Player2_ID", "Player2_health", "Player2_x", "Player2_y",
                    "Player2_up", "Player2_down", "Player2_right", "Player2_left",
                    "Player2_Y", "Player2_B", "Player2_X", "Player2_A", "Player2_L", "Player2_R",
                    "Player2_in_move", "Player2_move_id", "Player2_jumping", "Player2_crouching"
                ])

    def log_game_state(self, game_state):
        """Log the current game state to the CSV file."""
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                game_state.timer,
                game_state.has_round_started,
                game_state.is_round_over,
                game_state.player1.player_id,
                game_state.player1.health,
                game_state.player1.x_coord,
                game_state.player1.y_coord,
                game_state.player1.player_buttons.up,
                game_state.player1.player_buttons.down,
                game_state.player1.player_buttons.right,
                game_state.player1.player_buttons.left,
                game_state.player1.player_buttons.Y,
                game_state.player1.player_buttons.B,
                game_state.player1.player_buttons.X,
                game_state.player1.player_buttons.A,
                game_state.player1.player_buttons.L,
                game_state.player1.player_buttons.R,
                game_state.player1.is_player_in_move,
                game_state.player1.move_id,
                game_state.player1.is_jumping,
                game_state.player1.is_crouching,
                game_state.player2.player_id,
                game_state.player2.health,
                game_state.player2.x_coord,
                game_state.player2.y_coord,
                game_state.player2.player_buttons.up,
                game_state.player2.player_buttons.down,
                game_state.player2.player_buttons.right,
                game_state.player2.player_buttons.left,
                game_state.player2.player_buttons.Y,
                game_state.player2.player_buttons.B,
                game_state.player2.player_buttons.X,
                game_state.player2.player_buttons.A,
                game_state.player2.player_buttons.L,
                game_state.player2.player_buttons.R,
                game_state.player2.is_player_in_move,
                game_state.player2.move_id,
                game_state.player2.is_jumping,
                game_state.player2.is_crouching
            ])

    def fight(self, current_game_state, player):
        """Main fight logic."""
        # Log the current game state to the CSV file
        self.log_game_state(current_game_state)

        # Assign the updated buttons to the command
        if player == "1":
            self.my_command.player_buttons = self.buttn
        elif player == "2":
            self.my_command.player2_buttons = self.buttn

        return self.my_command