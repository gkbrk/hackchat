# hackchat

`hackchat` is a Python library for writing [hack.chat](https://hack.chat) bots and clients. It is event-driven, simple to use, and is
contained in a single file.

# Installation

- Install the library: `pip3 install hackchat`

# Usage

```python3
#!/usr/bin/env python3
import hackchat

def message_got(chat, message, sender):
    if "hello" in message.lower():
        chat.send_message("Hello there {}!".format(sender))

chat = hackchat.HackChat("HelloBot", "programming")
chat.on_message += [message_got]
chat.run()
```

# License

This project is under the [MIT License](LICENSE).
