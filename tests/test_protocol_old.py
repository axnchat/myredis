import sys

import pytest
sys.path.append("myredis")  # Add the 'folder' directory to the Python path

from protocol import extract_frame_from_stream, SimpleString

@pytest.mark.parametrize("buff, expected_result", [
    (b"+OK\r\n",(SimpleString("OK"),5)),        # Test case 1
    (b"+Partial_string",(None,0)),        # Test case 2
    (b"+string\r\nExtraData",(SimpleString("string"),9)),       # Test case 3
])
def test_read(buff, expected_result):
    result = extract_frame_from_stream(buff)
    assert result == expected_result

def test_read_string():
    buff = b"+OK\r\n"
    frame,frameSize = extract_frame_from_stream(buff)
    assert frame == SimpleString("OK")
    assert frameSize == 5


def test_read_partial_string():
    buff = b"+Partial_string"
    frame,frameSize = extract_frame_from_stream(buff)
    assert frame == None
    assert frameSize == 0

def test_read_string_extraData():
    buff = b"+string\r\nExtraData"
    frame,frameSize = extract_frame_from_stream(buff)
    assert frame == SimpleString("string")
    assert frameSize == 9



""" def test_read_error():
    buff = b"-Error\r\n"
    frame,frameSize = extract_frame_from_stream(buff)
    assert frame == SimpleError("Error")
    assert frameSize == 0

def test_read_int():
    buff = b":10\r\n"
    frame,frameSize = extract_frame_from_stream(buff)
    assert frame == SimpleInt("10")
    assert frameSize == 0 """



