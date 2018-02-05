'''
pip install pytesseract
pip install pillow
'''

import pytesseract
from PIL import Image


def main():
    image = Image.open("aaaa.png")
    #image.show()
    print(image)
    #text = pytesseract.image_to_string(image)
    text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
    print(text)


if __name__ == '__main__':
    main()


