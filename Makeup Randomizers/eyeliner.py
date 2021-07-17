import tkinter
import random

# GUI Stuff
window = tkinter.Tk()
window.title("Graphic Eyeliner Randomizer")
window.geometry("800x300")

# Functions
# Chooses palette and colors
def colors():
    reset_button["state"] = "normal"
    colors_button["state"] = "disabled"
    shades = ["Pastels", "Neons"]
    shade = random.choice(shades)
    shade_result["text"] = "{0}".format(shade)
    if shade == "Pastels":
        pastels = ["Pastel Pink", "Pastel Orange", "Pastel Yellow", "Pastel Green", "Pastel teal", "Pastel Blue", "Pastel Purple", "White"]
        pastel1 = random.choice(pastels)
        pastel2 = random.choice(pastels)
        pastel3 = random.choice(pastels)
        colors_result["text"] = "{0}, {1}, {2}".format(pastel1, pastel2, pastel3)
    elif shade == "Neons":
        neons = ["Neon Pink", "Neon Red", "Neon Orange", "Neon Yellow", "Neon Green", "Neon Blue", "Neon Purple", "Black"]
        neon1 = random.choice(neons)
        neon2 = random.choice(neons)
        neon3 = random.choice(neons)
        colors_result["text"] = "{0}, {1}, {2}".format(neon1, neon2, neon3)

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
    colors_button["state"] = "normal"
    type_button["state"] = "normal"
    colors_result["text"] = ""
    shade_result["text"] = ""
    type_result["text"] = ""

#Buttons
colors_button = tkinter.Button(window, text="Palette", command=colors, state="normal")
colors_button.pack()

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