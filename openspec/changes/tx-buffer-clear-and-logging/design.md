## Context

Currently, the `serial_handler.py` module manages serial communications without explicit TX buffer flushing before transmissions, leading to unpredictable behavior if data remains in the buffer. Furthermore, there is no integrated logging system to track the real-time flow of data, making validation difficult.

## Goals / Non-Goals

**Goals:**
- Implement a buffer clear routine in `serial_handler.py` to ensure clean transmission.
- Create a logging utility to intercept and store all transmitted and received data strings with timestamps.

**Non-Goals:**
- Implementing persistent disk-based logging beyond current session runtime (though the interface should allow for future extensibility).

## Decisions

- **Buffer Clearing**: Using `pyserial`'s built-in `reset_output_buffer()` method for efficiency and reliability.
- **Logging Interface**: Using the standard Python `logging` library configured to output to both console and a file-like buffer/GUI component to maintain flexibility.

## Risks / Trade-offs

- [Risk] Performance impact of logging every byte on high-speed serial. 
  - Mitigation: Ensure the logging operation is asynchronous or lightweight enough to not block the main transmission thread.
