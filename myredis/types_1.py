from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class SimpleString:
    data: str
    def resp_encode(self):
        return f"+{self.data}\r\n".encode()
    def as_str(self):
        return f"{self.data}"


@dataclass
class Error:
    data: str
    def resp_encode(self):
        return f"-{self.data}\r\n".encode()
    def as_str(self):
        return f"{self.data}"


@dataclass
class Integer:
    value: int
    def resp_encode(self):
        return f":{self.value}\r\n".encode()
    def as_str(self):
        return f"{self.value}"


@dataclass
class BulkString:
    data: bytes
    def resp_encode(self):
        if self.data is not None:
            return f"${len(self.data)}\r\n{self.data}\r\n".encode()
        else:
            return f"$-1\r\n".encode()
    def as_str(self):
        return self.data.decode('utf-8') 
    


@dataclass
class Array(Sequence):
    data: list
    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def resp_encode(self):
        result = b''
        if self.data is not None:
            for item in self.data:
                result += item.resp_encode()
            return f"*{len(self.data)}\r\n".encode() + result
        else:
            return f"*-1\r\n".encode()