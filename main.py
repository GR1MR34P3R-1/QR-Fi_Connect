import platform

# Import libraries based on the operating system
if platform.system() == "Linux":
    import qrcode
    import wifi
elif platform.system() == "Windows":
    import qrcode
    import wifi

def get_wifi_details():
    wifi_networks = []

    cells = wifi.Cell.all('wlo1')  # Replace 'wlo1' with your Wi-Fi interface name

    for cell in cells:
        ssid = cell.ssid
        wifi_networks.append(ssid)

    return wifi_networks

def generate_wifi_qr_code(ssid, password, encryption_type):
    # Wi-Fi network details
    wifi_data = f'WIFI:S:{ssid};T:{encryption_type};P:{password};;'

    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(wifi_data)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    qr_image.save('wifi_qr_code.png')
    print("Wi-Fi QR code generated successfully.")

# Retrieve Wi-Fi network details
networks = get_wifi_details()

if len(networks) == 0:
    print("No Wi-Fi networks found.")
else:
    print("Available Wi-Fi networks:")
    for i, ssid in enumerate(networks):
        print(f"{i+1}. {ssid}")

    network_index = int(input("Select a Wi-Fi network (enter the corresponding number): "))
    password = input("Enter the Wi-Fi password: ")

    if network_index < 1 or network_index > len(networks):
        print("Invalid network selection.")
    else:
        ssid = networks[network_index - 1]
        encryption_type = "WPA"  # Set the encryption type based on your network security

        generate_wifi_qr_code(ssid, password, encryption_type)