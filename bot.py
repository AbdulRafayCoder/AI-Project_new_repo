import joblib
import numpy as np
from command import Command
from buttons import Buttons

class Bot:

    def __init__(self):
        self.my_command = Command()
        self.buttn = Buttons()
        self.model = joblib.load("street_fighter_model.pkl")

    def fight(self, game_state, player):
        # Strict feature extraction
        features = [
            game_state.player1.player_id,
            game_state.player2.player_id,
            game_state.player1.health - game_state.player2.health,  # health_difference
            int(game_state.player2.player_buttons.up),
            int(game_state.player2.player_buttons.down),
            int(game_state.player2.player_buttons.right),
            int(game_state.player2.player_buttons.left),
            int(game_state.player2.player_buttons.Y),
            int(game_state.player2.player_buttons.B),
            int(game_state.player2.player_buttons.X),
            int(game_state.player2.player_buttons.A),
            int(game_state.player2.player_buttons.L),
            int(game_state.player2.player_buttons.R),
            game_state.player2.x_coord - game_state.player1.x_coord,  # x_distance
            game_state.player2.y_coord - game_state.player1.y_coord   # y_distance
        ]

        # Predict output using model
        prediction = self.model.predict([features])[0]

        # Button mapping
        buttons = self.buttn
        button_names = ["up", "down", "right", "left", "Y", "B", "X", "A", "L", "R"]

        for i, name in enumerate(button_names):
            setattr(buttons, name, bool(prediction[i]))

        # Assign buttons to correct player
        if player == "1":
            self.my_command.player_buttons = buttons
        elif player == "2":
            self.my_command.player2_buttons = buttons

        return self.my_command
