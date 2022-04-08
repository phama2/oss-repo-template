from PIL import Image, ImageOps
import numpy

for pic in ["cloth1.png", "cloth2.png", "cloth3.png"]:
    # creates image objects
    i1 = Image.open(pic)

    # processing image
    # grayscale
    p1 = ImageOps.grayscale(i1)

    # resize to 28x28
    p1 = p1.resize((28,28))

    # Invert colors
    p1 = ImageOps.invert(p1)
    p1.save(pic.split(".")[0] + "_processed.png")