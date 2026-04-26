## ADDED Requirements

### Requirement: Enhanced CS Algorithm
The system SHALL calculate CS by summing all payload bytes, taking the lowest 8 bits, and outputting as two ASCII-encoded hex characters.

#### Scenario: CS Calculation
- **WHEN** user enables CS and transmits data
- **THEN** system appends two bytes representing the hex value of the lower 8 bits of the sum.
