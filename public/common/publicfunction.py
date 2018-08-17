#coding=utf-8
import time

from config import globalparam


# 截图放到report下的img目录下
def get_img(dr, filename):
    time_c = time.strftime("%Y-%m-%d_%H-%M-%S_")
    path = globalparam.img_path + '\\' +time_c+filename
    dr.take_screenshot(path)

