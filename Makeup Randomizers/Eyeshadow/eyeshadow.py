import random
import tkinter
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Eyeshadow Randomizer")
window.geometry("1000x500")

# Palette Images
jh_image = ImageTk.PhotoImage(Image.open('jh_palette.jpg').resize((350, 200)))
jc_image = ImageTk.PhotoImage(Image.open('jc_palette.jpg').resize((250, 200)))
mickey_image = ImageTk.PhotoImage(Image.open('mickey_mouse.jpg').resize((250, 200)))
q_image = ImageTk.PhotoImage(Image.open('9Q.jpg').resize((250, 200)))

# Shade Names (Made them tuples cause the shade names stay constant)
jc_mattes = ("Canvas", "518", "Rusted", "Tea", "Punch Me", "Mary", "You're Kidding", "Boutique", "Benny", "Flashback", "Tune", "Code James", "10% Off", "No Beans", "Spooky", "Bee", "Playground", "Brother", "Love That", "Pinkity Drinkity", "Social Blade", "Daddy", "Cola", "Escape", "Single", "Skip")
jc_shimmers = ("Ringlight", "So Good", "Halloween", "Wig", "Sister", "Literally", "Shook", "Face", "Guac", "Hello", "Artistry", "Cape Cod", "A Capella")
jh_mattes = ("Silk Creme", "M.F.E.O.", "Creamsicle", "Butter", "Pooter", "Pukey", "Hunts", "Roxanne", "Jacz", "Chip", "Mocha", "Jada", "Enchanted", "Central Park", "Soda Pop", "Abyss")
jh_shimmers = ("Enlight", "Beam", "Faint", "Sissy", "Little Lady", "Firework", "Queen", "Obsessed", "S.B.N.", "Hillster", "Buns", "Cranapple", "Royalty", "Twerk", "Hustle", "Meeks", "24/7", "Pool Party", "Diva")
mickey_mattes = ("Head Out", "Life's Short", "So Fearless", "Big Dreamer", "Play by Ear", "Stop & Stare", "Big Bows", "Coy Toy", "On the Dot", "Bat Those Lashes", "Awe-Dascious", "Awe Goody", "Out Loud", "Very Vixen", "Thumbs Up", "Stun & Games", "Street Beats", "Major Edge", "Secret Weapon", "Original Artist", "Push It", "Max Power", "Wild One", "Instigator", "Total Rebel")
mickey_shimmers = ("Own It", "Creative Collision", "Made Ya Look", "Extra Sparkle", "Staring Contest", "Super Sassy", "Talk Flirty", "Iconic Vibes", "Troublemaker", "Into Mischief")
q_shades = ("Life", "Healing", "Sun", "Spirit", "Fluidity", "Nature", "Representation", "Serenity", "Visibilty")

# Functions
# Chooses shades, adds them onto GUI
def shade_selector(mattes, shimmers=()):
    m = mattes
    if shimmers != ():
        s = shimmers
    else:
        snum = 0
    
    mnum = random.randint(2, 4)
    snum = random.randint(0, 2)

    selected_mattes = ", ".join(random.choices(m, k=mnum))
    selected_shimmers = "None" if snum == 0 or shimmers == () else ", ".join(random.choices(s, k=snum))

    shades_result["text"] = "Matte Shades: {}; Shimmer Shades: {}".format(selected_mattes, selected_shimmers)

# Associates palette with its picture, adds them onto GUI
def palettes(palette_name, palette_image):
    palette_pic["image"] = palette_image
    palette_result["text"] = "Eyeshadow palette: {0}".format(palette_name)

# Chooses your palette, colors determined by palette_selector
def palette_selector():
    palette_button["state"] = "disabled"
    palette_names = ["James Charles Palette", "Jaclyn Hill Palette", "Mickey & Friends Palette", "9Q Love Matters Palette"]
    selected_palette = random.choice(palette_names)

    if selected_palette == "James Charles Palette":
        palettes(selected_palette, jc_image)
        shade_selector(jc_mattes, jc_shimmers)

    elif selected_palette == "Jaclyn Hill Palette":
        palettes(selected_palette, jh_image)
        shade_selector(jh_mattes, jh_shimmers)

    elif selected_palette == "Mickey & Friends Palette":
        palettes(selected_palette, mickey_image)
        shade_selector(mickey_mattes, mickey_shimmers)
    
    elif selected_palette == "9Q Love Matters Palette":
        palettes(selected_palette, q_image)
        shade_selector(q_shades)

# Chooses the style of eyeshadow
def eyeshadow_type():
    type_button["state"] = "disabled"
    types = ["Halo", "Cut Crease", "Half Cut Crease", "Smokey Eye"]
    t = random.choice(types)
    type_result["text"] = "Eyeshadow type: {0}".format(t)

# Chooses the liner
def liner():
    liner_button["state"] = "disabled"
    eyeliners = ["Winged", "Smudged", "None"]
    eyeliner = random.choice(eyeliners)
    liner_result["text"] = "Eyeliner style: {0}".format(eyeliner)

# Resets program
def reset():
    palette_button["state"] = type_button["state"] = liner_button["state"] = "normal"
    palette_result["text"] = shades_result["text"] = type_result["text"] = liner_result["text"] = palette_pic["image"] = ""


# Buttons
palette_button = tkinter.Button(window, text="Palette", command=palette_selector)
palette_button.pack()

palette_pic = tkinter.Label(window, image="")
palette_pic.pack()

palette_result = tkinter.Label(window, text="")
palette_result.pack()

shades_result = tkinter.Label(window, text="")
shades_result.pack()

type_button = tkinter.Button(window, text="Type", command=eyeshadow_type)
type_button.pack()

type_result = tkinter.Label(window, text="")
type_result.pack()

liner_button = tkinter.Button(window, text="Eyeliner", command=liner)
liner_button.pack()

liner_result = tkinter.Label(window, text="")
liner_result.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset)
reset_button.pack()

window.mainloop()
