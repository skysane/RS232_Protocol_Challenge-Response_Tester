## ADDED Requirements

### Requirement: XOR Verification Logic
The system SHALL support 4 verification data sets, where users define the byte positions for XOR calculation and an Offset value.

#### Scenario: Performing XOR verification
- **WHEN** verification data is transmitted
- **THEN** system calculates XOR result based on defined bytes and applies offset before processing validation
