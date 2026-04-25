# serial_handler.py

import serial
import serial.tools.list_ports

class SerialHandler:
    def __init__(self):
        self.ser = None
        self.port = None
        self.baudrate = None

    def list_available_ports(self):
        """Lists available serial ports."""
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect(self, port, baudrate=9600, timeout=1):
        """Connects to the specified serial port."""
        try:
            self.port = port
            self.baudrate = baudrate
            self.ser = serial.Serial(self.port, self.baudrate, timeout=timeout/1000.0)
            if self.ser.isOpen():
                return True
            else:
                return False
        except serial.SerialException as e:
            raise e
        except Exception as e:
            raise e

    def disconnect(self):
        """Disconnects from the serial port."""
        if self.ser and self.ser.isOpen():
            self.ser.close()
        self.ser = None
        self.port = None
        self.baudrate = None

    def is_connected(self):
        """Checks if currently connected to a serial port."""
        return self.ser is not None and self.ser.isOpen()

    def send_data(self, data):
        """Sends data to the serial port. Data should be bytes."""
        if not self.is_connected():
            return False
        try:
            self.ser.reset_output_buffer()
            self.ser.write(data)
            return True
        except serial.SerialTimeoutException:
            return False
        except Exception as e:
            raise e

    def receive_data(self, length):
        """Receives a specified number of bytes from the serial port."""
        if not self.is_connected():
            return None
        try:
            data = self.ser.read(length)
            if data: # If any data received
                return data
            else: # Timeout or no data received
                return None
        except serial.SerialTimeoutException:
            return None
        except Exception as e:
            raise e
