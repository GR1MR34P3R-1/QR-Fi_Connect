import platform
import tkinter as tk
from tkinter import messagebox
import qrcode
import wifi

class WifiQRCodeGeneratorUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wi-Fi QR Code Generator")

        # Create labels and entry fields
        self.ssid_label = tk.Label(self.window, text="Wi-Fi SSID:")
        self.ssid_entry = tk.Entry(self.window)
        self.password_label = tk.Label(self.window, text="Wi-Fi Password:")
        self.password_entry = tk.Entry(self.window, show="*")
        self.generate_button = tk.Button(self.window, text="Generate QR Code", command=self.generate_qr_code)

        # Position labels and entry fields
        self.ssid_label.pack()
        self.ssid_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.generate_button.pack()

    def get_wifi_details(self):
        wifi_networks = []

        # Retrieve Wi-Fi cells
        wifi_interface = self.get_wifi_interface()
        cells = wifi.Cell.all(wifi_interface)

        # Extract SSID of each Wi-Fi network
        for cell in cells:
            ssid = cell.ssid
            wifi_networks.append(ssid)

        return wifi_networks

    def get_wifi_interface(self):
        if platform.system() == "Linux":
            return "wlo1"  # Default interface name for Linux
        elif platform.system() == "Windows":
            return "Wi-Fi"  # Default interface name for Windows

    def generate_qr_code(self):
        ssid = self.ssid_entry.get()
        password = self.password_entry.get()

        if ssid == "":
            messagebox.showerror("Error", "Please enter a Wi-Fi SSID.")
            return

        if password == "":
            messagebox.showerror("Error", "Please enter a Wi-Fi password.")
            return

        encryption_type = "WPA"  # Set the encryption type based on your network security

        # Generate and save the QR code
        try:
            wifi_data = f'WIFI:S:{ssid};T:{encryption_type};P:{password};;'
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(wifi_data)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")
            qr_image.save('wifi_qr_code.png')
            messagebox.showinfo("Success", "Wi-Fi QR code generated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        # Retrieve Wi-Fi network details
        wifi_networks = self.get_wifi_details()

        if len(wifi_networks) == 0:
            messagebox.showwarning("Warning", "No Wi-Fi networks found.")
            self.window.destroy()
            return

        # Set default SSID
        self.ssid_entry.insert(0, wifi_networks[0])

        self.window.mainloop()

if __name__ == "__main__":
    app = WifiQRCodeGeneratorUI()
    app.run()
