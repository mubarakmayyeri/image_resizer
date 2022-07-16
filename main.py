from PIL import Image
import os

#C:\Users\mubar\Pictures\Camera Roll\1.png
path = input("Enter image path : ")
im = Image.open(path)

ext = os.path.splitext(path)[-1].lower()
width = int(input("Enter width : "))
length = int(input("Enter length : "))

size = width, length
new_image = im.resize(size)

new_image.show()

if ext == ".jpg":
    new_image.save('resized.jpg')
elif ext == ".png":
    new_image.save('resized.png')
else:
    print("Invalid file format")
