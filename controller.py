import socket
import json
import sys
from game_state import GameState
from bot import Bot

def connect(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", port))
    server_socket.listen(5)
    (client_socket, _) = server_socket.accept()
    print("Connected to game!")
    return client_socket

def send(client_socket, command):
    command_dict = command.object_to_dict()
    payload = json.dumps(command_dict).encode()
    client_socket.sendall(payload)

def receive(client_socket):
    payload = client_socket.recv(4096)
    input_dict = json.loads(payload.decode())
    return GameState(input_dict)

def main():
    if sys.argv[1] == '1':
        client_socket = connect(9999)
    elif sys.argv[1] == '2':
        client_socket = connect(10000)

    bot = Bot()
    current_game_state = None
    print("Model-based bot is now controlling the game!")

    while (current_game_state is None) or (not current_game_state.is_round_over):
        current_game_state = receive(client_socket)
        bot_command = bot.fight(current_game_state, sys.argv[1])
        send(client_socket, bot_command)

if __name__ == '__main__':
    main()
