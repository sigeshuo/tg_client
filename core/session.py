from enum import Enum


class Session:
    def __init__(self, name, phone_number, session_string=None):
        self.name = name
        self.phone_number = phone_number
        self.session_string = session_string


class SessionType(Enum):
    STRING = "string"
    FILE = "file"
