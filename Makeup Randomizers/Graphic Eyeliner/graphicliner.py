import tkinter
import random
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Graphic Eyeliner Randomizer")
window.geometry("800x500")

# Palette Images
neon_image = ImageTk.PhotoImage(Image.open('neon.jpg').resize((200, 200)))

pastel_image = ImageTk.PhotoImage(Image.open('pastel.jpg').resize((200, 200)))

# Functions
# Chooses palette and colors
def colors():
    reset_button["state"] = "normal"
    colors_button["state"] = "disabled"
    shades = ["Pastels", "Neons"]
    shade = random.choice(shades)
    shade_result["text"] = "{0}".format(shade)
    if shade == "Pastels":
        shade_pic["image"] = pastel_image
        pastels = ["Pastel Pink", "Pastel Orange", "Pastel Yellow", "Pastel Green", "Pastel Teal", "Pastel Blue", "Pastel Purple", "White"]
        pastel_1 = random.choice(pastels)
        pastel_2 = random.choice(pastels)
        pastel_3 = random.choice(pastels)
        colors_result["text"] = "{0}, {1}, {2}".format(pastel_1, pastel_2, pastel_3)
    elif shade == "Neons":
        shade_pic["image"] = neon_image
        neons = ["Neon Pink", "Neon Red", "Neon Orange", "Neon Yellow", "Neon Green", "Neon Blue", "Neon Purple", "Black"]
        neon_1 = random.choice(neons)
        neon_2 = random.choice(neons)
        neon_3 = random.choice(neons)
        colors_result["text"] = "{0}, {1}, {2}".format(neon_1, neon_2, neon_3)

# Chooses style
def type():
    reset_button["state"] = "normal"
    type_button["state"] = "disabled"
    types = ["Floating Crease Liner", "Double Liner", "Dotted Liner", "Creative Liner"]
    type = random.choice(types)
    type_result["text"] = "".join(type)

# Resets program
def reset():
    reset_button["state"] = "disabled"
    colors_button["state"] = type_button["state"] = "normal"
    colors_result["text"] = shade_result["text"] = type_result["text"] = shade_pic["image"] = ""

#Buttons
colors_button = tkinter.Button(window, text="Palette", command=colors, state="normal")
colors_button.pack()

shade_pic = tkinter.Label(window, image="")
shade_pic.pack()

shade_result = tkinter.Label(window, text="")
shade_result.pack()

colors_result = tkinter.Label(window, text="")
colors_result.pack()

type_button = tkinter.Button(window, text="Type", command=type, state="normal")
type_button.pack()

type_result = tkinter.Label(window, text="")
type_result.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset, state="disabled")
reset_button.pack()

window.mainloop()