#!/usr/bin/python
#coding=utf-8
#0000.py
#author:TianFengX

from PIL import Image, ImageDraw, ImageFont

class ImageMessage:
    def __init__(self):
        self.im = None
        self.fnt = None
    
    def open(self, path):
        self.im = Image.open(path)
        return True

    def setFont(self, font, size):
        self.fnt = ImageFont.truetype(font, size)
        #self.fnt = ImageFont.load_default().font
        return True

    def drawImage(self, str_number, color):
        draw = ImageDraw.Draw(self.im)
        x, y = self.im.size
        draw.text((x-50, 7), str_number, color, self.fnt)
        self.im.show()
        self.im.save('0001.jpg')

number = str(5)
windows_fnt = 'FreeSans.ttf'
number_color = (250, 0, 0)
def main():
    print("0000.py main")
    ImageMsg = ImageMessage()
    ImageMsg.open("0000.jpg")
    ImageMsg.setFont(windows_fnt, 80)
    ImageMsg.drawImage(number, number_color)

if __name__ == "__main__":
    main()
else:
    print("0000.py was imported !")

