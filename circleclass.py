import tkinter as tk

class Circle(object):
    def __init__(self, center, radius):  
        self.center = center
        self.radius = radius

    def draw(self, canvas, color='light pink'):  
        rad = self.radius
        x1 = self.center[0] - rad
        y1 = self.center[1] - rad
        x2 = self.center[0] + rad
        y2 = self.center[1] + rad
        canvas.create_oval(x1, y1, x2, y2, fill=color)

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

biggest_circle = Circle([200, 200], 150)  
biggest_circle.draw(canvas, color='light green')
outer_circle = Circle([200, 200], 100)  
outer_circle.draw(canvas, color='light pink')
inner_circle = Circle([200, 200], 50)  
inner_circle.draw(canvas, color='light blue')
window.mainloop()