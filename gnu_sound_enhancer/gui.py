import tkinter as tk
from control import volume
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
        self.slider = tk.Scale(self.app, from_=0, to=200, orient=tk.HORIZONTAL, command=self.changeVolume)
        self.slider.pack()
        
        # creating frame to store the 3 buttons
        self.three_button_frame = tk.Frame(self.app,  bd=5, relief=tk.GROOVE, highlightbackground="red", highlightcolor="red")
        self.three_button_frame.pack( )

        # exit button
        self.exit_button = tk.Button(self.three_button_frame, text= 'X', command=self.exitProgram)
        self.exit_button.pack(side=tk.LEFT)


    # increase volume 
    def changeVolume(self, vol):
        status = volume(str(100+int(vol)))

    # exit by setting the volume system 50%
    def exitProgram(self):
        status = volume("50")
        self.app.destroy()

def main():
    app = tk.Tk()
    controll = GUI(app)
    app.mainloop()

if __name__ == "__main__":
    main()
