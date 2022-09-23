import hashlib
import struct


def hash(x: bytes) -> int:
    return struct.unpack("<I", hashlib.sha1(x).digest()[:4])[0]
