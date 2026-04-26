## 1. Core Logic Updates

- [x] 1.1 Modify `serial_handler.py` to add `reset_output_buffer()` before `write()` operations
- [x] 1.2 Implement a centralized logging class/utility for TX and RX data
- [x] 1.3 Integrate the logging utility into `serial_handler.py` to capture TX/RX events

## 2. GUI and System Integration

- [x] 2.1 Update `main_gui.py` to connect the new logging utility to the UI
- [x] 2.2 Verify TX buffer clearing behavior in the main application flow
- [x] 2.3 Verify data logging captured all communications correctly
