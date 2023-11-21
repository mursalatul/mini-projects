import tkinter as tk

class GUI:
    # store app instance
    app = None
    def __init__(self, app):
        self.app = app
        self.create()
    
    # create basic design of app
    def create(self):
        self.app.title("GNU Sound Enhancer")
        self.app.geometry('350x200')

        # scale
        self.slider = tk.Scale(self.app, from_=0, to=100, orient=tk.HORIZONTAL)
        self.slider.pack()
        
        # creating frame to store the 3 buttons
        self.three_button_frame = tk.Frame(self.app,  bd=5, relief=tk.GROOVE, highlightbackground="red", highlightcolor="red")
        self.three_button_frame.pack( )

        # plus button
        self.plus_button = tk.Button(self.three_button_frame, text="+")
        self.plus_button.pack(side=tk.LEFT)

        # minus button
        self.minus_button = tk.Button(self.three_button_frame, text="-")
        self.minus_button.pack(side=tk.LEFT)

        # exit button
        self.minus_button = tk.Button(self.three_button_frame, text= 'X')
        self.minus_button.pack(side=tk.LEFT)
    
    # def functions(self):


def main():
    app = tk.Tk()
    controll = GUI(app)
    app.mainloop()

if __name__ == "__main__":
    main()
