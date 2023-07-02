# 📶 QR-Fi Connect
QR-Fi Connect is a Python script that generates a QR code for a specified Wi-Fi network, enabling easy sharing of network credentials with others. The generated QR code can be scanned by devices to quickly connect to the Wi-Fi network.

# 🚀 Quick Start
Ensure that Python is installed on your system.
Install the required dependencies by running the following command:
pip install qrcode wifi
Clone this repository or download the main.py file.
Open a terminal or command prompt and navigate to the project directory.
Run the script using the following command:
python main.py
Follow the on-screen instructions to select a Wi-Fi network and enter the password.
Upon completion, the script will generate a QR code image named wifi_qr_code.png in the current directory.

# 🔧 Dependencies
This script requires the following Python libraries:
qrcode: Used to generate QR codes.
wifi: Used to retrieve available Wi-Fi network details.
Install these dependencies using the following command:
pip install qrcode wifi

# 🎯 Usage
Run the script using the provided instructions.
The script will display a list of available Wi-Fi networks.
Enter the corresponding number for the desired network.
Enter the Wi-Fi password for the selected network.
The script will generate a QR code image named wifi_qr_code.png.
Share the generated QR code with others to easily connect to the Wi-Fi network.

# 💡 Tips
Ensure that your Wi-Fi interface name is correctly set in the script. Replace 'wlo1' in the get_wifi_interface function with your interface name.
Adjust the encryption type (encryption_type) in the generate_qr_code function based on your network's security settings.

# 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

Happy Wi-Fi sharing! 📶✨
