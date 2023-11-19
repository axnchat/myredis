from dataclasses import dataclass

MSG_SEPERATOR = b"\r\n"

@dataclass
class SimpleString:
    data:str

def extract_frame_from_stream(buffer):
    match chr(buffer[0]):
        case '+':
            seperator = buffer.find(MSG_SEPERATOR)
            if seperator != -1:
                return SimpleString(buffer[1:seperator].decode()),seperator+2
    return None,0

""" def test_read_string():
    buff = b"+OK\r\n"
    frame,frameSize = extract_frame_from_stream(buff)
    assert frame == SimpleString("OK")
    assert frameSize == 0

test_read_string() """