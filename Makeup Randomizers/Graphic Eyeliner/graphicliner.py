import tkinter
import random
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Graphic Eyeliner Randomizer")
window.geometry("800x800")

# Palette Images
neon_image = ImageTk.PhotoImage(Image.open('Eyeliner/neon.jpg').resize((150, 150)))
pastel_image = ImageTk.PhotoImage(Image.open('Eyeliner/pastel.jpg').resize((150, 150)))
colour_galaxy_image = ImageTk.PhotoImage(Image.open('Eyeliner/colourgalaxy.jpg').resize((150, 150)))

# Functions
def palette():
    pass
    
def pot():
    pass

# Chooses palette and colors
def colors():
    reset_button["state"] = "normal"
    colors_button["state"] = "disabled"
    main_text["text"] = "Now choose the liner style..."

    shades = ["Pastels", "Neons", "Colour Galaxy"]
    pastels = ["Pink Velvet", "Peaches & Cream", "Banana Split", "Key Lime", "Ice Pop", "Blue Raspberry", "Gelato", "Skate Date"]
    neons = ["Roller Skate", "Hot Pants", "Chill Pill", "Crop Top", "Spandex", "Mood Ring", "Tie Dye", "Disco Fever"]
    colour_galaxy = ["Hard Candy", "Lemon Lush", "Mango Sunrise", "Bandana", "Platforms", "Bell Bottoms", "Sour Apple", "Graphite"]

    num = random.randint(1, 3)

    if input.get() == "1":

        shade = random.choice(shades)
        shade_result["text"] = "".join(shade)

        if shade == "Pastels":
            shade_pic["image"] = pastel_image
            pastel = random.choices(pastels, k=num)
            colors_result["text"] = ", ".join(pastel)

        elif shade == "Neons":
            shade_pic["image"] = neon_image
            neon = random.choices(neons, k=num)
            colors_result["text"] = ", ".join(neon)

        elif shade == "Colour Galaxy":
            shade_pic["image"] = colour_galaxy_image
            galaxy = random.choices(colour_galaxy, k=num)
            colors_result["text"] = ", ".join(galaxy)

    elif input.get() == "2":
        shade = random.sample(shades, k=2)
        shade_result["text"] = "{0}, {1}".format(shade[0], shade[1])
        if shade[0] == "Pastels" and shade[1] == "Neons":
            shade_pic["image"] = pastel_image
            shade_pic2["image"] = neon_image
            color1 = "".join(random.choice(pastels))
            color2 = "".join(random.choice(neons))
            colors_result["text"] = "{0}, {1}".format(color1, color2)

        elif shade[0] == "Pastels" or shade[1] == "Colour Galaxy":
            shade_pic["image"] = pastel_image
            shade_pic2["image"] = colour_galaxy_image
            color1 = "".join(random.choice(pastels))
            color2 = "".join(random.choice(colour_galaxy))
            colors_result["text"] = "{0}, {1}".format(color1, color2)

        elif shade[0] == "Neons" or shade[1] == "Colour Galaxy":
            shade_pic["image"] = neon_image
            shade_pic2["image"] = colour_galaxy_image
            color1 = "".join(random.choice(neons))
            color2 = "".join(random.choice(colour_galaxy))
            colors_result["text"] = "{0}, {1}".format(color1, color2)

        elif shade[0] == "Neons" or shade[1] == "Pastels":
            shade_pic["image"] = neon_image
            shade_pic2["image"] = pastel_image
            color1 = "".join(random.choice(neons))
            color2 = "".join(random.choice(pastels))
            colors_result["text"] = "{0}, {1}".format(color1, color2)

        elif shade[0] == "Colour Galaxy" or shade[1] == "Pastels":
            shade_pic["image"] = colour_galaxy_image
            shade_pic2["image"] = pastel_image
            color1 = "".join(random.choice(colour_galaxy))
            color2 = "".join(random.choice(pastels))
            colors_result["text"] = "{0}, {1}".format(color1, color2)

        elif shade[0] == "Colour Galaxy" or shade[1] == "Neons":
            shade_pic["image"] = colour_galaxy_image
            shade_pic2["image"] = neon_image
            color1 = "".join(random.choice(colour_galaxy))
            color2 = "".join(random.choice(neons))
            colors_result["text"] = "{0}, {1}".format(color1, color2)

    elif input.get() == "3":
        shade_result["text"] = "{0}, {1}, & {2}".format(shades[0], shades[1], shades[2])
        shade_pic["image"] = colour_galaxy_image
        shade_pic2["image"] = neon_image
        shade_pic3["image"] = pastel_image
        galaxy = "".join(random.choice(colour_galaxy))
        neon = "".join(random.choice(neons))
        pastel = "".join(random.choice(pastels))
        colors_result["text"] = "{0}, {1}, {2}".format(galaxy, neon, pastel)
    else:
        main_text["text"] = "Invalid number"


# Chooses style
def style():
    reset_button["state"] = "normal"
    style_button["state"] = "disabled"
    main_text["text"] = "Here's your graphic liner look!!"

    styles = ["Floating Crease Liner", "Double Liner", "Dotted Liner", "Flames", "Winged", "Whatever The Fuck You Want"]
    s = random.choice(styles)
    style_result["text"] = "".join(s)

# Resets program
def reset():
    main_text["text"] = "How many palettes do you want to use?"
    reset_button["state"] = "disabled"
    colors_button["state"] = style_button["state"] = "normal"
    colors_result["text"] = shade_result["text"] = style_result["text"] = shade_pic["image"] = shade_pic2["image"] = shade_pic3["image"] = ""
    user_input.delete(0, "end")

# Buttons & Text
main_text = tkinter.Label(window, text="How many palettes do you want to use? Choose a number between 1 and 3.")
main_text.pack()

input = tkinter.StringVar()
user_input = tkinter.Entry(window, textvariable=input)
user_input.pack()

colors_button = tkinter.Button(window, text="Palette/Palettes", command=colors, state="normal")
colors_button.pack(pady=8)

shade_pic = tkinter.Label(window, image="")
shade_pic.pack()

shade_pic2 = tkinter.Label(window, image="")
shade_pic2.pack()

shade_pic3 = tkinter.Label(window, image="")
shade_pic3.pack()

shade_result = tkinter.Label(window, text="")
shade_result.pack()

colors_result = tkinter.Label(window, text="")
colors_result.pack()

style_button = tkinter.Button(window, text="Style", command=style, state="normal")
style_button.pack()

style_result = tkinter.Label(window, text="")
style_result.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset, state="disabled")
reset_button.pack()

window.mainloop()
