from PIL import Image
im = Image.open("rabbit.jpg")

print(im.format, im.size, im.mode)