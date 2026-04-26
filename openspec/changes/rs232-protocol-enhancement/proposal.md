## Why

The current RS232 testing tool requires more flexible configuration and verification mechanisms. Users need adjustable timeout units, unlimited data reception, and a more robust verification process involving custom XOR/Addition logic for challenge-response testing, along with the ability to initiate transmission after verification setup.

## What Changes

- **Timeout Configuration**: Standardize timeout settings to use seconds as the unit.
- **Data Reception**: Remove length restrictions on received data.
- **Enhanced Verification Logic**:
    - Users can define custom verification strings.
    - Implement a 4-block transmission verification:
        - Each block accepts two user-defined bytes.
        - Perform addition operations (default values: 0x1F, 0x20, 0x21, 0x22).
        - Retain only the lowest 8 bits.
        - Display results in the UI.
    - CS (Checksum) handling: If enabled, append 2-byte CS to the transmission.
    - New "Transmit" button to initiate data transfer after verification setup is complete.

## Capabilities

### New Capabilities
- `timeout-config`: Standardization of timeout units to seconds.
- `unlimited-rx`: Removal of packet length limits for incoming serial data.
- `verification-engine`: Implementation of the 4-block custom verification and CS calculation logic.
- `transmission-control`: UI control to initiate transmission after verification.

### Modified Capabilities
- `rs232-comm`: Updating serial handler to support longer data frames.

## Impact

- `challenge_response_logic.py`: Update core logic for verification calculations.
- `main_gui.py`: Update UI with new verification blocks, CS option, and Transmit button.
- `serial_handler.py`: Update data reception handling to remove buffer limitations.
