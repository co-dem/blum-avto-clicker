from PIL import Image, ImageGrab, ImageEnhance
import pyautogui as pg
import time


#* variables
global con
con = 1
cords = []
filename = 'finaltest.png'
greens = [250, 251, 252, 253, 254, 255]
reds, blues = [250, 251, 252, 253, 254, 255], [0]

#* applying filters
#? using recursion method
def editImage_func():
    screenschot = ImageGrab.grab().crop((0,0,480,820)).save(filename)
    img_tmp = Image.open(filename)

    img1 = ImageEnhance.Contrast(img_tmp).enhance(2)
    return ImageEnhance.Color(img1).enhance(2)

def findAndClick_func(img_to_click):
    rgb_im = img_to_click.convert("RGB")
    for y in [190, 250]:
        for x in range(img_to_click.size[0]):
            x = int((x * 10) / 2)
            if x < 480:
                pix = rgb_im.getpixel((x, y))
                if pix[0] in reds and pix[1] in greens:
                    pg.moveTo(x=x,y=y)
                    pg.click()
            else:
                break

if __name__ == '__main__':
    time.sleep(5)
    while con != 80:
        findAndClick_func(editImage_func())
        time.sleep(0.1)
        con += 1