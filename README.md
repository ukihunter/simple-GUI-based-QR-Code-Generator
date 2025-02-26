# QR Code Generator by UKI

## Description

This is a simple GUI-based QR Code Generator created using Python, utilizing the `qrcode`, `customtkinter`, and `Pillow` libraries. The app allows users to input a URL and then generates a QR code for that URL that can be displayed on the screen.

### Features:
- **Enter URL**: Users can input any URL into a text field.
- **Generate QR Code**: On clicking the "Generate" button, the app creates a QR code for the given URL.
- **Display QR Code**: The generated QR code is displayed on the screen within a frame.
- **Scan the QR Code**: The QR code can be scanned using any QR code reader.

---

## Prerequisites

Make sure you have the following Python packages installed to run the app:

- `qrcode`
- `customtkinter`
- `Pillow`

You can install these dependencies using `pip`:

```bash
pip install qrcode[pil] customtkinter Pillow
How to Use
Launch the Application: Run the Python script to open the app window.
Enter a URL: In the text field, type the URL that you want to generate a QR code for.
Generate QR Code: Click the "Generate" button to create and display the QR code.
View the QR Code: The generated QR code will appear within a frame on the window. You can scan it using any QR code scanner.
Code Explanation
Libraries Used:
qrcode: To generate the QR code image.
customtkinter: To build the graphical user interface (GUI).
Pillow (PIL): To display the QR code image in the Tkinter window.
Application Components:
App Window: The main window of the app, created using customtkinter.CTk().
Title Label: A label at the top of the window displaying the title "QR Code GEN 🦆".
URL Entry: A text entry field where users can input the URL to generate a QR code for.
QR Code Frame: A frame that holds the generated QR code.
Generate Button: A button that, when clicked, triggers the generation of the QR code.
Functionality:
generate_qr(): This function takes the input from the text entry, generates a QR code using the qrcode library, and then resizes and displays it within the qr_label in the window.
Example Screenshot

(Include a screenshot of the app here)

License
This project is open-source and available for personal use. You may freely modify, distribute, or contribute to the project.

