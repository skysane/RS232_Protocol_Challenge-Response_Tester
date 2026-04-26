## Context

The project is an RS232 testing tool. Currently, the UI and logic have fixed-length reception and limited verification capabilities. The goal is to make the tool more flexible for various protocols by adding custom challenge-response verification and user-controlled transmission.

## Goals / Non-Goals

**Goals:**
- Provide a flexible verification engine for challenge-response testing.
- Allow user-defined verification blocks with custom logic (XOR/Addition).
- Implement a transmission trigger.
- Remove data reception length constraints.
- Standardize timeout to seconds.

**Non-Goals:**
- Supporting communication protocols other than RS232.
- Replacing the existing GUI framework.

## Decisions

- **Verification Engine**: Verification logic will be centralized in `challenge_response_logic.py`, utilizing a clear interface to pass block data.
- **Data Reception**: The serial handler will switch from fixed buffer sizes to dynamic reading to remove length constraints.
- **UI Architecture**: New input fields and the transmit button will be added to the existing `main_gui.py` layout, following the existing structure.
- **Timeout**: The input logic will be updated to handle floating-point or integer values as seconds, normalizing to seconds before passing to the pyserial configuration.

## Risks / Trade-offs

- **Risk**: Dynamic reception could lead to high memory usage if the sender sends an infinite stream without breaks.
    - **Mitigation**: Implement a reasonable maximum buffer limit per read cycle or periodic clearing if necessary, keeping it configurable if required in future.
- **Risk**: Adding complexity to the GUI could clutter the UI.
    - **Mitigation**: Group verification blocks and transmission controls logically, perhaps using grouping elements in the GUI.
