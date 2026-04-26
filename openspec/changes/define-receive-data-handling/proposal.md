## Why

The current RS232 testing tool lacks flexibility in configuration and data handling, specifically regarding timeout units and receive buffer length. Standardizing these will improve usability and compatibility with various RS232 protocols.

## What Changes

- **Timeout Configuration**: Standardize all timeout settings to use seconds as the unit.
- **Data Reception**: Remove length restrictions on received data to support variable-length frames.

## Capabilities

### New Capabilities
- `timeout-config`: Standardization of timeout units to seconds.
- `unlimited-rx`: Removal of packet length limits for incoming serial data.

## Impact

- `serial_handler.py`: Update logic for timeout handling and data reception.
- `main_gui.py`: Update UI labels and input handling for timeout settings.
