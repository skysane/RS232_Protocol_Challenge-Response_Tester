# challenge_response_logic.py

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

def calculate_xor_offset_answer(challenge_data):
    """Performs XOR and offset calculation on the challenge data.

    Args:
        challenge_data (bytes): The 8 bytes extracted from the response.

    Returns:
        bytes: The calculated answer, formatted as needed for the protocol.
    """
    if len(challenge_data) != 8:
        raise ValueError(f"Expected 8 bytes of challenge data, but got {len(challenge_data)} bytes.")

    # Placeholder for XOR operation. This is a simplified example.
    # The actual XOR logic needs to be defined by the protocol specification.
    # For now, let's assume a simple XOR with a fixed value or sum.
    xor_result = 0
    for byte in challenge_data:
        xor_result ^= byte

    # Placeholder for offset operation. This is a simplified example.
    # The actual offset value and operation needs to be defined by the protocol.
    # For now, let's add a fixed offset.
    offset = 10
    final_answer_value = (xor_result + offset) & 0xFF # Keep it within a byte range for simplicity

    # The spec requires assembling the answer into a protocol format.
    # This typically involves specific header/footer bytes and the answer value.
    # Example: [START_BYTE] [ANSWER_VALUE] [END_BYTE]
    # For now, let's return the single byte answer for demonstration.
    # A real implementation would format this into a byte string as per protocol.
    return bytes([final_answer_value])

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
