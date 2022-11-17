from tkinter import *
import cv2 as cv
from PIL import ImageTk, Image
import threading
import time
from loop import *
from recording import *



class appli(Frame):

    def __init__(self):
        Frame.__init__(self)

        self.loop = loop(self)
        self.loop.start()

        self.block_left = Frame(self)
        self.block_left.grid(row=0, column=0)

        self.block_right = Frame(self)
        self.block_right.grid(row=0, column=2)

        #left block
        self.val_record = IntVar(self)
        self.val_record_pre = 0
        Radiobutton(self.block_left, text="Recording", variable=self.val_record, value=1, command=lambda:recording(self)).grid(row=0, column=0)

        self.list_detect_color = ["nothing", "red", "blue", "green", "white", "black"]
        self.var_detect_color = StringVar(self)
        self.var_detect_color.set(self.list_detect_color[0])
        Label(self.block_left, text="Unique color").grid(row=1, column=0)
        self.opt_detect_color = OptionMenu(self.block_left, self.var_detect_color, *self.list_detect_color)
        self.opt_detect_color.grid(row=2, column=0)
        self.opt_detect_color.bind("<Configure>", self.detect)

        self.list_detect_form = ["nothing", "rectangle", "triangle", "circle"]
        self.var_detect_form = StringVar(self)
        self.var_detect_form.set(self.list_detect_form[0])
        Label(self.block_left, text="Unique form").grid(row=3, column=0)
        self.opt_detect_form = OptionMenu(self.block_left, self.var_detect_form, *self.list_detect_form)
        self.opt_detect_form.grid(row=4, column=0)

        self.list_delete_bg = ['nothing', 'black', 'white']
        self.var_delete_bg = StringVar()
        self.var_delete_bg.set(self.list_delete_bg[0])
        Label(self.block_left, text="delete background").grid(row=5, column=0)
        self.opt_delete_bg = OptionMenu(self.block_left, self.var_delete_bg, *self.list_delete_bg)
        self.opt_delete_bg.grid(row=6, column=0)

        #right block
        self.sc_threshold = Scale(self.block_right, label="threshold", from_=0, to=255, tickinterval=55, length=150, orient=HORIZONTAL, command=self.loop.threshold)
        self.sc_threshold.grid(row=0, column=0)

        Label(self.block_right, text="Detect").grid(row=1, column=0)

        self.var_border = IntVar(self)
        self.radio_border=Radiobutton(self.block_right, variable=self.var_border, value=1, text="Border", command=self.loop.detect_border)
        self.radio_border.grid(row=2, column=0)

        self.var_face = IntVar(self)
        self.radio_face = Radiobutton(self.block_right, variable=self.var_face, value=1, text="Face", command=self.loop.detect_face)
        self.radio_face.grid(row=3, column=0)

        self.var_identity = IntVar(self)
        self.radio_identity = Radiobutton(self.block_right, variable=self.var_identity, value=1, text="identity", command=self.loop.detect_gender)
        self.radio_identity.grid(row=4, column=0)

        self.var_motion = IntVar(self)
        self.radio_motion = Radiobutton(self.block_right, variable=self.var_motion, value=1, text="Motion")
        self.radio_motion.grid(row=5, column=0)

        self.bout_refresh = Button(self.block_right, text="refresh")
        self.bout_refresh.grid(rows=6, column=0)

    def detect(self, event):
        if self.var_detect_color.get() != "nothing" or self.var_detect_form != "nothing" or self.var_delete_bg != "nothing":
            self.loop.detect_unique = 1
        else:
            self.loop.detect_unique = 0
if __name__ == '__main__':
    fen = Tk()
    my_appli = appli()
    my_appli.pack()
    fen.mainloop()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
