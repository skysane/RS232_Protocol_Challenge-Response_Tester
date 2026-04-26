## 1. UI Enhancements

- [x] 1.1 Add "Clear Log" button in the Data Log frame
- [x] 1.2 Implement clear log logic in `main_gui.py`

## 2. Communication Protocol Refinement

- [x] 2.1 Update `SerialHandler.connect` to perform a buffer reset on connection
- [x] 2.2 Refactor protocol state management in `main_gui.py` to ensure correct flow after timeouts and resets
- [x] 2.3 Verify and test the new sequential communication flow
