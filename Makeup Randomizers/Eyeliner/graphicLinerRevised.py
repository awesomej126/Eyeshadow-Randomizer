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

# Palette names, shades, and images as well as eyeliner styles
PASTELS = ["Pink Velvet", "Peaches & Cream", "Banana Split", "Key Lime", "Ice Pop", "Blue Raspberry", "Gelato", "Skate Date"]
NEONS = ["Roller Skate", "Hot Pants", "Chill Pill", "Crop Top", "Spandex", "Mood Ring", "Tie Dye", "Disco Fever"]
COLOUR_GALAXY = ["Hard Candy", "Lemon Lush", "Mango Sunrise", "Bandana", "Platforms", "Bell Bottoms", "Sour Apple", "Graphite"]
SHADES = [PASTELS, NEONS, COLOUR_GALAXY]
NAMES = ["Pastels", "Neons", "Colour Galaxy"]
IMAGES = [pastel_image, neon_image, colour_galaxy_image]
STYLES = ["Floating Crease Liner", "Double Liner", "Dotted Liner", "Flames", "Winged", "Freestyle"]

# Functions
# Selects only one palette and chooses random shades
def one_palette():

    # Disables all palette buttons, enables reset button, changes main text
    one_palette_button.configure(state=tkinter.DISABLED)
    two_palettes_button.configure(state=tkinter.DISABLED)
    three_palettes_button.configure(state=tkinter.DISABLED)
    reset_button.configure(state=tkinter.NORMAL)
    main_text.configure(text="Now choose your eyeliner style...")

    index = random.randint(0, 2)
    num_shades = random.randint(1, 3)
    palette_image_label_1.configure(image=IMAGES[index])
    shades = random.sample(SHADES[index], k=num_shades)
    palette_result.configure(text="".join(NAMES[index]))
    colors_result.configure(text=", ".join(shades))

# Selects two palettes and chooses random shades
def two_palettes():

    # Disables all palette buttons, enables reset button, changes main text
    one_palette_button.configure(state=tkinter.DISABLED)
    two_palettes_button.configure(state=tkinter.DISABLED)
    three_palettes_button.configure(state=tkinter.DISABLED)
    reset_button.configure(state=tkinter.NORMAL)
    main_text.configure(text="Now choose your eyeliner style...")

    index = random.sample(range(3), k=2)
    shade_num_1 = random.randint(1, 2)
    shade_num_2 = random.randint(1, 2)
    palette_image_label_1.configure(image=IMAGES[index[0]])
    palette_image_label_2.configure(image=IMAGES[index[1]])
    shades_1 = random.sample(SHADES[index[0]], k=shade_num_1)
    shades_2 = random.sample(SHADES[index[1]], k=shade_num_2)
    shades = shades_1 + shades_2
    palette_result.configure(text=f"{NAMES[index[0]]} & {NAMES[index[1]]}")
    colors_result.configure(text=", ".join(shades))

# Selects all three palettes and chooses random shades
def three_palettes():

    # Disables all palette buttons, enables reset button, changes main text
    one_palette_button.configure(state=tkinter.DISABLED)
    two_palettes_button.configure(state=tkinter.DISABLED)
    three_palettes_button.configure(state=tkinter.DISABLED)
    reset_button.configure(state=tkinter.NORMAL)
    main_text.configure(text="Now choose your eyeliner style...")

    palette_result.configure(text=f"{NAMES[0]}, {NAMES[1]}, & {NAMES[2]}")
    palette_image_label_1.configure(image=colour_galaxy_image)
    palette_image_label_2.configure(image=neon_image)
    palette_image_label_3.configure(image=pastel_image)
    galaxy_shade = "".join(random.choice(COLOUR_GALAXY))
    neon_shade = "".join(random.choice(NEONS))
    pastel_shade = "".join(random.choice(PASTELS))
    colors_result.configure(text=f"{galaxy_shade}, {neon_shade}, {pastel_shade}")

# Chooses style
def style():
    style_button.configure(state=tkinter.DISABLED)
    reset_button.configure(state=tkinter.NORMAL)
    main_text.configure(text="Here's your graphic liner look!!")

    style = random.choice(STYLES)
    style_result.configure(text="".join(style))

# Resets program
def reset():

    # Enables all palette buttons, disables reset button
    one_palette_button.configure(state=tkinter.NORMAL)
    two_palettes_button.configure(state=tkinter.NORMAL)
    three_palettes_button.configure(state=tkinter.NORMAL)
    style_button.configure(state=tkinter.NORMAL)
    reset_button.configure(state=tkinter.DISABLED)

    # Restores main text, clears images and labels
    main_text.configure(text="How many palettes do you want to use?")
    palette_result.configure(text="")
    colors_result.configure(text="")
    style_result.configure(text="")
    palette_image_label_1.configure(image="")
    palette_image_label_2.configure(image="")
    palette_image_label_3.configure(image="")

# Buttons & Text
main_text = tkinter.Label(window, text="How many palettes do you want to use?")
main_text.pack()

one_palette_button = tkinter.Button(window, text="One Palette", command=one_palette, state="normal")
one_palette_button.pack()

two_palettes_button = tkinter.Button(window, text="Two Palettes", command=two_palettes, state="normal")
two_palettes_button.pack()

three_palettes_button = tkinter.Button(window, text="Three Palettes", command=three_palettes, state="normal")
three_palettes_button.pack()

palette_image_label_1 = tkinter.Label(window, image="")
palette_image_label_1.pack()

palette_image_label_2 = tkinter.Label(window, image="")
palette_image_label_2.pack()

palette_image_label_3 = tkinter.Label(window, image="")
palette_image_label_3.pack()

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
