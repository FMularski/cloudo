import tkinter as tk
import pyautogui as pag


class CloudoWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('cloudo')

        screen_width, screen_height = pag.size()
        self.appWidth = screen_width / 2
        self.appHeight = screen_height

        self.canvas = tk.Canvas(self.root, width=self.appWidth, height=self.appHeight)

        background_image = tk.PhotoImage(file='imgs/sky.png')
        self.backgroundLabel = tk.Label(self.root, image=background_image)

        self.place_widgets()

    def place_widgets(self):
        self.canvas.pack()
        self.backgroundLabel.place(relwidth=1, relheight=1)

        self.root.mainloop()