import random
import tkinter
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Eyeshadow Randomizer")
window.geometry("1000x500")

# Palette Images
jh_image = ImageTk.PhotoImage(Image.open('Eyeshadow/jhpalette.jpg').resize((350, 200)))
jc_image = ImageTk.PhotoImage(Image.open('Eyeshadow/jcpalette.jpg').resize((250, 200)))
mickey_image = ImageTk.PhotoImage(Image.open('Eyeshadow/mickeymouse.jpg').resize((250, 200)))

# Functions
# Chooses your palette and colors
def palettes():
    reset_button["state"] = "normal"
    palettes = ["James Charles Palette", "Jaclyn Hill Palette", "Mickey & Friends Palette"]
    palette = random.choice(palettes)
    palette_result["text"] = "Eyeshadow palette: {0}".format(palette)
    james_mattes = ["Canvas", "518", "Rusted", "Tea", "Punch Me", "Mary", "You're Kidding", "Boutique", "Benny", "Flashback", "Tune", "Code James", "10% Off", "No Beans", "Spooky", "Bee", "Playground", "Brother", "Love That", "Pinkity Drinkity", "Social Blade", "Daddy", "Cola", "Escape", "Single", "Skip"]
    james_shimmers = ["Ringlight", "So Good", "Halloween", "Wig", "Sister", "Literally", "Shook", "Face", "Guac", "Hello", "Artistry", "Cape Cod", "A Capella"]
    jaclyn_mattes = ["Silk Creme", "M.F.E.O.", "Creamsicle", "Butter", "Pooter", "Pukey", "Hunts", "Roxanne", "Jacz", "Chip", "Mocha", "Jada", "Enchanted", "Central Park", "Soda Pop", "Abyss"]
    jaclyn_shimmers = ["Enlight", "Beam", "Faint", "Sissy", "Little Lady", "Firework", "Queen", "Obsessed", "S.B.N.", "Hillster", "Buns", "Cranapple", "Royalty", "Twerk", "Hustle", "Meeks", "24/7", "Pool Party", "Diva"]
    mickey_mattes = ["Head Out", "Life's Short", "So Fearless", "Big Dreamer", "Play by Ear", "Stop & Stare", "Big Bows", "Coy Toy", "On the Dot", "Bat Those Lashes", "Awe-Dascious", "Awe Goody", "Out Loud", "Very Vixen", "Thumbs Up", "Stun & Games", "Street Beats", "Major Edge", "Secret Weapon", "Original Artist", "Push It", "Max Power", "Wild One", "Instigator", "Total Rebel"]
    mickey_shimmers = ["Own It", "Creative Collision", "Made Ya Look", "Extra Sparkle", "Staring Contest", "Super Sassy", "Talk Flirty", "Iconic Vibes", "Troublemaker", "Into Mischief"]
    mnum = random.randint(2, 4)
    snum = random.randint(0, 2)
    if palette == "James Charles Palette":
        palette_pic["image"] = jc_image
        mjames = random.choices(james_mattes, k=mnum)
        sjames = random.choices(james_shimmers, k=snum)
        if snum == 0:
            sjames = "None"
        shades_result["text"] = "Matte Shades: {0}, Shimmer Shades: {1}".format(mjames, sjames)
    elif palette == "Jaclyn Hill Palette":
        palette_pic["image"] = jh_image
        mjaclyn = random.choices(jaclyn_mattes, k=mnum)
        sjaclyn = random.choices(jaclyn_shimmers, k=snum)
        if snum == 0:
            sjaclyn = "None"
        shades_result["text"] = "Matte Shades: {0}, Shimmer Shades: {1}".format(mjaclyn, sjaclyn)
    elif palette == "Mickey & Friends Palette":
        palette_pic["image"] = mickey_image
        mmickey = random.choices(mickey_mattes, k=mnum)
        smickey = random.choices(mickey_shimmers, k=snum)
        if snum == 0:
            smickey = "None"
        shades_result["text"] = "Matte Shades: {0}, Shimmer Shades: {1}".format(mmickey, smickey)
    palette_button["state"] = "disabled"

# Chooses the style of eyeshadow
def type():
    reset_button["state"] = "normal"
    types = ["Halo", "Cut Crease", "Half Cut Crease", "Smokey Eye"]
    type = random.choice(types)
    type_result["text"] = "Eyeshadow type: {0}".format(type)
    type_button["state"] = "disabled"

# Chooses the liner
def liner():
    reset_button["state"] = "normal"
    eyeliners = ["Winged", "Smudged", "None"]
    eyeliner = random.choice(eyeliners)
    liner_result["text"] = "Eyeliner style: {0}".format(eyeliner)
    liner_button["state"] = "disabled"

# Resets program
def reset():
    reset_button["state"] = "disabled"
    palette_button["state"] = type_button["state"] = liner_button["state"] = "normal"
    palette_result["text"] = shades_result["text"] = type_result["text"] = liner_result["text"] = palette_pic["image"] = ""

palette_button = tkinter.Button(window, text="Palette", command=palettes)
palette_button.pack()

palette_pic = tkinter.Label(window, image="")
palette_pic.pack()

palette_result = tkinter.Label(window, text="")
palette_result.pack()

shades_result = tkinter.Label(window, text="")
shades_result.pack()

type_button = tkinter.Button(window, text="Type", command=type)
type_button.pack()

type_result = tkinter.Label(window, text="")
type_result.pack()

liner_button = tkinter.Button(window, text="Eyeliner", command=liner)
liner_button.pack()

liner_result = tkinter.Label(window, text="")
liner_result.pack()

reset_button = tkinter.Button(window, text="Reset", command=reset, state="disabled")
reset_button.pack()

window.mainloop()
