import tkinter as tk
from tkinter import messagebox
import qrcode
import platform
import os
import subprocess

class WifiQRCodeGeneratorUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wi-Fi QR Code Generator")

        self.ssid_label = tk.Label(self.window, text="Wi-Fi SSID:")
        self.ssid_entry = tk.Entry(self.window)
        self.password_label = tk.Label(self.window, text="Wi-Fi Password:")
        self.password_entry = tk.Entry(self.window, show="*")
        self.generate_button = tk.Button(self.window, text="Generate QR Code", command=self.generate_qr_code)

        self.ssid_label.pack(pady=(10, 0))
        self.ssid_entry.pack(fill=tk.X, padx=10)
        self.password_label.pack(pady=(10, 0))
        self.password_entry.pack(fill=tk.X, padx=10)
        self.generate_button.pack(pady=(20, 10))

        self.populate_ssid_entry()

    def populate_ssid_entry(self):
        connected_ssid = self.get_connected_wifi_ssid()
        if connected_ssid:
            self.ssid_entry.insert(0, connected_ssid)

    def get_connected_wifi_ssid(self):
        try:
            if platform.system() == "Linux":
                iwconfig_output = subprocess.check_output(["iwconfig"], encoding="utf-8")
                for line in iwconfig_output.splitlines():
                    if "ESSID" in line:
                        ssid = line.split('"')[1]
                        return ssid

            elif platform.system() == "Windows":
                netsh_output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], encoding="utf-8")
                for i, line in enumerate(netsh_output.splitlines()):
                    if "SSID" in line and "BSSID" in netsh_output.splitlines()[i + 1]:
                        ssid = line.split(":")[1].strip()
                        return ssid

        except (subprocess.CalledProcessError, FileNotFoundError):
            return None

    def generate_qr_code(self):
        ssid = self.ssid_entry.get().strip()
        password = self.password_entry.get()

        if not ssid:
            messagebox.showerror("Error", "Please enter a Wi-Fi SSID.")
            return

        encryption_type = "WPA"
        wifi_data = f'WIFI:S:{ssid};T:{encryption_type};P:{password};;'

        try:
            qr = qrcode.QRCode(
                version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
            )
            qr.add_data(wifi_data)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            script_dir = os.path.dirname(os.path.abspath(__file__))
            qr_image.save(os.path.join(script_dir, 'wifi_qr_code.png'))

            messagebox.showinfo("Success", "Wi-Fi QR code generated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = WifiQRCodeGeneratorUI()
    app.run()
