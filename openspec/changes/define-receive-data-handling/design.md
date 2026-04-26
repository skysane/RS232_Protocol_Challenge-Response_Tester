## Context

The project is an RS232 testing tool. Currently, the UI and logic have fixed-length reception and potentially ambiguous timeout units. The goal is to normalize these to enhance protocol compatibility.

## Goals / Non-Goals

**Goals:**
- Standardize timeout inputs and configuration to seconds.
- Enable unlimited data reception by removing fixed buffer limits.

**Non-Goals:**
- Adding new communication protocols.
- Refactoring the entire UI framework.

## Decisions

- **Timeout**: The UI and `serial_handler.py` will explicitly use seconds for `pyserial` configuration.
- **Data Reception**: The serial handler will move from fixed-size `ser.read(n)` calls to a dynamic approach, likely utilizing `ser.in_waiting` or a reading loop until silence, ensuring all bytes are captured.

## Risks / Trade-offs

- **Risk**: Dynamic reception could lead to high memory usage if the sender sends an infinite stream.
    - **Mitigation**: Implement a reasonable maximum buffer limit per read cycle or periodic clearing if necessary.
