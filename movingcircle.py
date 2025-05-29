import tkinter as tk

class Circle(object):
    def __init__(self, center, radius, fill='light blue', outline='black', outline_width=1):
        self.center = center
        self.radius = radius
        self.fill = fill
        self.outline = outline
        self.outline_width = outline_width

    def draw(self, canvas):
        rad = self.radius
        x1 = self.center[0] - rad
        y1 = self.center[1] - rad
        x2 = self.center[0] + rad
        y2 = self.center[1] + rad
        canvas.create_oval(
            x1, y1, x2, y2,
            fill=self.fill,
            outline=self.outline,
            width=self.outline_width
        )

window = tk.Tk()
window.title("Multiple Circles")

canvas = tk.Canvas(window, width=400, height=200)
canvas.pack()

for i in range(120):
    canvas.delete("all")
    circle1 = Circle(center=[80 + i * 2, 100], radius=70, fill='light blue', outline='navy', outline_width=2)
    circle2 = Circle(center=[80 + i * 2, 100], radius=50, fill='light green', outline='dark green', outline_width=2)
    circle3 = Circle(center=[80 + i * 2, 100], radius=30, fill='light pink', outline='red', outline_width=2)
    circle1.draw(canvas)
    circle2.draw(canvas)
    circle3.draw(canvas)
    window.after(20)
    window.update()

window.mainloop()