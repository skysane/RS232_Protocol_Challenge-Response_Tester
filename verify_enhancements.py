import unittest
from unittest.mock import MagicMock
from challenge_response_logic import calculate_checksum
from serial_handler import SerialHandler

class TestEnhancedRS232(unittest.TestCase):
    def test_checksum_algorithm(self):
        # sum = 0x01+0x02+0x03+0x04+0x05 = 0x0F
        # Expected: high 0x0, low 0xF -> '0' (0x30), 'F' (0x46)
        payload = b'\x01\x02\x03\x04\x05'
        expected = b'\x30\x46'
        self.assertEqual(calculate_checksum(payload), expected)

    def test_unlimited_tx(self):
        handler = SerialHandler()
        mock_serial = MagicMock()
        handler.ser = mock_serial
        handler.ser.isOpen.return_value = True
        
        long_payload = b'\x01' * 100 # 100 bytes
        handler.send_data(long_payload)
        mock_serial.write.assert_called_with(long_payload)

if __name__ == '__main__':
    unittest.main()
