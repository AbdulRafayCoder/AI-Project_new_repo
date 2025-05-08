import socket
import json
import sys
from pynput import keyboard
from game_state import GameState
from bot import Bot

# Global variable to store the current key states
key_states = {
    "up": False,
    "down": False,
    "left": False,
    "right": False,
    "Y": False,  # Light Punch (S)
    "B": False,  # Light Kick (X)
    "X": False,  # Medium Punch (A)
    "A": False,  # Medium Kick (Z)
    "L": False,  # Hard Punch (W)
    "R": False   # Hard Kick (E)
}

def on_press(key):
    """Handle key press events."""
    try:
        if key.char == 'w':
            key_states["L"] = True  # Hard Punch
        elif key.char == 'e':
            key_states["R"] = True  # Hard Kick
        elif key.char == 'a':
            key_states["X"] = True  # Medium Punch
        elif key.char == 'z':
            key_states["A"] = True  # Medium Kick
        elif key.char == 's':
            key_states["Y"] = True  # Light Punch
        elif key.char == 'x':
            key_states["B"] = True  # Light Kick
    except AttributeError:
        if key == keyboard.Key.up:
            key_states["up"] = True  # Move Up (Jump)
        elif key == keyboard.Key.down:
            key_states["down"] = True  # Move Down (Crouch)
        elif key == keyboard.Key.left:
            key_states["left"] = True  # Move Left
        elif key == keyboard.Key.right:
            key_states["right"] = True  # Move Right

def on_release(key):
    """Handle key release events."""
    try:
        if key.char == 'w':
            key_states["L"] = False  # Hard Punch
        elif key.char == 'e':
            key_states["R"] = False  # Hard Kick
        elif key.char == 'a':
            key_states["X"] = False  # Medium Punch
        elif key.char == 'z':
            key_states["A"] = False  # Medium Kick
        elif key.char == 's':
            key_states["Y"] = False  # Light Punch
        elif key.char == 'x':
            key_states["B"] = False  # Light Kick
    except AttributeError:
        if key == keyboard.Key.up:
            key_states["up"] = False  # Move Up (Jump)
        elif key == keyboard.Key.down:
            key_states["down"] = False  # Move Down (Crouch)
        elif key == keyboard.Key.left:
            key_states["left"] = False  # Move Left
        elif key == keyboard.Key.right:
            key_states["right"] = False  # Move Right

def connect(port):
    """For making a connection with the game."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", port))
    server_socket.listen(5)
    (client_socket, _) = server_socket.accept()
    print("Connected to game!")
    return client_socket

def send(client_socket, command):
    """Send updated command to Bizhawk so the game reacts accordingly."""
    command_dict = command.object_to_dict()
    pay_load = json.dumps(command_dict).encode()
    client_socket.sendall(pay_load)

def receive(client_socket):
    """Receive the game state and return it."""
    pay_load = client_socket.recv(4096)
    input_dict = json.loads(pay_load.decode())
    game_state = GameState(input_dict)
    return game_state

def map_keys_to_buttons(bot_command):
    """Map the current key states to the bot's button commands."""
    bot_command.player_buttons.up = key_states["up"]
    bot_command.player_buttons.down = key_states["down"]
    bot_command.player_buttons.left = key_states["left"]
    bot_command.player_buttons.right = key_states["right"]
    bot_command.player_buttons.Y = key_states["Y"]  # Light Punch
    bot_command.player_buttons.B = key_states["B"]  # Light Kick
    bot_command.player_buttons.X = key_states["X"]  # Medium Punch
    bot_command.player_buttons.A = key_states["A"]  # Medium Kick
    bot_command.player_buttons.L = key_states["L"]  # Hard Punch
    bot_command.player_buttons.R = key_states["R"]  # Hard Kick

def main():
    if sys.argv[1] == '1':
        client_socket = connect(9999)
    elif sys.argv[1] == '2':
        client_socket = connect(10000)

    current_game_state = None
    bot = Bot()

    # Start listening to keyboard events
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while (current_game_state is None) or (not current_game_state.is_round_over):
        current_game_state = receive(client_socket)
        bot_command = bot.fight(current_game_state, sys.argv[1])

        # Map keyboard inputs to bot commands
        map_keys_to_buttons(bot_command)

        send(client_socket, bot_command)

    listener.stop()

if __name__ == '__main__':
    main()