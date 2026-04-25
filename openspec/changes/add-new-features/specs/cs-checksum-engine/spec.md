## ADDED Requirements

### Requirement: Checksum Calculation
The system SHALL provide an option to calculate the SUM of instruction fields and transmit it as a 2-byte hexadecimal ASCII string.

#### Scenario: Successful checksum transmission
- **WHEN** user enables 'CS' option and triggers transmission
- **THEN** system calculates SUM of fields, converts to low-byte hex ASCII, and transmits bytes sequentially
