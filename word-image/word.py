# idea to do a dic mapping of the word to the image

from PIL import Image
import os
import sys

#create a blank png image
new = Image.new("RGB",(1200,1280),(255,255,255))
x, y = 0,0

#get text
##if len(sys.argv) != 2:
##    sys.exit("Usage: python word.py text")
text = open(r"C:\Users\Asus\OneDrive\Desktop\ML\Handwriting Project\word-image\dumb.text")
reader = text.read().replace("\n","")
# Get my letters dir
for i in reader:
    letter = Image.open("test\{}.jpg".format(str(ord(i)))).resize((100,100))
    print(letter)
    new.paste(letter, (x,y))
    x += letter.width
    if x > 1200 or len(i)*115 > (1200-x):
        x,y=0,y+140
new.save("test.png", "PNG")
