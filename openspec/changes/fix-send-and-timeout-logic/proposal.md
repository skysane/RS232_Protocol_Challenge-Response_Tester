## Why

The current data transmission and timeout logic is incorrectly sequenced. The command needs to be sent first, followed immediately by the initiation of the timeout timer and data reception listener.

## What Changes

- **Correct Sequence**: Update `send_command` in `main_gui.py` to initiate timeout timer and start reception immediately after the command is sent.
- **Immediate Feedback**: Ensure data received within the timeout period cancels the timer and displays the data immediately.

## Capabilities

### New Capabilities
- `correct-transmission-sequence`: Ensures the timeout and reception logic begins exactly when a command is dispatched.

### Modified Capabilities

## Impact

- `main_gui.py`: Refactor `send_command` event flow.
