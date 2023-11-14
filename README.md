# PictureToText Encoder
This is a small program that takes a file that can encode a message into a picture and then decodes it. To encode a message it takes all of the RGBA values of the image and checks if there are any encoded characters inside the picture and resets them to some trivial value. Since it is transparent it does not matter what this value is. Then it makes all of the pixels on the y-axis transparent as that is where the characters are going to be encoded and RGB values changed. Once this is done it uses the message and then replaces the RGBA values on the y-axis with the encoded values. To decode it does looks up the key to signify an encoded value and then decodes the pixels in that location and creates the message.

# How to use
To use this file you download the main.py file. It needs the Tkinter and Pillow libraries to run. Once you have the files and libraries downloaded you can run the file in the command line. Follow the commands on the menu to encode and decode. If the window to select the file does not appear it is most likely behind the window you are currently on.

Commands:
- cd c:\Users\your\file\path
- pip install Pillow
- pip install tk
- py main.py

# Future add-ons
In the future I hope to make it be able to encode more pixels inside the picture without being noticeable to make the amount of characters inside the message not limited by the height of the image.
