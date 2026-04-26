import unittest
from unittest.mock import MagicMock, patch
import serial
from serial_handler import SerialHandler

class TestSerialHandlerUnlimitedRX(unittest.TestCase):
    def setUp(self):
        self.handler = SerialHandler()
        # Mock serial.Serial
        self.mock_serial = MagicMock()
        self.handler.ser = self.mock_serial
        self.handler.ser.isOpen.return_value = True

    def test_receive_unlimited_data(self):
        # Setup mock for read_all
        expected_data = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A'
        self.mock_serial.read_all.return_value = expected_data
        
        # Test unlimited reception
        received = self.handler.receive_data()
        
        self.assertEqual(received, expected_data)
        self.mock_serial.read_all.assert_called_once()

    def test_timeout_normalization(self):
        # Test connection timeout handling (should pass float directly)
        with patch('serial.Serial', return_value=self.mock_serial) as mock_serial_class:
            self.handler.connect('COM1', 9600, 2.5)
            mock_serial_class.assert_called_with('COM1', 9600, timeout=2.5)

if __name__ == '__main__':
    unittest.main()
