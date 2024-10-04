from PIL import Image, ImageGrab, ImageEnhance
import pyautogui as pg
import time


#* variables
con = 1
cords = []
filename = 'finaltest.png'
greens = [250, 251, 252, 253, 254, 255]
reds, blues = [250, 251, 252, 253, 254, 255], [0]




#* applying filters
#? using recursion method
def editImage_func(num, img, iters):
#* make a screenshot and save it
    time.sleep(4)
    screenschot = ImageGrab.grab()
    screenschot.save(fp=filename)
#* open, crop, convert color scheme to RGB and save it again
    img_tmp = Image.open(filename)
    img_tmp.crop((0,0,480,820)).save(filename)
#* open the ready for proccessing file
    img_tmp = Image.open(filename)

    if num == iters:
        print('done')
        return img
    else:
        num += 1
        img1 = ImageEnhance.Contrast(img).enhance(2)
        img2 = ImageEnhance.Color(img1).enhance(2)
        editImage_func(num, img2, iters)

def findAndClick_func(img_to_click):
# def findAndClick_func():
    rgb_im = img_to_click.convert("RGB")
    for y in [190, 250]:
    # for y in [150, 152]:
        cords.clear()
        for x in range(img_to_click.size[0]):
        # for x in range(img_tmp.size[0]):

            x = int((x * 10) / 2)
            if x >= 480:
                break
            else:
                pix = rgb_im.getpixel((x, y))
                if pix[0] in reds and pix[1] in greens:
                    cords.append((x, y))

        for i in cords:
            pg.moveTo(x=i[0],y=i[1])
            pg.click()

if __name__ == '__main__':
    while con != 10:
        # editImage_func(num=1, img=img_tmp, iters=4)
        findAndClick_func(editImage_func(num=1, img=img_tmp, iters=4))
        time.sleep(0.8)
        con+=1