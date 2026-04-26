import datetime
import logging

class DataLogger:
    def __init__(self, log_file="serial_communication.log"):
        self.logger = logging.getLogger("RS232Logger")
        self.logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_tx(self, data):
        self.logger.info(f"TX: {data.hex() if isinstance(data, bytes) else data}")

    def log_rx(self, data):
        self.logger.info(f"RX: {data.hex() if isinstance(data, bytes) else data}")
