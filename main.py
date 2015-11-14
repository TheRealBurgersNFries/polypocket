''' This is the way in which the computer and leap are to 
    interact. Further reading is required to determine the
    connectivity with the Photon. Poly Pocket is a pocket 
    polygraph device. It uses a few resistors and LEDs, 
    photosensors and a few other things to '''

from tkinter import Tk, BOTH, CENTER
from tkinter.ttk import Frame, Button, Style, Label
import Leap

class poly_pocket(Frame):
    def __init__(self):
        window = Tk()
        self.parent = window
        window.geometry("800x600+50+50")
        Frame.__init__(self, window)
        self.baseline = 0
        self.initUI()
        window.mainloop()
    def initUI(self):
        # Initialize and name Window
        self.parent.title("Poly Pocket")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        def new_baseline():

            return
        def old_baseline():
            return
        def test(baseline):
            return
        def spark_connect():
            return
        def leap_connect():
            return
        def quit():
            self.parent.destroy()
            return

        welcome = "Welcome to Poly Pocket!"
        welcome_label = Label(self, text=welcome, font=("Helvetica", 24))
        welcome_label.place(x=5, y=5)
        welcome_label.pack()
        
        baseline_button = Button(self, text="New Baseline",
                command=new_baseline())
        recover_baseline_button = Button(self, text="Recover Baseline",
                command=old_baseline())
        test_button = Button(self, text="Conduct Test",
                command=test(self.baseline))
        connect_leap_button = Button(self, text="Establish Leap Connection",
                command=leap_connect)
        connect_spark_button = Button(self, text="Establish Spark Connection",
                command=spark_connect)
        exit_button = Button(self, text="Quit",
                command=quit)
        
        baseline_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        recover_baseline_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        test_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        connect_leap_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        connect_spark_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        exit_button.place(relx=0.5, rely = 0.8, anchor=CENTER)



poly_pocket()
