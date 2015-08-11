import hackchat

chat = hackchat.HackChat("HelloBot", "programming")

def message_got(chat, message, sender):
    if "hello" in message.lower():
        chat.send_message("Hello there {}!".format(sender))

chat.on_message.append(message_got)
chat.run_loop()
