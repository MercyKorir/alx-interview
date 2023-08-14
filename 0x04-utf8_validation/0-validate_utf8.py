#!/usr/bin/python3
"""Definition of a method"""


def validUTF8(data):
    """
    Determines if data rep valid utf8 encoding
    """

    bytes_no = 0
    for byte in data:
        if bytes_no == 0:
            if (byte >> 5) == 0b110:
                bytes_no = 1
            elif (byte >> 4) == 0b1110:
                bytes_no = 2
            elif (byte >> 3) == 0b11110:
                bytes_no = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_no -= 1
    return bytes_no == 0
