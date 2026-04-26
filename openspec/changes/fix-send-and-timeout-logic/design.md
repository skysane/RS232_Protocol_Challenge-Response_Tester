## Context

The current `RS232TesterGUI.send_command` logic triggers reception before confirming that the command has been successfully written and the timeout timer is correctly active.

## Goals / Non-Goals

**Goals:**
- Enforce the sequence: Send -> Start Timer -> Receive.

**Non-Goals:**
- Changing existing challenge-response logic.

## Decisions

- **Flow Control**: Reorder operations in `send_command` so the timer starts immediately after `serial_handler.send_data()` returns success, followed by the call to receive data.

## Risks / Trade-offs

- [Risk] GUI hang during reception.
  - Mitigation: Reception currently uses `serial.read_all()`, ensure this remains non-blocking or at least respects the configured serial timeout.
