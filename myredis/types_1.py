from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class SimpleString:
    data: str
    def resp_encode(self):
        return f"+{self.data}\r\n".encode()


@dataclass
class Error:
    data: str
    def resp_encode(self):
        return f"+{self.data}\r\n".encode()


@dataclass
class Integer:
    value: int
    def resp_encode(self):
        return f"+{self.data}\r\n".encode()


@dataclass
class BulkString:
    data: bytes
    def resp_encode(self):
        return f"+{self.data}\r\n".encode()


@dataclass
class Array:#(Sequence):
    data: list
    def resp_encode(self):
        return f"+{self.data}\r\n".encode()