#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""
import cv2
import numpy as np

def cleanWatermark_01(path):
    src = cv2.imread(path)  # 默认的彩色图(IMREAD_COLOR)方式读入原始图像
    cv2.imshow("SRC", src)

    mask = cv2.imread('./resource/mask_jd.png', cv2.IMREAD_GRAYSCALE)  # 灰度图(IMREAD_GRAYSCALE)方式读入水印蒙版图像
    # thresh = cv2.inRange(mask, np.array([250, 250, 250]), np.array([255, 255, 255]))
    # cv2.imshow("MASK", thresh)
    # 参数：目标修复图像; 蒙版图（定位修复区域）; 选取邻域半径; 修复算法(包括INPAINT_TELEA/INPAINT_NS， 前者算法效果较好)
    dst = cv2.inpaint(src, mask, 3, cv2.INPAINT_TELEA)

    cv2.imwrite('./resource/result.jpg', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cleanWatermark(path):
    img = cv2.imread(path)
    hight, width, depth = img.shape[0:3]

    # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
    # thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
    thresh = cv2.inRange(img, np.array([209, 164, 166]), np.array([255, 255, 255]))

    # 创建形状和尺寸的结构元素
    kernel = np.ones((3, 3), np.uint8)

    # 扩张待修复区域
    hi_mask = cv2.dilate(thresh, kernel, iterations=1)
    specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

    cv2.namedWindow("Image", 0)
    cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
    cv2.imshow("Image", img)

    cv2.namedWindow("newImage", 0)
    cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
    cv2.imshow("newImage", specular)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def makeWatermark(path):
    img = cv2.imread(path)
    height, width = img.shape[0:2]
    # 开始操作
    thresh = cv2.inRange(img, np.array([209, 164, 166]), np.array([192, 192, 192]))
    # thresh = cv2.inRange(img, np.array([0, 0, 0]), np.array([192, 192, 192]))
    scan = np.ones((3, 3), np.uint8)
    cor = cv2.dilate(thresh, scan, iterations=1)
    specular = cv2.inpaint(img, cor, 5, flags=cv2.INPAINT_TELEA)
    # 操作结束，下面开始是输出图片的代码
    cv2.namedWindow("image", 0)
    # cv2.resizeWindow("image", int(width / 2), int(height / 2))
    cv2.imshow("image", img)

    cv2.namedWindow("modified", 0)
    # cv2.resizeWindow("modified", int(width / 2), int(height / 2))
    cv2.imshow("modified", specular)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Hello World")
    path = "./file/image/1340/1.jpg"
    # makeWatermark(path)
    # cleanWatermark(path)
    cleanWatermark_01(path)
