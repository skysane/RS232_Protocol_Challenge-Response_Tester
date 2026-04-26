## ADDED Requirements

### Requirement: Centralized Data Logging
The system SHALL intercept all serial data transmitted and received and log it with a high-resolution timestamp.

#### Scenario: Log transmission
- **WHEN** data is sent via the serial port
- **THEN** the system logs the data content, direction (TX), and the timestamp to the logger.

#### Scenario: Log reception
- **WHEN** data is received via the serial port
- **THEN** the system logs the data content, direction (RX), and the timestamp to the logger.
