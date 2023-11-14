from PIL import Image
import sys
import tkinter as tk
from tkinter import filedialog

keyboard_characters = [chr(i) for i in range(32, 127)]
# Add additional special characters
special_characters = "!\#$%&'()*+,-./:;<=>?@[]^_`{|}~"
keyboard_characters.extend(special_characters)
keyboard_characters.append('"')


class ImageEncoder:
    def __init__(self, image_path):
        self.image = Image.open(image_path).convert("RGBA")
        self.image_path = image_path

    def encode(self, message):
        for i in range(len(message)):
            keyboard_index = keyboard_characters.index(message[i])
            rgba: list = list(self.image.getpixel((0, i)))
            rgba[0] = 0
            rgba[1] = 255
            rgba[2] = keyboard_index
            rgba[3] = 0
            rgba: tuple = tuple(rgba)
            self.image.putpixel((0, i), rgba)

    def decode(self):
        indices = []
        rgba_values = list(self.image.getdata())
        for i in range(len(rgba_values)):
            if rgba_values[i][0] == 0 and rgba_values[i][1] == 255 and rgba_values[i][3] == 0:
                indices.append(keyboard_characters[rgba_values[i][2]])
        return "".join(indices)

    def resetImage(self):
        rgba_cleared = 0
        rgba_values = list(self.image.getdata())
        for i in range(len(rgba_values)):
            if rgba_values[i][0] == 0 and rgba_values[i][1] == 255 and rgba_values[i][3] == 0:
                rgba_value: list = list(rgba_values[i])
                rgba_value[0] = 100
                rgba_value[1] = 100
                rgba_value[3] = 0
                rgba_value: tuple = tuple(rgba_value)
                self.image.putpixel((0, i // self.image.width), rgba_value)
                rgba_cleared += 1
        for i in range(self.image.height):
            x = i % self.image.width
            y = i // self.image.width
            rgba_value: list = list(rgba_values[x * y])
            if rgba_value[3] != 0:
                rgba_value[3] = 0
                rgba_value: tuple = tuple(rgba_value)
                self.image.putpixel((0, i), rgba_value)
                rgba_cleared += 1
        self.image.save(self.image_path, "PNG")
        print(f"Cleared: {rgba_cleared} values.\n")

    def show(self, title):
        self.image.show(f"{title}")

    def getPixel(self, coordinates):
        return self.image.getpixel(coordinates)


def openFileDialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select an image file",
                                           filetypes=[("Image files",
                                                       "*.png;*.jpg;*.jpeg;*.bmp;*.ppm;*.pgm;*.pbm;*.tif;*.tiff,*.gif")])
    return file_path


def main():
    print("\n____________\n")
    print("Select a file to edit.")
    image_path = openFileDialog()
    if not image_path:
        print("\nNo file selected. Exiting.")
        sys.exit()
    image_controller = ImageEncoder(image_path)
    while True:
        print("\n____________\n")
        print("1. Encode a picture)")
        print("2. Decode a picture")
        print("3. View picture")
        print("4. Reset Picture")
        print("5. Choose Picture")
        print("6. Exit")
        controller = input("\n> ")
        match controller:
            case '1':
                print("\n____________\n")
                image_controller.resetImage()
                message = str(input("\nEnter a message you want to encode: "))
                image_controller.encode(message)
                image_controller.image.save(image_path, "PNG")
                print("\nEncoded successfully.")
                input("\n> ")
            case '2':
                print("\n____________\n")
                print(f"Message: {image_controller.decode()}")
                input("\n> ")
            case '3':
                image_controller.show("image")
            case '4':
                print("\n____________\n")
                image_controller.resetImage()
                print("Image Reset.")
                input("\n> ")
            case '5':
                print("\n____________\n")
                print("Select a file to edit.")
                image_path = openFileDialog()
                if not image_path:
                    print("\nNo file selected. Exiting.")
                    sys.exit()
                image_controller = ImageEncoder(image_path)
                print("Image Loaded.")
                input("\n> ")
            case '6':
                sys.exit()
            case _:
                print("\n____________\n")
                print("Invalid option.")
                input("\n> ")


if __name__ == '__main__':
    main()
