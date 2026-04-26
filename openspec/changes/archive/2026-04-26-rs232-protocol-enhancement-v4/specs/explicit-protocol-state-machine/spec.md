## ADDED Requirements

### Requirement: Protocol State Machine
The system SHALL strictly follow the defined communication flow: Connection (auto-reset) -> Command Input -> Send -> Await/Receive Challenge -> Manual User Verification/Answer Trigger. Timeout events MUST reset the flow to the Idle state.

#### Scenario: Verify protocol reset on timeout
- **WHEN** a timeout occurs after sending a command
- **THEN** the system logs the timeout and returns to an idle state ready for a new command input
