# Specification: Unlimited Data Reception

## Overview
Remove the dependency on fixed-length reading to support variable-length RS232 frames.

## Requirements
- The serial handler shall read all available data from the buffer.
- The system shall not pre-define a maximum receive frame length.
- The handler shall maintain efficiency to prevent blocking the GUI.
