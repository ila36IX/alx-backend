#!/usr/bin/python3
"""
Validate whether a given dataset represents a valid UTF-8 encoding
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list[int]): A list of integers representing bytes
    
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    # Counter for the number of continuation bytes expected
    cont_bytes = 0
    
    for num in data:
        # Ensure we're only looking at the 8 least significant bits
        byte = num & 0xFF
        
        if cont_bytes:
            # Check if this byte is a continuation byte
            if byte >> 6 != 0b10:
                return False
            cont_bytes -= 1
        else:
            # Determine the number of continuation bytes
            if byte >> 7 == 0:
                cont_bytes = 0
            elif byte >> 5 == 0b110:
                cont_bytes = 1
            elif byte >> 4 == 0b1110:
                cont_bytes = 2
            elif byte >> 3 == 0b11110:
                cont_bytes = 3
            else:
                return False
    
    # All continuation bytes should be accounted for
    return cont_bytes == 0 
