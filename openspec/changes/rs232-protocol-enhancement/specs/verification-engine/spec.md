## ADDED Requirements

### Requirement: Custom Verification Engine
The system SHALL support 4 verification blocks, each taking two bytes from the user and applying custom addition/XOR logic to determine the 8-bit result.

#### Scenario: Perform verification calculation
- **WHEN** user provides input bytes for a verification block
- **THEN** system calculates the 8-bit result based on defined addition/XOR rules and displays it

### Requirement: Checksum (CS) Handling
The system SHALL append a 2-byte CS to the transmission if the CS option is enabled by the user.

#### Scenario: Enable CS for transmission
- **WHEN** user enables the CS checkbox and triggers transmission
- **THEN** system appends a calculated 2-byte CS to the data packet
