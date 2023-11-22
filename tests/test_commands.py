import pytest

from myredis.protocol import extract_frame_from_stream,encode_message
from myredis.commands import handle_command
from myredis.types_1 import (
    Array,
    BulkString,
    Error,
    Integer,
    SimpleString,
)

@pytest.mark.parametrize(
    "command, expected",
    [
        # Echo Tests
        (
            Array([BulkString(b"ECHO")]),
            Error("ERR wrong number of arguments for 'echo' command"),
        ),
        (Array([BulkString(b"echo"), BulkString(b"Hello")]), BulkString("Hello")),
        (
            Array([BulkString(b"echo"), BulkString(b"Hello"), BulkString("World")]),
            Error("ERR wrong number of arguments for 'echo' command"),
        ),
        # Ping Tests
        (Array([BulkString(b"ping")]), SimpleString("PONG")),
        (Array([BulkString(b"ping"), BulkString(b"Hello")]), BulkString("Hello")),
    ],
)
def test_handle_command(command, expected):
    result = handle_command(command)
    assert result == expected