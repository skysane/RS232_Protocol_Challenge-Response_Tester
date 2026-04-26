## ADDED Requirements

### Requirement: Correct Transmission Sequence
The system SHALL initiate the timeout timer and start data reception only AFTER the command has been successfully sent to the serial port.

#### Scenario: Verify sequence and timer
- **WHEN** the user initiates command transmission
- **THEN** the system sends the command, then activates the timeout timer, and THEN attempts to read incoming data
