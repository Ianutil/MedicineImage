#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""
import base64
import json
import time

import cv2
import numpy as np
import requests
import threading


def request_url(request):
    res = requests.post("http://115.159.221.182:5123/image_classify/v1/child_detection", json=request)
    print(time.strftime('%H:%M:%S', time.localtime()) + res.text)

def detect_face():
    # cv2.namedWindow("test")
    cap = cv2.VideoCapture(0)  # 加载摄像头录制
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

    # haarcascade_frontalface_default.xml
    file = "/Users/ianchang/Public/2017-11-23/face_detect_n_track-master/haarcascade_frontalface_default.xml"
    classifier = cv2.CascadeClassifier(file)
    encode_faces = []
    cap_frame_num = 0
    while True:
        success, frame = cap.read()
        # cap_time = round(time.time() * 1000)
        # pre_cap_time = cap_time
        size = frame.shape[:2]
        image = np.zeros(size, dtype=np.float16)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(image, image)
        divisor = 8
        h, w = size
        minSize = (w // divisor, h // divisor)
        faceRects = classifier.detectMultiScale(image, 1.1, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect
                face_array = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                img_encode = cv2.imencode('.jpg', face_array)[1]
                byte_image = (str(base64.b64encode(img_encode))[2:-1])
                encode_faces.append(byte_image)

                if len(encode_faces) >= 1:
                    req = {"store_id": "sh1001", "device_id": "A1010", "image": encode_faces}
                    thread = threading.Thread(target=request_url, args=(req,))
                    thread.start()
                    # res = requests.post("http://10.10.10.4:5123/image_classify/v1/child_detection", json=req)
                    # print(time.strftime('%H:%M:%S', time.localtime()) + res.text)
                    encode_faces.clear()
                cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 2)

        cv2.imshow("capture", frame)
        key = cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
    cv2.destroyWindow("capture")


if __name__ == "__main__":
    print("Hello World")
    detect_face()
