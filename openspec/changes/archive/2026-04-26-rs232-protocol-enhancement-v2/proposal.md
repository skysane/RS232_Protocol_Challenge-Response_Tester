## Why

The current RS232 testing tool requires more flexible input, an accurate checksum calculation, and more configurable transmission and timeout behaviors to better support various communication protocols.

## What Changes

- **Flexible Input**: Allow users to toggle between string and HEX input for command frames.
- **Enhanced CS Algorithm**: Redefine the checksum calculation logic: sum all data, take the lowest 8 bits, and represent as two ASCII characters (high-nibble + low-nibble).
- **Unlimited Transmission**: Remove length restrictions on command data transmission.
- **Adjustable Timeout**: Modify timeout behavior to initiate timer (1-300s, default 5s) only after transmission, displaying a timeout message only after the configured period.

## Capabilities

### New Capabilities
- `flexible-input`: Allows switching between string/HEX inputs.
- `enhanced-cs`: Implements the new 2-byte CS calculation.
- `unlimited-tx`: Removes command transmission length constraints.
- `deferred-timeout`: Implements post-transmission timer with configurable duration.

### Modified Capabilities
- `rs232-comm`: Updating serial handler to support variable transmission lengths and updated timeout logic.

## Impact

- `main_gui.py`: UI updates for input mode toggling, new timeout field, and transmission logic.
- `challenge_response_logic.py`: Update CS algorithm to match new requirement.
- `serial_handler.py`: Update serial communication to handle dynamic transmit lengths.
