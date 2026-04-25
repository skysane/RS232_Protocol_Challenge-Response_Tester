# test_rs232_tester.py

import unittest
from unittest.mock import MagicMock, patch
import serial
import serial.tools.list_ports

# Import the modules to be tested
import serial_handler
import challenge_response_logic

# --- Test Cases for serial_handler.py ---
class TestSerialHandler(unittest.TestCase):

    def setUp(self):
        self.handler = serial_handler.SerialHandler()

    @patch('serial.Serial')
    def test_connect_success(self, MockSerial):
        # Configure the mock serial port to appear open
        mock_instance = MockSerial.return_value
        mock_instance.isOpen.return_value = True

        port = "COM1"
        baudrate = 9600
        result = self.handler.connect(port, baudrate)

        self.assertTrue(result)
        MockSerial.assert_called_with(port, baudrate, timeout=1)
        self.assertTrue(self.handler.is_connected())
        self.assertEqual(self.handler.port, port)
        self.assertEqual(self.handler.baudrate, baudrate)

    @patch('serial.Serial')
    def test_connect_failure(self, MockSerial):
        # Configure the mock serial port to raise an exception
        MockSerial.side_effect = serial.SerialException("Permission denied")

        port = "COM1"
        baudrate = 9600
        with self.assertRaises(serial.SerialException):
            self.handler.connect(port, baudrate)

        MockSerial.assert_called_with(port, baudrate, timeout=1)
        self.assertFalse(self.handler.is_connected())

    def test_disconnect(self):
        # Simulate an already connected state
        mock_ser = MagicMock(spec=serial.Serial)
        mock_ser.isOpen.return_value = True
        self.handler.ser = mock_ser
        self.handler.port = "COM1"
        self.handler.baudrate = 9600

        self.handler.disconnect()
        mock_ser.close.assert_called_once()
        self.assertIsNone(self.handler.ser)
        self.assertIsNone(self.handler.port)
        self.assertIsNone(self.handler.baudrate)

    @patch('serial.Serial')
    def test_send_data_success(self, MockSerial):
        mock_instance = MockSerial.return_value
        mock_instance.isOpen.return_value = True
        self.handler.ser = mock_instance
        self.handler.port = "COM1"
        self.handler.baudrate = 9600

        data_to_send = b'\x01\x02\x03\x04\x05'
        result = self.handler.send_data(data_to_send)

        self.assertTrue(result)
        mock_instance.write.assert_called_once_with(data_to_send)

    @patch('serial.Serial')
    def test_send_data_not_connected(self, MockSerial):
        data_to_send = b'\x01\x02\x03\x04\x05'
        result = self.handler.send_data(data_to_send)

        self.assertFalse(result)
        # MockSerial.return_value.write.assert_not_called() # No need to assert this as the method checks is_connected() first

    @patch('serial.Serial')
    def test_receive_data_success(self, MockSerial):
        mock_instance = MockSerial.return_value
        mock_instance.isOpen.return_value = True
        mock_instance.read.return_value = b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
        self.handler.ser = mock_instance
        self.handler.port = "COM1"
        self.handler.baudrate = 9600

        expected_length = 16
        received_data = self.handler.receive_data(expected_length)

        self.assertEqual(received_data, b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f')
        mock_instance.read.assert_called_once_with(expected_length)

    @patch('serial.Serial')
    def test_receive_data_timeout(self, MockSerial):
        mock_instance = MockSerial.return_value
        mock_instance.isOpen.return_value = True
        mock_instance.read.return_value = b'' # Simulate timeout
        self.handler.ser = mock_instance
        self.handler.port = "COM1"
        self.handler.baudrate = 9600

        expected_length = 16
        received_data = self.handler.receive_data(expected_length)

        self.assertIsNone(received_data)
        mock_instance.read.assert_called_once_with(expected_length)

    @patch('serial.tools.list_ports.comports')
    def test_list_available_ports(self, mock_comports):
        # Mocking the return value of comports()
        mock_port1 = MagicMock()
        mock_port1.device = "COM1"
        mock_port2 = MagicMock()
        mock_port2.device = "/dev/ttyUSB0"
        mock_comports.return_value = [mock_port1, mock_port2]

        ports = self.handler.list_available_ports()
        self.assertEqual(ports, ["COM1", "/dev/ttyUSB0"])

# --- Test Cases for challenge_response_logic.py ---
class TestChallengeResponseLogic(unittest.TestCase):

    def test_decode_challenge_data_valid(self):
        full_response = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f' # Bytes 5-12 are 0x04 to 0x0b
        expected_challenge = b'\x04\x05\x06\x07\x08\x09\x0a\x0b'
        result = challenge_response_logic.decode_challenge_data(full_response)
        self.assertEqual(result, expected_challenge)

    def test_decode_challenge_data_invalid_length(self):
        short_response = b'\x00\x01\x02\x03\x04\x05\x06\x07'
        with self.assertRaises(ValueError):
            challenge_response_logic.decode_challenge_data(short_response)

    def test_calculate_xor_offset_answer_valid(self):
        challenge_data = b'\x01\x02\x03\x04\x05\x06\x07\x08'
        # XOR of 0x01 ^ 0x02 ^ ... ^ 0x08 = 0x08
        # 0x08 + 0x0a (offset) = 0x12
        expected_answer = b'\x12' # Corrected from b'\x13'
        result = challenge_response_logic.calculate_xor_offset_answer(challenge_data)
        self.assertEqual(result, expected_answer)

    def test_calculate_xor_offset_answer_invalid_length(self):
        short_challenge = b'\x01\x02\x03'
        with self.assertRaises(ValueError):
            challenge_response_logic.calculate_xor_offset_answer(short_challenge)

    def test_assemble_response_protocol(self):
        answer_bytes = b'\x13'
        expected_protocol = b'\x02\x13\x03' # STX + Answer + ETX
        result = challenge_response_logic.assemble_response_protocol(answer_bytes)
        self.assertEqual(result, expected_protocol)

if __name__ == '__main__':
    unittest.main()
