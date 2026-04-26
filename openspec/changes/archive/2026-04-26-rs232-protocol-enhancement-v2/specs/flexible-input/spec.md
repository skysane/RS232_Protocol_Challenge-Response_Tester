## ADDED Requirements

### Requirement: Flexible Input Toggle
The system SHALL provide an interface to switch input modes between "String" and "HEX" for the command frame.

#### Scenario: Switching input to HEX
- **WHEN** user selects "HEX" input mode
- **THEN** command entry accepts hexadecimal character pairs

#### Scenario: Switching input to String
- **WHEN** user selects "String" input mode
- **THEN** command entry accepts plain ASCII string characters
