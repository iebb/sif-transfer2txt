from pytesseract import image_to_string
from PIL import Image, ImageChops
import os, glob
os.environ["PATH"] += ";.\\tesseract\\"
os.environ["TESSDATA_PREFIX"] = ".\\tesseract\\"
out = open("result.txt", "w+")
for f in glob.glob("./codes/*.png") + glob.glob("./codes/*.jpg"):
    Im = Image.open(f)
    bg = Image.new(Im.mode, Im.size, Im.getpixel((0,0)))
    diff = ImageChops.difference(Im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    Im = Im.crop(diff.getbbox())
    cropped = Im.crop((Im.size[0] * 0.5, Im.size[1] * 0.22, Im.size[0] * 0.8, Im.size[1] * 0.35))
    result = image_to_string(cropped, lang = "num", config = "digits")
    out.write(f + " " + result + "\n")
    print f, result