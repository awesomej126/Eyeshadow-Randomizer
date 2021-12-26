import random
import tkinter

# GUI Stuff
window = tkinter.Tk()
window.title("Eyeshadow Randomizer")
window.geometry("800x300")

#Functions
# Chooses your palette and colors
def palettes():
    reset_button["state"] = "normal"
    palettes = ["James Charles Palette", "Jaclyn Hill Palette", "Mickey & Friends Palette"]
    palette = random.choice(palettes)
    palette_result["text"] = "Eyeshadow palette: {0}".format(palette)

    if palette == "James Charles Palette":
        james_mattes = ["Canvas", "518", "Rusted", "Tea", "Punch Me", "Mary", "You're Kidding", "Boutique", "Benny", "Flashback", "Tune", "Code James", "10% Off", "No Beans", "Spooky", "Bee", "Playground", "Brother", "Love That", "Pinkity Drinkity", "Social Blade", "Daddy", "Cola", "Escape", "Single", "Skip"]
        james_shimmers = ["Ringlight", "So Good", "Halloween", "Wig", "Sister", "Literally", "Shook", "Face", "Guac", "Hello", "Artistry", "Cape Cod", "A Capella"]
        transition1 = random.choice(james_mattes)
        crease1 = random.choice(james_mattes)
        outer_v1 = random.choice(james_mattes)
        lid1 = random.choice(james_shimmers)
        lower_lash_line1 = random.choice(james_mattes)
        shades_result["text"] = "Transition color: {0}, Crease color: {1}, Outer-V color: {2}, Lid Color: {3}, Lower Lash Line Color: {4}".format(transition1, crease1, outer_v1, lid1, lower_lash_line1)
    elif palette == "Jaclyn Hill Palette":
        jaclyn_mattes = ["Silk Creme", "M.F.E.O.", "Creamsicle", "Butter", "Pooter", "Pukey", "Hunts", "Roxanne", "Jacz", "Chip", "Mocha", "Jada", "Enchanted", "Central Park", "Soda Pop", "Abyss"]
        jaclyn_shimmers = ["Enlight", "Beam", "Faint", "Sissy", "Little Lady", "Firework", "Queen", "Obsessed", "S.B.N.", "Hillster", "Buns", "Cranapple", "Royalty", "Twerk", "Hustle", "Meeks", "24/7", "Pool Party", "Diva"]
        transition2 = random.choice(jaclyn_mattes)
        crease2 = random.choice(jaclyn_mattes)
        outer_v2 = random.choice(jaclyn_mattes)
        lid2 = random.choice(jaclyn_shimmers)
        lower_lash_line2 = random.choice(jaclyn_mattes)
        shades_result["text"] = "Transition color: {0}, Crease color: {1}, Outer-V color: {2}, Lid Color: {3}, Lower Lash Line Color: {4}".format(transition2, crease2, outer_v2, lid2, lower_lash_line2)
    elif palette == "Mickey & Friends Palette":
        mickey_mattes = ["Head Out", "Life's Short", "So Fearless", "Big Dreamer", "Play by Ear", "Stop & Stare", "Big Bows", "Coy Toy", "On the Dot", "Bat Those Lashes", "Awe-Dascious", "Awe Goody", "Out Loud", "Very Vixen", "Thumbs Up", "Stun & Games", "Street Beats", "Major Edge", "Secret Weapon", "Original Artist", "Push It", "Max Power", "Wild One", "Instigator", "Total Rebel"]
        mickey_shimmers = ["Own It", "Creative Collision", "Made Ya Look", "Extra Sparkle", "Staring Contest", "Super Sassy", "Talk Flirty", "Iconic Vibes", "Troublemaker", "Into Mischief"]
        transition3 = random.choice(mickey_mattes)
        crease3 = random.choice(mickey_mattes)
        outer_v3 = random.choice(mickey_mattes)
        lid3 = random.choice(mickey_shimmers)
        lower_lash_line3 = random.choice(mickey_mattes)
        shades_result["text"] = "Transition color: {0}, Crease color: {1}, Outer-V color: {2}, Lid Color: {3}, Lower Lash Line Color: {4}".format(transition3, crease3, outer_v3, lid3, lower_lash_line3)
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
    eyeliners = ["Winged", "Smudged", "Fox Eye", "None"]
    eyeliner = random.choice(eyeliners)
    liner_result["text"] = "Eyeliner style: {0}".format(eyeliner)
    liner_button["state"] = "disabled"

# Resets program
def reset():
    reset_button["state"] = "disabled"
    palette_button["state"] = "normal"
    type_button["state"] = "normal"
    liner_button["state"] = "normal"
    palette_result["text"] = ""
    shades_result["text"] = ""
    type_result["text"] = ""
    liner_result["text"] = ""

palette_button = tkinter.Button(window, text="Palette", command=palettes)
palette_button.pack()

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

reset_button = tkinter.Button(window, text="Reset", command=reset)
reset_button.pack()

window.mainloop()
