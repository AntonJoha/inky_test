import os
import queue
from flask import Flask
from flask import request
import threading
import time

import try_inky

app = Flask(__name__)
order = queue.Queue()


def handle_queue():
    while True:
        item = order.get(block=True, timeout=None)
        try_inky.set_screen(item)
        time.sleep(60)

def add_image(data):
    order.put(data, block=True, timeout=None)

@app.get("/")
def handle_info():
    """
    This is what's seen if someone just opens the port in the web browser 
    """
    return "Hej på dig"


@app.post("/")
def handle_start():
    """
    This function is called everytime your snake is entered into a game.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()
    add_image(data)
    

    return "ok"



if __name__ == "__main__":

    print("Starting Battlesnake Server...")
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=True)
