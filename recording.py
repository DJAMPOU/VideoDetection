import cv2 as cv
from tkinter import *
import threading

global rcd
def recording(self):
    if self.val_record.get() == 1 and self.val_record_pre == 0:
        self.val_record_pre = 1
        choose_directory(self)
    else:
        self.val_record.set(0)
        self.val_record_pre = 0
        stop()

def choose_directory(self):
    fen = Toplevel(self)
    fen.title("recording directory")
    cd = Entry(fen, name="direction", width=100)
    cd.pack()
    cd.bind("<Return>", lambda event: go(self=self, fen=fen, cd=cd, event=event))
    fen.mainloop()

def go(self,fen, cd, event):
    global rcd
    dir = cd.get()
    fen.destroy()
    rcd = record(self, dir)
    rcd.start()

def stop():
    rcd.stop = 1
class record(threading.Thread):

    def __init__(self, boss, dir):
        threading.Thread.__init__(self)
        self.boss = boss
        self.dir = dir
        self.stop = 0

    def run(self):
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter(self.dir, fourcc, 20.0, (500, 400))
        while True:
            frame = self.boss.loop.frame_f
            out.write(frame)
            cv.waitKey(40)
            if self.stop == 1:
                break
        out.release()

