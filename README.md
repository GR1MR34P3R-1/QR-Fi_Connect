# 📶 QR-Fi Connect

This Python script generates a QR code for a specified Wi-Fi network, allowing easy sharing of network credentials with others. The generated QR code can be scanned by devices to quickly connect to the Wi-Fi network.

# 🚀 Quick Start

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running the following command:
3. Clone this repository or download the `main.py` file.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the script using the following command:python3 main.py
6. Follow the on-screen instructions to select a Wi-Fi network and enter the password.
7. Once completed, the script will generate a QR code image named `wifi_qr_code.png` in the current directory.

# 🔧 Dependencies

This script requires the following Python libraries:
- `qrcode`: Used to generate QR codes.
- `wifi`: Used to retrieve available Wi-Fi network details.

# 🎯 Usage

1. Run the script using the provided instructions.
2. The script will display a list of available Wi-Fi networks.
3. Enter the corresponding number for the desired network.
4. Enter the Wi-Fi password for the selected network.
5. The script will generate a QR code image named `wifi_qr_code.png`.
6. Share the generated QR code with others to easily connect to the Wi-Fi network.

# 💡 Tips

- Make sure your Wi-Fi interface name is correctly set in the script (replace `'wlo1'` with your interface name).
- Adjust the encryption type (`encryption_type`) in the `generate_wifi_qr_code` function based on your network's security settings.

# 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Happy Wi-Fi sharing! 📶✨
