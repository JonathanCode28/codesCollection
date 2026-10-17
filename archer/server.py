import socket, pickle, _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ADDR = "localhost"
ADDR = "194.36.89.237"

server.bind((ADDR, 2433))
server.listen()

print("Server started...")

data = {
    "player1": {
        "gravity": 1,
        "velocity_y": 0,
        "jump_power": -15,
        "direction": "right",
        "on_ground": False,
        "x": 0,
        "y": 300,
        "speed": 5,
        "arrows": [],
        "hp": 100,
        "winner": 0,
    },
    "player2": {
        "gravity": 1,
        "velocity_y": 0,
        "jump_power": -15,
        "direction": "right",
        "on_ground": False,
        "x": 400,
        "y": 300,
        "speed": 5,
        "arrows": [],
        "hp": 100,
        "winner": 0,
    },
}

next_id = 1


def handle_client(client, player_id):
    global data

    my_key = f"player{player_id}"

    init_data = {
        "data": data,
        "player_id": player_id,
    }

    client.send(pickle.dumps(init_data))

    while True:
        try:
            data_recv = pickle.loads(client.recv(4096))

        # שומרים את החיים והניצחון שהשרת מכיר
        # כדי שהקליינט לא ידרוס אותם בטעות
            old_hp = data[my_key]["hp"]
            old_winner = data[my_key]["winner"]

        # קודם כל מעדכנים את השחקן לפי מה שהקליינט שלח
            data[my_key] = data_recv

            # מחזירים את hp ו winner לשליטה של השרת
            data[my_key]["hp"] = old_hp
            data[my_key]["winner"] = old_winner

        # בודקים את החצים של השחקן הזה
            for arrow in data[my_key]["arrows"][:]:
                if arrow["hit"] is not None:
                    target = arrow["hit"]

                if target in data:
                    data[target]["hp"] -= 10

                if data[target]["hp"] < 0:
                    data[target]["hp"] = 0

                if data[target]["hp"] <= 0:
                    data[my_key]["winner"] = 1

            # אחרי שחץ פגע מוחקים אותו
            # אחרת הוא יכול להוריד חיים כמה פעמים
            data[my_key]["arrows"].remove(arrow)

            client.send(pickle.dumps(data))

        except Exception as e:
            print("Client error:", e)
            break

            client.close()


    try:
        while True:
            client, addr = server.accept()
            print("Connected to:", addr)

            if next_id > 2:
                client.close()
                continue

        player_id = next_id
        next_id += 1

        _thread.start_new_thread(handle_client, (client, player_id))

    finally:
        server.close()