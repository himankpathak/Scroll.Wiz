import tkinter as tk


mname = ['Scroll Mode','YoutubeMode','YoutubeMode2']

def center_window(root,width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def PopUp(mnum):
	r = tk.Tk()
	button = tk.Button(r, text=mname[mnum], width=25, command=r.destroy)
	button.config(font=("Courier", 15))
	button.pack()
	center_window(r,180,50)
	r.overrideredirect(1)
	r.after(1200, r.destroy)
	r.mainloop()
