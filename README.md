# Network Usage Tracker

The Network Usage Tracker is a Python application with a Tkinter GUI that allows users to monitor real-time network usage, store usage data in a MySQL database, and receive alerts when usage exceeds a predefined maximum limit.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Real-time Tracking:** Monitor network usage in real-time, displaying data in bytes per second.
- **Database Storage:** Store network usage data in a MySQL database for historical tracking and analysis.
- **Connection Status:** Display the current connection status and IP address.
- **Max Limit Alert:** Receive a notification if network usage exceeds a predefined maximum limit.

## Requirements

Ensure you have the following dependencies installed before running the application:

- Python 3.x
- Tkinter
- Pillow (PIL)
- psutil
- mysql-connector-python

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/network-usage-tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd network-usage-tracker
    ```

3. Install the required Python packages:

    ```bash
    pip install Pillow psutil mysql-connector-python
    ```

## Configuration

1. **MySQL Database:**
    - Create a MySQL database named `network_usage`.
    - Update the database connection details in the code (`host`, `user`, `password`).

2. **Application:**
    - Open the `network.py` file and modify any configuration variables if needed.

## Usage

1. Launch the application:

    ```bash
    python network.py
    ```

2. Click the "START" button to begin network usage tracking.
3. The main window will minimize, and a new window will display real-time network usage information.
4. To stop tracking, click the "STOP" button in the new window.

## Screenshots

![Main Window](Images/front.png)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
