# Plot the ISS

Welcome to **Plot the ISS**, a Python program that allows you to track the current location of the International Space Station (ISS) and visualize it on a map.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

Plot the ISS is a Python program that interacts with APIs to retrieve the ISS's current location and display it on a map. You can choose between two main options: "Where is the ISS?" and "Verify the location". Additionally, there's an option to exit the program.

## Features

- Fetch the real-time latitude and longitude of the ISS.
- View the ISS's current location on OpenStreetMap.
- Verify the ISS's location using NASA's tracking map.

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python installed (Python 3 recommended).
3. Install the required dependencies (see [Dependencies](#dependencies)).
4. Run the program by executing the script: `python plot_iss.py`.

## Usage

1. Run the program using the instructions provided in [Getting Started](#getting-started).
2. Choose one of the available options from the menu:
   - **1. Where is the ISS?**: Fetches the ISS's current latitude and longitude, then opens OpenStreetMap to display its location.
   - **2. Verify the location**: Opens NASA's tracking map for the ISS.
   - **3. Exit**: Terminate the program.
3. Follow the on-screen instructions to navigate through the options.

## Dependencies

- Python 3.x
- `webbrowser` (Python Standard Library)
- `json` (Python Standard Library)
- `urllib.request` (Python Standard Library)

## License

This project is licensed under the [MIT License](LICENSE).

