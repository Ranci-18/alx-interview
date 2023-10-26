#!/usr/bin/python3
"""Module that determines if a given data set represents a valid"""
import codecs


def validUTF8(data):
    """Determines if a given data set represents a valid
    UTF-8 encoding"""
    for unit_data in data:
        byte_data = bytes([unit_data])
        try:
            codecs.decode(byte_data, 'utf-8', errors='strict')
        except UnicodeDecodeError:
            return False

    return True
