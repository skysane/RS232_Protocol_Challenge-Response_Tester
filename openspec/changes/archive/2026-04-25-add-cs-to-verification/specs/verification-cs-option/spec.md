## ADDED Requirements

### Requirement: Verification Checksum Option
The system SHALL provide an option for the user to enable Checksum calculation when transmitting verification data.

#### Scenario: Enabling Checksum for verification
- **WHEN** user enables 'CS' option in the verification data settings and triggers verification
- **THEN** system calculates checksum of the verification data and appends it to the transmission
