import qrcode
import customtkinter as ctk
from PIL import ImageTk, Image

app = ctk.CTk()
app.geometry("350x500")
app.title("QR Code GEN by UKI")

# Title Label
title_label = ctk.CTkLabel(app, text="QR Code GEN 🦆", font=("Stencil Std", 30))
title_label.place(x=60, y=10)

# Entry for URL
entry = ctk.CTkEntry(app, placeholder_text="Enter the URL", width=200)
entry.place(x=70, y=60)

# Frame to hold QR code
qr_frame = ctk.CTkFrame(app, width=250, height=250, corner_radius=10)
qr_frame.place(x=50, y=150)

# Label inside the frame to display the QR code
qr_label = ctk.CTkLabel(qr_frame, text="", width=250, height=250)
qr_label.place(relx=0.5, rely=0.5, anchor="center")

# Function to generate the QR code
def generate_qr():
    url = entry.get()  
    if url:
        img = qrcode.make(url)
        img = img.resize((250, 250))  # Resize to fit within the frame
        img_tk = ImageTk.PhotoImage(img)  
        qr_label.configure(image=img_tk)  # Display QR code
        qr_label.image = img_tk  # Keep a reference to the image to prevent garbage collection

# Button to trigger QR code generation
button = ctk.CTkButton(app, text="Generate", command=generate_qr)
button.place(x=90, y=100)

app.mainloop()
