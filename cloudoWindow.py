import tkinter as tk
import tkinter.scrolledtext as tkst
import pyautogui as pag


class CloudoWindow:
    def __init__(self, btn_callback):
        self.root = tk.Tk()
        self.root.title('cloudo')
        self.font ='Arial'

        screen_width, screen_height = pag.size()
        self.appWidth = screen_width / 2
        self.appHeight = screen_height

        self.canvas = tk.Canvas(self.root, width=self.appWidth, height=self.appHeight)

        self.background_image = tk.PhotoImage(file='imgs/sky.png')
        self.backgroundLabel = tk.Label(self.root, image=self.background_image)

        self.input = tk.Entry(self.root, bg='white', font=(self.font, 12))

        # self.weatherInfoLabel = tk.Label(self.root, justify='left', anchor='nw')

        self.weatherInfoText = tkst.ScrolledText(self.root)

        self.btn = tk.Button(self.root, bg='#1394eb', fg='white', highlightcolor='#9ad0f5', text='Search',
                             font=(self.font, 12), command=lambda: btn_callback(self.input.get(),
                                                                                self.weatherInfoText))
        self.place_widgets()

    def place_widgets(self):
        self.canvas.pack()
        self.backgroundLabel.place(relwidth=1, relheight=1)
        self.input.place(relx=0.45, rely=0.15, relwidth=0.3, relheight=0.04, anchor='n')
        self.btn.place(relx=0.7, rely=0.15, relwidth=0.1, relheight=0.04, anchor='n')
        self.weatherInfoText.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.7, anchor='n')

