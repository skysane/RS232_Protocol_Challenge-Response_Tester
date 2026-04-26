## 1. Core Logic & Serial Handling Updates

- [x] 1.1 Update `serial_handler.py` to support dynamic-length data reception
- [ ] 1.2 Update `challenge_response_logic.py` to implement 4-block verification engine with XOR/Addition logic
- [ ] 1.3 Implement Checksum (CS) calculation for transmission in `challenge_response_logic.py`

## 2. GUI Updates

- [ ] 2.1 Update `main_gui.py` to standardize timeout units to seconds
- [ ] 2.2 Add UI components for 4-block verification inputs and results display
- [ ] 2.3 Add "CS" toggle and "Transmit" button to the UI
- [ ] 2.4 Connect GUI events to the updated core logic

## 3. Validation

- [ ] 3.1 Verify timeout configuration units
- [ ] 3.2 Verify verification calculation results
- [ ] 3.3 Verify CS calculation and transmission functionality
- [ ] 3.4 Ensure unlimited data reception works as expected
