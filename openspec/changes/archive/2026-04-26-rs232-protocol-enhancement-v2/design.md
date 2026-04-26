## Context

The RS232 tool needs to handle more complex protocol scenarios including flexible input, updated checksums, and delayed timeout handling.

## Goals / Non-Goals

**Goals:**
- Provide flexible input mechanism (String/HEX toggle).
- Correctly implement 2-byte ASCII encoded CS logic.
- Support arbitrary length data transmission.
- Implement post-transmission timeout timer.

**Non-Goals:**
- Supporting communication protocols other than RS232.
- Refactoring the entire UI framework.

## Decisions

- **Input Handling**: GUI will add a toggle (e.g., Radio button) to switch interpretation of user input for command frame.
- **CS Logic**: Centralize CS in `challenge_response_logic.py`. The algorithm will perform the sum, mask lower 8 bits, then split into high/low nibble ASCII.
- **Timeout**: Move timer logic into GUI level, triggered by the "Transmit" event, with customizable wait duration.
- **Transmission**: `SerialHandler.send_data()` will be used to pass raw byte stream without fixed-length checks.

## Risks / Trade-offs

- [Risk] GUI responsiveness during timeout period.  Use non-blocking timers (e.g., `master.after()` or threading).
