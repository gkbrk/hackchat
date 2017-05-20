#!/usr/bin/python3
import hackchat

chat = hackchat.HackChat("HelloBot", "programming")

def message_got(chat, message, sender):
    if "hello" in message.lower():
        chat.send_message("Hello there {}!".format(sender))

chat.on_message += [message_got]
chat.start_ping_thread() # Send a ping packet every 60 seconds
chat.run_loop()
