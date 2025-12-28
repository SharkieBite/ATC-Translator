# Project: FAA Tower Request System

**Author:** Michael Mondaini  
**Date:** December 28, 2025  
**Language:** Python  

---------------------------------------------------------

This program is a command-line interface (CLI) simulation tool designed to replicate the communication procedures between Pilots and Air Traffic Control (ATC). It automates the generation of standard aviation phraseology for various flight phases, utilizing internal databases for ICAO airport codes and the NATO phonetic alphabet to ensure accurate formatting of requests and clearances.

## Functionality & Features

### Roles
* **Pilot Mode:** Allows the user to input flight details and generate standard requests for landing, takeoff, lineup & wait, taxiing, and startup/pushback.
* **ATC Mode:** Allows the user to act as the tower controller, issuing clearances and instructions to specific flights.
* **Registration System:** Includes options to pre-register flight details or tower locations to streamline the simulation session.

### Data Integration
* **Phonetic Alphabet Translator:** automatically converts taxiway codes (e.g., "A B") into their NATO phonetic equivalents (e.g., "Alfa, Bravo") for realistic output strings.
* **Airport Database:** Contains a dictionary of ICAO codes (e.g., `EGKK`, `GCLP`) mapped to their real-world airport names (Gatwick, Gran Canaria).

### Request Types Supported
1.  **Landing:** Approach and runway assignment.
2.  **Takeoff:** Departure clearance.
3.  **Line Up & Wait:** Runway entry instructions.
4.  **Taxi:** Routing to gates or runways using specific taxiways.
5.  **Startup & Pushback:** Pre-flight authorizations.

## Dependencies & Compatibility

* **Python 3.x**
* **OS Module:** The script utilizes `os.system('clear')` to refresh the user interface.
    * *Note:* This command is native to **Linux/macOS** environments. If running on Windows, the screen clear functionality may require changing `'clear'` to `'cls'`.

## Files in the repository
* `faa_tower_system.py`: The main script containing the logic for Pilot/ATC interaction, the phonetic dictionary, and the main execution loop.

## How to Run
1.  Execute the script in a terminal environment.
2.  Select your role from the main menu:
    * **1 - ATC:** Issue commands.
    * **2 - Pilot:** Request instructions.
    * **3 - Register:** Set a persistent location for the session.
3.  Follow the on-screen prompts to enter airline names, flight numbers, and specific runway/taxiway codes.
