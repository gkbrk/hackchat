from setuptools import setup

setup(
    name = "hackchat",
    py_modules = ["hackchat"],
    version = "1.0.0",
    description = "An event-driven hack.chat client library.",
    author = "Gokberk Yaltirakli",
    author_email = "webdosusb@gmail.com",
    url = "https://github.com/gkbrk/hackchat",
    keywords = ["hack.chat", "event", "client", "chat"],
    install_requires = ["websocket-client"]
)
