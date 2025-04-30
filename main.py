# QR Code Generator
# This program generates a QR code for a given website link.
# It validates the input URL and saves the QR code image in a specified folder.
# The program continues to prompt for new links until the user decides to exit.
import qrcode
import time
import os
import re

def is_valid_url(url):
    # URL validation
    pattern = re.compile(
        r'^(http://|https://)?'         # optional http(s)
        r'([\w\-]+\.)+[a-zA-Z]{2,6}'    # domain name
        r'(/[\w\-./?%&=]*)?$'           # optional path
    )
    return re.match(pattern, url)

# create a folder named 'qr-code' if it doesn't exist
folder_name = "qr-code"
os.makedirs(folder_name, exist_ok=True)

print("Welcome to QR Code Generator")
print("This program will generate a QR code for the website link you provide.")
print("Type '-1' to exit.")

while True:
    link = input("Enter website link: ").strip()

    if link == "-1":
            print("Exiting", end="", flush=True)
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            time.sleep(1)
            print("\nHave a great day/night!")
            break

    if not is_valid_url(link):
        print("Invalid input. Please enter a valid website link (e.g., https://www.joe50097.is-a.dev/) or -1 to exit.")
        continue

    # ensure link starts with http:// or https://
    if not link.startswith("http://") and not link.startswith("https://"):
        link = "https://" + link

    # generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # create a clean filename
    clean_link = link.replace("https://", "").replace("http://", "").rstrip("/").replace("/", "_")
    filename = f"{clean_link}.png"
    file_path = os.path.join(folder_name, filename)

    # save the QR code
    img.save(file_path)
    print(f"QR code saved as {file_path}\n")