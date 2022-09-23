from io import BytesIO

import PIL
import qrcode
from PIL import Image
# import matplotlib.pyplot as plt
from PIL import ImageDraw
# from PIL import ImageFont


def getQRcode(strs, ico_path="./olimp_croped.jpg"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=100,
        border=2,
    )


    qr.add_data(strs)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("CMYK")  # RGBA
    icon = Image.open(ico_path)
    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # icon = icon.resize((icon_w, icon_h))
    icon = icon.resize((size_w, size_h))
    w = int((img_w - size_w) / 2)
    h = int((img_h - size_h) / 2)
    # w = int((img_w - icon_w) / 2)
    # h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), None)
    img = img.convert('RGB')
    # img.save(name)
    return img


def info(body) ->PIL.Image.Image:
    qrImg = getQRcode(body, ico_path="./olimp_croped.jpg")

    bg_img_path = './rainbow_suqare.png'
    fg_img_path = './olimp.jpg'
    qr_size = 1024
    # qr_size = 490
    border_sise = 80
    bg_size = qr_size+2*border_sise

    bgImg = Image.open(bg_img_path)
    bgImg = bgImg.resize((bg_size, bg_size))
    # qrImg = Image.open(name)
    qrImg = qrImg.resize((qr_size, qr_size))
    bgImg.paste(qrImg, (border_sise, border_sise))
    draw = ImageDraw.Draw(bgImg)
    bgImg = bgImg.convert('RGB')
    # bgImg.save(name)
    # return bgImg
    return qrImg

if __name__ == '__main__':
    txt = 'Lorem ipsum — dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.'
    ur = "https://www.topcoder.com"
    img = info(txt)
    img.save("qrcode_result2.png")
    print(img)
    print(type(img))
    # img.tobytes()
    f_bytes = BytesIO()
    f_bytes: BytesIO
    img.save(fp=f_bytes,format="png")
    # print(f_bytes.getbuffer().tobytes())




