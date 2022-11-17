import threading
import cv2
from detect_unique import *
from detect import *

class loop(threading.Thread):

    def __init__(self, boss):
        threading.Thread.__init__(self)
        self.cap = cv.VideoCapture(0)
        self.boss = boss
        self.frame = cv.imread("ac.jpg")
        self.frame_f = cv.resize(self.frame, (500, 400))
        cv.imshow("test", self.frame_f)
        self.detect_unique = 0
        self.detect_bord = 0
        self.detect_fc = 0
        self.detect_gd = 0
        self.th = 0

    def run(self):
        while True:
            _, self.frame = self.cap.read()
            self.frame = cv.flip(self.frame, 1)
            self.frame_f = cv.resize(self.frame, (500, 400))
            if self.th !=0:
                self.frame_f = cv.cvtColor(self.frame_f, cv.COLOR_BGR2GRAY)
                _, self.frame_f = cv.threshold(self.frame_f, self.th, 255, 0)
                self.frame_f = cv2.cvtColor(self.frame_f, cv.COLOR_GRAY2BGR)
            if self.detect_unique == 1:
                self.frame_f = unique_color(self.frame_f, self.boss.var_detect_color.get())
                #self.frame_f = unique_form(self.frame_f, self.boss.var_detect_form.get())

            if self.detect_bord == 1:
                self.frame_f = border(self.frame_f)

            if self.detect_fc == 1:
                self.frame_f = face(self.frame_f)

            if self.detect_gd == 1:
                self.frame_f = identity(self.frame_f)
            cv.imshow("test", self.frame_f)
            key = cv.waitKey(1)
            if key==ord(" "):
                break

    def threshold(self, value):
        self.th = int(value)

    def detect_border(self):
        if self.detect_bord == 0 and self.boss.var_border.get() == 1:
            self.detect_bord = 1

        elif self.detect_bord == 1 and self.boss.var_border.get() == 1:
            self.detect_bord = 0
            self.boss.var_border.set(0)

    def detect_face(self):
        if self.detect_fc == 0 and self.boss.var_face.get() == 1:
            self.detect_fc = 1

        elif self.detect_fc == 1 and self.boss.var_face.get() == 1:
            self.detect_fc = 0
            self.boss.var_face.set(0)

    def detect_gender(self):
        if self.detect_gd == 0 and self.boss.var_identity.get() == 1:
            self.detect_gd = 1

        elif self.detect_gd == 1 and self.boss.var_identity.get() == 1:
            self.detect_gd = 0
            self.boss.var_identity.set(0)