import json
import time
import websocket
import threading

class HackChat:
    def __init__(self, nick, channel="programming"):
        self.nick = nick
        self.channel = channel

        self.online_users = []

        self.on_message = []
        self.on_join = []
        self.on_leave = []

        self.ws = websocket.create_connection("wss://hack.chat/chat-ws")
        self.ws.send(json.dumps({"cmd": "join", "channel": channel, "nick": nick}))

    def run(self):
        result = json.loads(self.ws.recv())
        if result["cmd"] == "chat" and not result["nick"] == self.nick:
            for handler in list(self.on_message):
                handler(self, result["text"], result["nick"])
        elif result["cmd"] == "onlineAdd":
            self.online_users.append(result["nick"])
            for handler in list(self.on_join):
                handler(self, result["nick"])
        elif result["cmd"] == "onlineRemove":
            self.online_users.remove(result["nick"])
            for handler in list(self.on_leave):
                handler(self, result["nick"])
        elif result["cmd"] == "onlineSet":
            for nick in result["nicks"]:
                self.online_users.append(nick)
        return result

    def run_loop(self):
        while True:
            self.run()

    def send_message(self, msg):
        self.ws.send(json.dumps({"cmd": "chat", "text": msg}))

    def _ping_thread(self):
        while self.ws.connected:
            self.ws.send(json.dumps({"cmd": "ping"}))
            time.sleep(60)

    def start_ping_thread(self):
        threading.Thread(target=self._ping_thread).start()
