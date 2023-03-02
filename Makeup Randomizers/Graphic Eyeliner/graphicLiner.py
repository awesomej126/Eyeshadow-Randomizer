import tkinter
import random
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Graphic Eyeliner Randomizer")
window.geometry("800x800")

# Palette Images
neon_image = ImageTk.PhotoImage(Image.open('neon.jpg').resize((150, 150)))
pastel_image = ImageTk.PhotoImage(Image.open('pastel.jpg').resize((150, 150)))
colour_galaxy_image = ImageTk.PhotoImage(Image.open('colour_galaxy.jpg').resize((150, 150)))

pastels = ("Pink Velvet", "Peaches & Cream", "Banana Split", "Key Lime", "Ice Pop", "Blue Raspberry", "Gelato", "Skate Date")
neons = ("Roller Skate", "Hot Pants", "Chill Pill", "Crop Top", "Spandex", "Mood Ring", "Tie Dye", "Disco Fever")
colour_galaxy = ("Hard Candy", "Lemon Lush", "Mango Sunrise", "Bandana", "Platforms", "Bell Bottoms", "Sour Apple", "Graphite")
palettes = (pastels, neons, colour_galaxy)
palette_names = ("Pastels", "Neons", "Colour Galaxy")
palette_images = (pastel_image, neon_image, colour_galaxy_image)

# Functions
# Selects only one palette and chooses random shades
def one_palette():
    index = random.randint(0, 2)
    shade_num = random.randint(1, 3)
    palette_pic["image"] = palette_images[index]
    shades = random.sample(palettes[index], k=shade_num)
    palette_result["text"] = "".join(palette_names[index])
    colors_result["text"] = ", ".join(shades)

# Selects two palettes and chooses random shades
def two_palettes():
    index = random.sample(range(3), k=2)
    shade_num_1 = random.randint(1, 2)
    shade_num_2 = random.randint(1, 2)
    palette_pic["image"] = palette_images[index[0]]
    palette_pic_2["image"] = palette_images[index[1]]
    shades_1 = random.sample(palettes[index[0]], k=shade_num_1)
    shades_2 = random.sample(palettes[index[1]], k=shade_num_2)
    shades = shades_1 + shades_2
    palette_result["text"] = f"{palette_names[index[0]]} & {palette_names[index[1]]}"
    colors_result["text"] = ", ".join(shades)

# Selects all three palettes and chooses random shades
def three_palettes():
    palette_result["text"] = f"{palette_names[0]}, {palette_names[1]}, & {palette_names[2]}"
    palette_pic["image"] = colour_galaxy_image
    palette_pic_2["image"] = neon_image
    palette_pic_3["image"] = pastel_image
    galaxy_shade = "".join(random.choice(colour_galaxy))
    neon_shade = "".join(random.choice(neons))
    pastel_shade = "".join(random.choice(pastels))
    colors_result["text"] = f"{galaxy_shade}, {neon_shade}, {pastel_shade}"

# Chooses palette and colors
def color_selector():
    reset_button["state"] = "normal"
    colors_button["state"] = "disabled"
    main_text["text"] = "Now choose the liner style..."

    num_input = input.get()

    if num_input == "1":
        one_palette()

    elif num_input == "2":
        two_palettes()

    elif num_input == "3":
        three_palettes()

    else:
        main_text["text"] = "Invalid number"


# Chooses style
def style():
    reset_button["state"] = "normal"
    style_button["state"] = "disabled"
    main_text["text"] = "Here's your graphic liner look!!"

    styles = ["Floating Crease Liner", "Double Liner", "Dotted Liner", "Flames", "Winged", "Freestyle"]
    s = random.choice(styles)
    style_result["text"] = "".join(s)

# Resets program
def reset():
    main_text["text"] = "How many palettes do you want to use?"
    reset_button["state"] = "disabled"
    colors_button["state"] = style_button["state"] = "normal"
    colors_result["text"] = palette_result["text"] = style_result["text"] = palette_pic["image"] = palette_pic_2["image"] = palette_pic_3["image"] = ""
    user_input.delete(0, "end")

# Buttons & Text
main_text = tkinter.Label(window, text="How many palettes do you want to use? Choose a number between 1 and 3.")
main_text.pack()

input = tkinter.StringVar()
user_input = tkinter.Entry(window, textvariable=input)
user_input.pack()

colors_button = tkinter.Button(window, text="Palette/Palettes", command=color_selector, state="normal")
colors_button.pack(pady=8)

palette_pic = tkinter.Label(window, image="")
palette_pic.pack()

palette_pic_2 = tkinter.Label(window, image="")
palette_pic_2.pack()

palette_pic_3 = tkinter.Label(window, image="")
palette_pic_3.pack()

palette_result = tkinter.Label(window, text="")
palette_result.pack()

colors_result = tkinter.Label(window, text="")
colors_result.pack()

style_button = tkinter.Button(window, text="Style", command=style, state="normal")
style_button.pack()

style_result = tkinter.Label(window, text="")
style_result.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset, state="disabled")
reset_button.pack()

window.mainloop()
