# challenge_response_logic.py

def calculate_checksum(data):
    """Calculates the checksum (sum of bytes), masks to 8 bits, 
    and returns the 2-byte ASCII representation of the high and low nibbles.

    Args:
        data (bytes): The data to calculate checksum for.

    Returns:
        bytes: 2 bytes (high nibble ASCII, low nibble ASCII).
    """
    checksum = sum(data) & 0xFF
    high_nibble = (checksum >> 4) & 0x0F
    low_nibble = checksum & 0x0F
    
    def nibble_to_ascii(nibble):
        if 0 <= nibble <= 9:
            return nibble + 0x30
        else:
            return nibble - 10 + 0x41 # 'A' is 0x41

    return bytes([nibble_to_ascii(high_nibble), nibble_to_ascii(low_nibble)])

def decode_challenge_data(response_bytes):
    """Extracts bytes 5-12 from a 16-byte response.

    Args:
        response_bytes (bytes): The 16-byte response data.

    Returns:
        bytes: The extracted 8 bytes (bytes 5-12).
    """
    if len(response_bytes) != 16:
        raise ValueError(f"Expected 16 bytes response, but got {len(response_bytes)} bytes.")
    # According to the spec, bytes 5-12 are extracted. Python slicing is 0-indexed.
    # So, we need bytes from index 4 up to (but not including) index 12.
    return response_bytes[4:12]

def calculate_xor_offset_answer(challenge_data, xor_indices, offsets):
    """Performs XOR and offset calculation on the challenge data based on user configuration.

    Args:
        challenge_data (bytes): The 8 bytes extracted from the response.
        xor_indices (list of tuple): List of 4 tuples, each containing two byte indices to XOR.
        offsets (list of int): List of 4 integer offsets.

    Returns:
        bytes: The calculated answer of 4 bytes.
    """
    if len(challenge_data) != 8:
        raise ValueError(f"Expected 8 bytes of challenge data, but got {len(challenge_data)} bytes.")

    answers = []
    for i in range(4):
        idx1, idx2 = xor_indices[i]
        offset = offsets[i]
        result = (challenge_data[idx1] ^ challenge_data[idx2] + offset) & 0xFF
        answers.append(result)

    return bytes(answers)

def assemble_response_protocol(answer_bytes):
    """Assembles the final answer into the protocol format for transmission.

    Args:
        answer_bytes (bytes): The calculated answer bytes.

    Returns:
        bytes: The complete protocol message to be sent back.
    """
    # This is a placeholder. The actual protocol framing needs to be defined.
    # Example: assuming a simple start byte, answer, and end byte.
    start_byte = b'\x02' # STX
    end_byte = b'\x03'   # ETX
    return start_byte + answer_bytes + end_byte
