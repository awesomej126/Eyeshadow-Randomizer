import random
import tkinter

window = tkinter.Tk()
window.title("Eyeshadow Randomizer")
window.geometry("800x300")

def palettes():
    palette_list = ["James Charles Palette", "Jaclyn Hill Palette"]
    palette = random.choices(palette_list)
    palette_result["text"] = "Eyeshadow palette: " + str(palette)

    if palette == ["James Charles Palette"]:
        james_mattes = ["Canvas", "518", "Rusted", "Tea", "Punch Me", "Mary", "You're Kidding", "Boutique", "Benny", "Flashback", "Tune", "Code James", "10% Off", "No Beans", "Spooky", "Bee", "Playground", "Brother", "Love That", "Pinkity Drinkity", "Social Blade", "Daddy", "Cola", "Escape", "Single", "Skip"]
        james_shimmers = ["Ringlight", "So Good", "Halloween", "Wig", "Sister", "Literally", "Shook", "Face", "Guac", "Hello", "Artistry", "Cape Cod", "A Capella"]
        transition1 = random.choices(james_mattes)
        crease1 = random.choices(james_mattes)
        outer_v1 = random.choices(james_mattes)
        lid1 = random.choices(james_shimmers)
        lower_lash_line1 = random.choices(james_mattes)
        shades_result["text"] = "Transition color: " + str(transition1) + ", Crease color: " + str(crease1) + ", Outer-V color: " + str(outer_v1) + ", Lid Color: " + str(lid1) + ", Lower Lash Line Color: " + str(lower_lash_line1)
    elif palette == ["Jaclyn Hill Palette"]:
        jaclyn_mattes = ["Silk Creme", "M.F.E.O.", "Creamsicle", "Butter", "Pooter", "Pukey", "Hunts", "Roxanne", "Jacz", "Chip", "Mocha", "Jada", "Enchanted", "Central Park", "Soda Pop", "Abyss"]
        jaclyn_shimmers = ["Enlight", "Beam", "Faint", "Sissy", "Little Lady", "Firework", "Queen", "Obsessed", "S.B.N.", "Hillster", "Buns", "Cranapple", "Royalty", "Twerk", "Hustle", "Meeks", "24/7", "Pool Party", "Diva"]
        transition2 = random.choices(jaclyn_mattes)
        crease2 = random.choices(jaclyn_mattes)
        outer_v2 = random.choices(jaclyn_mattes)
        lid2 = random.choices(jaclyn_shimmers)
        lower_lash_line2 = random.choices(jaclyn_mattes)
        shades_result["text"] = "Shades: Transition color: " + str(transition2) + ", Crease color: " + str(crease2) + ", Outer-V color: " + str(outer_v2) + ", Lid Color: " + str(lid2) + ", Lower Lash Line Color: " + str(lower_lash_line2)

    palette_button["state"] = "disabled"

def type():
    types = ["Halo", "Cut Crease", "Half Cut Crease", "Smokey Eye"]
    type = random.choices(types)
    type_result["text"] = "Eyeshadow type: "+ str(type)
    type_button["state"] = "disabled"

def liner():
    eyeliner = ["Winged", "Smudged", "Fox Eye"]
    style = random.choices(eyeliner)
    liner_result["text"] = "Eyeliner style: " + str(style)
    liner_button["state"] = "disabled"

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

window.mainloop()
