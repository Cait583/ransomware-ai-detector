# Ransomware AI Detector

## Overview
This project simulates an AI-powered ransomware attack detection system built in Python.  
It generates fake system logs, including simulated ransomware activities, analyzes them using rule-based AI logic, and immediately alerts a security analyst when a potential ransomware attack is detected.

## Features
- Generates fake system logs with normal and ransomware-like activity.
- Detects ransomware indicators using simple AI/rule-based detection.
- Sends urgent alert messages to the analyst console.
- Prompts the analyst to view detailed attack logs.
- Saves detected attack information into a log file for further investigation.

## Usage
1. Run the program with `python main.py`.
2. When an attack is detected, an urgent alert is displayed.
3. The analyst is prompted to view the detailed attack log.
4. Logs are saved automatically for record-keeping.

## Requirements
- Python 3.7 or higher
- Required Python packages (install with `pip install -r requirements.txt`):
  - pandas

## Project Structure
- `main.py` — Entry point for the detection system.
- `data_generator.py` — Generates fake system logs.
- `detector.py` — Contains AI/rule-based attack detection logic.
- `alert_system.py` — Handles alerts and analyst interaction.
- `attack_logs/` — Directory where detected attack logs are saved.

## Future Work
- Incorporate machine learning models for more accurate detection.
- Extend to detect other types of attacks.
- Build a GUI dashboard for real-time monitoring.

## Author
Cait583
