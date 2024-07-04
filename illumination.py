import tkinter as tk
import colorsys

def hsv_to_rgb(h, s, v):
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}'

def update_color():
    global hue
    hue += 0.01
    if hue > 1:
        hue = 0
    color = hsv_to_rgb(hue, 1, 1)
    canvas.configure(bg=color)
    root.after(50, update_color)

root = tk.Tk()
root.title("Illumination Effect")
root.geometry("400x400")
root.configure(bg='#000000')

hue = 0

canvas = tk.Canvas(root, width=400, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

update_color()

root.mainloop()
