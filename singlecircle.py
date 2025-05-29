import tkinter as tk

class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self, canvas):
        rad = self.radius
        x1 = self.center[0] - rad
        y1 = self.center[1] - rad
        x2 = self.center[0] + rad
        y2 = self.center[1] + rad
        canvas.create_oval(x1, y1, x2, y2, fill='light blue')

    def move(self, x, y):
        self.center = [x, y]
window = tk.Tk()
window.title("Circle Drawing")
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()
myCircle = Circle([100, 100], 50)
myCircle.draw(canvas)
window.mainloop()