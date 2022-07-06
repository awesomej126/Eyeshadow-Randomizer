import tkinter
import random
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Graphic Eyeliner Randomizer")
window.geometry("800x500")

# Palette Images
neon_image = ImageTk.PhotoImage(Image.open('Eyeliner/neon.jpg').resize((200, 200)))
pastel_image = ImageTk.PhotoImage(Image.open('Eyeliner/pastel.jpg').resize((200, 200)))
colour_galaxy_image = ImageTk.PhotoImage(Image.open('Eyeliner/colourgalaxy.jpg').resize((200, 200)))

# Functions
# Chooses palette and colors
def colors():
    reset_button["state"] = "normal"

    colors_button["state"] = "disabled"
    shades = ["Pastels", "Neons", "Colour Galaxy"]
    shade = random.choice(shades)
    shade_result["text"] = "".join(shade)

    pastels = ["Pastel Pink", "Pastel Orange", "Pastel Yellow", "Pastel Green", "Pastel Teal", "Pastel Blue", "Pastel Purple", "White"]
    neons = ["Neon Pink", "Electric Neon Orange", "Neon Orange", "Neon Yellow", "Neon Green", "Neon Blue", "Neon Purple", "Black"]
    colour_galaxy = ["Pink", "Yellow", "Orange", "Red", "Purple", "Blue", "Green", "Gray"]

    num = random.randint(1, 3)

    if shade == "Pastels":
        shade_pic["image"] = pastel_image
        pastel = random.choices(pastels, k=num)
        if len(pastel) == 1:
            colors_result["text"] = "".join(pastel)
        elif len(pastel) == 2:
            colors_result["text"] = "{0}, {1}".format(pastel[0], pastel[1])
        else:
            colors_result["text"] = "{0}, {1}, {2}".format(pastel[0], pastel[1], pastel[2])

    elif shade == "Neons":
        shade_pic["image"] = neon_image
        neon = random.choices(neons, k=num)
        if len(neon) == 1:
            colors_result["text"] = "".join(neon)
        elif len(neon) == 2:
            colors_result["text"] = "{0}, {1}".format(neon[0], neon[1])
        else:
            colors_result["text"] = "{0}, {1}, {2}".format(neon[0], neon[1], neon[2])

    elif shade == "Colour Galaxy":
        shade_pic["image"] = colour_galaxy_image
        galaxy = random.choices(colour_galaxy, k=num)
        if len(galaxy) == 1:
            colors_result["text"] = "".join(galaxy)
        elif len(galaxy) == 2:
            colors_result["text"] = "{0}, {1}".format(galaxy[0], galaxy[1])
        else:
            colors_result["text"] = "{0}, {1}, {2}".format(galaxy[0], galaxy[1], galaxy[2])

# Chooses style
def liner_type():
    reset_button["state"] = "normal"

    type_button["state"] = "disabled"
    types = ["Floating Crease Liner", "Double Liner", "Dotted Liner", "Flames", "Winged", "Whatever The Fuck You Want"]
    t = random.choice(types)
    type_result["text"] = "".join(t)

# Resets program
def reset():
    reset_button["state"] = "disabled"
    colors_button["state"] = type_button["state"] = "normal"
    colors_result["text"] = shade_result["text"] = type_result["text"] = shade_pic["image"] = ""


# Buttons
colors_button = tkinter.Button(window, text="Palette", command=colors, state="normal")
colors_button.pack()

shade_pic = tkinter.Label(window, image="")
shade_pic.pack()

shade_result = tkinter.Label(window, text="")
shade_result.pack()

colors_result = tkinter.Label(window, text="")
colors_result.pack()

type_button = tkinter.Button(window, text="Type", command=liner_type, state="normal")
type_button.pack()

type_result = tkinter.Label(window, text="")
type_result.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset, state="disabled")
reset_button.pack()

window.mainloop()
