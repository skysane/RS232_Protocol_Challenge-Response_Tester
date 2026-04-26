## Context

The current tester lacks log management (clearing history) and has a loose communication flow. To make it a more robust tool for sequential verification, a formal protocol state machine must be enforced in the UI.

## Goals / Non-Goals

**Goals:**
- Add "Clear Log" functionality.
- Enforce strict communication protocol sequence.
- Ensure all serial state resets are automated upon connection.

**Non-Goals:**
- Automated state transitions (all transitions are user-triggered).

## Decisions

- **UI Interaction**: Add `Clear` button in the Log frame.
- **Protocol Flow**: Update `RS232TesterGUI` methods (`send_command`, `transmit_answer`, `on_timeout`) to explicitly manage the communication state transitions.
- **State Reset**: Add call to serial buffer reset during the `connect` and `disconnect` logic in `SerialHandler`.

## Risks / Trade-offs

- [Risk] Protocol getting stuck in an invalid state.
  - Mitigation: Any error, timeout, or reset event returns the protocol state to Idle, allowing re-initiation of commands.
