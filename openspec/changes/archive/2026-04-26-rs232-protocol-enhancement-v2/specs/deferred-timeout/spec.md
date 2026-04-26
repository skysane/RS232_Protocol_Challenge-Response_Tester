## ADDED Requirements

### Requirement: Deferred Timeout
The system SHALL start a configurable timeout timer (1-300s) only AFTER the transmission finishes, and alert the user if no response arrives within that window.

#### Scenario: Triggering timeout
- **WHEN** user transmits data and no response is received within the configured timeout period
- **THEN** system displays a timeout message
