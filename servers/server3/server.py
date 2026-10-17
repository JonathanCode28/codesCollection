import socket
import pickle
import _thread
import pygame
pygame.init()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind(("172.104.202.26", 2433))
server.bind(("localhost", 2433))

server.listen()
players = {
    "player1x": 200,
    "player1y": 250,
    "player1score": 0,

    "player2x": 700,
    "player2y": 250,
    "player2score": 0,

    "winner": 0
}
next_id = 1

font = pygame.font.SysFont("impact", 50)

def reset_pos():
    players["player1x"] = 200
    players["player1y"] = 250
    players["player2x"] = 700
    players["player2y"] = 250
def handle_client(client, player_id):
    global players
    try:
        init_data = {
            "player_id": player_id,
            "players": players
        }
        client.send(pickle.dumps(init_data))
        while True:
            data_recv = pickle.loads(client.recv(1024))
            if players["winner"] == 0:
                players[f"player{player_id}x"] = data_recv[f"player{player_id}x"]
                players[f"player{player_id}y"] = data_recv[f"player{player_id}y"]

                player1 = pygame.Rect(players["player1x"] - 25, players["player1y"] - 25, 25*2, 25*2)
                player2 = pygame.Rect(players["player2x"] - 25, players["player2y"] - 25, 25 * 2, 25*2)

                if player1.colliderect(player2):
                    if players["player1x"] < 900//2:
                        players["player1x"] = 200
                        players["player1y"] = 250
                    if players["player1x"] > 900//2:
                        players["player2x"] = 700
                        players["player2y"] = 250
                if players["player1x"] >= 890:
                    players["player1score"] += 1
                    reset_pos()
                if players["player2x"] <= 0:
                    players["player2score"] += 1
                    reset_pos()

                if players["player2score"] >= 5:
                    players["winner"] = 2
                if players["player1score"] >= 5:
                    players["winner"] = 1
                #winner_text = font.render("Player " + str(players["winner"]) + "wins!", True, "gold")
            client.send(pickle.dumps(players))
    except:
        pass

try:

    while True:
        #handle_client()
        client, addr = server.accept()
        player_id = next_id
        next_id += 1
        _thread.start_new_thread(handle_client, (client, player_id))

finally:
    client.close()
    server.close()