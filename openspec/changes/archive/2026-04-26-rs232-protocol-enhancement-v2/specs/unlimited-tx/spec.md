## ADDED Requirements

### Requirement: Unlimited TX
The system SHALL NOT limit the length of command frames transmitted over the serial port.

#### Scenario: Transmitting long frame
- **WHEN** user inputs a command longer than 5 bytes
- **THEN** system transmits the entire frame via RS232
