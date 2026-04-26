## Why

To enhance the testing workflow and improve user control over data management, the tester needs manual clearing of logs and more explicit state control over the serial communication protocol.

## What Changes

- **Log Clearing**: Add a button to the Data Log panel to clear logged traffic history.
- **Protocol Flow Redefinition**:
  - Automatically clear buffers on connection.
  - Manual initiation of command sending.
  - Timeout handling returns the system to a clean idle state for re-sending.
  - Manual initiation of verified response transmission.

## Capabilities

### New Capabilities
- `log-clear-control`: Ability for the user to flush logged communication data.
- `explicit-protocol-state-machine`: Strict control of the communication flow states (Idle -> Command -> Awaiting Response -> Processing -> Answer Ready -> Transmitted).

### Modified Capabilities

## Impact

- `main_gui.py`: Add UI element (Clear Log), update event handlers to manage the new state-based protocol flow.
- `serial_handler.py`: Ensure state resets (clearing buffers) are triggered correctly on connection.
