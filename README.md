## 📶 QR-Fi Connect
![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

QR-Fi Connect is a Python script that generates a QR code for a specified Wi-Fi network, enabling easy sharing of network credentials with others. The generated QR code can be scanned by devices to quickly connect to the Wi-Fi network.

# Table of Contents

1. [Introduction](#introduction)
    1.1 [Quick Start](#quick-start)
    1.2 [Dependencies](#dependencies)

2. [Installation](#installation)
    2.1 [Ensure Python is Installed](#ensure-python-is-installed)
    2.2 [Install Required Dependencies](#install-required-dependencies)
    2.3 [Clone or Download](#clone-or-download)
    2.4 [Run the Script](#run-the-script)

3. [Usage](#usage)
    3.1 [Running the Script](#running-the-script)
    3.2 [Entering Wi-Fi Details](#entering-wi-fi-details)
    3.3 [Generating QR Code](#generating-qr-code)
    3.4 [Sharing QR Code](#sharing-qr-code)

4. [Tips](#tips)

5. [License](#license)

6. [Happy Wi-Fi sharing!](#happy-wi-fi-sharing)

## 🚀 Quick Start

1. Ensure that Python is installed on your system.
2. Install the required dependencies by running the following command:

   ```pip install qrcode wifi```

3. Clone this repository or download the main.py file.

4. Open a terminal or command prompt and navigate to the project directory.

5. Run the script using the following command:

    ```python3 main.py```

6. Follow the on-screen instructions to select a Wi-Fi network and enter the password.

7. Upon completion, the script will generate a QR code image named wifi_qr_code.png in the current directory.

## 🔧 Dependencies
This script requires the following Python libraries:

* qrcode: Used to generate QR codes.
* wifi: Used to retrieve available Wi-Fi network details.

Install these dependencies using the following command:

```pip install qrcode wifi```

## 🎯 Usage
1. Run the script using the provided instructions. The script will display a list of available Wi-Fi networks.
2. Enter the Wi-Fi password for the selected network.
3. The script will generate a QR code image named wifi_qr_code.png.
4. Share the generated QR code with others to easily connect to the Wi-Fi network.

## 💡 Tips
* Ensure that your Wi-Fi interface name is correctly set in the script. Replace 'wlo1' in the get_wifi_interface function with your interface name.
* Adjust the encryption type (encryption_type) in the generate_qr_code function based on your network's security settings.

## 📄 License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

## Happy Wi-Fi sharing! 📶✨
