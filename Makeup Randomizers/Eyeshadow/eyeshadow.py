# from faulthandler import disable
import random
import tkinter
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Eyeshadow Randomizer")
window.geometry("1000x500")

# Palette Images
jh_image = ImageTk.PhotoImage(Image.open('Eyeshadow/jh_palette.jpg').resize((350, 200)))
jc_image = ImageTk.PhotoImage(Image.open('Eyeshadow/jc_palette.jpg').resize((250, 200)))
mickey_image = ImageTk.PhotoImage(Image.open('Eyeshadow/mickey_mouse.jpg').resize((250, 200)))
q_image = ImageTk.PhotoImage(Image.open('Eyeshadow/9Q.jpg').resize((250, 200)))

# Shade Names
james_mattes = ["Canvas", "518", "Rusted", "Tea", "Punch Me", "Mary", "You're Kidding", "Boutique", "Benny", "Flashback", "Tune", "Code James", "10% Off", "No Beans", "Spooky", "Bee", "Playground", "Brother", "Love That", "Pinkity Drinkity", "Social Blade", "Daddy", "Cola", "Escape", "Single", "Skip"]
james_shimmers = ["Ringlight", "So Good", "Halloween", "Wig", "Sister", "Literally", "Shook", "Face", "Guac", "Hello", "Artistry", "Cape Cod", "A Capella"]
jaclyn_mattes = ["Silk Creme", "M.F.E.O.", "Creamsicle", "Butter", "Pooter", "Pukey", "Hunts", "Roxanne", "Jacz", "Chip", "Mocha", "Jada", "Enchanted", "Central Park", "Soda Pop", "Abyss"]
jaclyn_shimmers = ["Enlight", "Beam", "Faint", "Sissy", "Little Lady", "Firework", "Queen", "Obsessed", "S.B.N.", "Hillster", "Buns", "Cranapple", "Royalty", "Twerk", "Hustle", "Meeks", "24/7", "Pool Party", "Diva"]
mickey_mattes = ["Head Out", "Life's Short", "So Fearless", "Big Dreamer", "Play by Ear", "Stop & Stare", "Big Bows", "Coy Toy", "On the Dot", "Bat Those Lashes", "Awe-Dascious", "Awe Goody", "Out Loud", "Very Vixen", "Thumbs Up", "Stun & Games", "Street Beats", "Major Edge", "Secret Weapon", "Original Artist", "Push It", "Max Power", "Wild One", "Instigator", "Total Rebel"]
mickey_shimmers = ["Own It", "Creative Collision", "Made Ya Look", "Extra Sparkle", "Staring Contest", "Super Sassy", "Talk Flirty", "Iconic Vibes", "Troublemaker", "Into Mischief"]
q_shades = ["Life", "Healing", "Sun", "Spirit", "Fluidity", "Nature", "Representation", "Serenity", "Visibilty"]

# Functions
# Chooses your palette and colors
def palettes():
    palette_button["state"] = "disabled"
    palettes = ["James Charles Palette", "Jaclyn Hill Palette", "Mickey & Friends Palette", "9Q Love Matters Palette"]
    palette = random.choice(palettes)
    palette_result["text"] = "Eyeshadow palette: {0}".format(palette)

    mnum = random.randint(2, 4)
    snum = random.randint(0, 2)

    if palette == "James Charles Palette":
        palette_pic["image"] = jc_image
        m = james_mattes
        s = 0 if snum == 0 else james_shimmers

    elif palette == "Jaclyn Hill Palette":
        palette_pic["image"] = jh_image
        m = jaclyn_mattes
        s = 0 if snum == 0 else jaclyn_shimmers

    elif palette == "Mickey & Friends Palette":
        palette_pic["image"] = mickey_image
        m = mickey_mattes
        s = 0 if snum == 0 else mickey_shimmers
    
    elif palette == "9Q Love Matters Palette":
        palette_pic["image"] = q_image
        m = q_shades
        snum = 0

    mattes = ", ".join(random.choices(m, k=mnum))
    shimmers = "None" if snum == 0 else ", ".join(random.choices(s, k=snum))

    shades_result["text"] = "Matte Shades: {}; Shimmer Shades: {}".format(mattes, shimmers)

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
palette_button = tkinter.Button(window, text="Palette", command=palettes)
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
