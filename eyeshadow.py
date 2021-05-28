import random

def palettes():
    palette_list = ["James Charles Palette", "Jaclyn Hill Palette"]
    palette = random.choices(palette_list)
    print("Eyeshadow palette: " + str(palette))

    if palette == ["James Charles Palette"]:
        james_mattes = ["Canvas", "518", "Rusted", "Tea", "Punch Me", "Mary", "You're Kidding", "Boutique", "Benny", "Flashback", "Tune", "Code James", "10% Off", "No Beans", "Spooky", "Bee", "Playground", "Brother", "Love That", "Pinkity Drinkity", "Social Blade", "Daddy", "Cola", "Escape", "Single", "Skip"]
        james_shimmers = ["Ringlight", "So Good", "Halloween", "Wig", "Sister", "Literally", "Shook", "Face", "Guac", "Hello", "Artistry", "Cape Cod", "A Capella"]
        transition1 = random.choices(james_mattes)
        crease1 = random.choices(james_mattes)
        outer_v1 = random.choices(james_mattes)
        lid1 = random.choices(james_shimmers)
        lower_lash_line1 = random.choices(james_mattes)
        print("Transition color: " + str(transition1) + ", Crease color: " + str(crease1) + ", Outer-V color: " + str(outer_v1) + ", Lid Color: " + str(lid1) + ", Lower Lash Line Color: " + str(lower_lash_line1))
    elif palette == ["Jaclyn Hill Palette"]:
        jaclyn_mattes = ["Silk Creme", "M.F.E.O.", "Creamsicle", "Butter", "Pooter", "Pukey", "Hunts", "Roxanne", "Jacz", "Chip", "Mocha", "Jada", "Enchanted", "Central Park", "Soda Pop", "Abyss"]
        jaclyn_shimmers = ["Enlight", "Beam", "Faint", "Sissy", "Little Lady", "Firework", "Queen", "Obsessed", "S.B.N.", "Hillster", "Buns", "Cranapple", "Royalty", "Twerk", "Hustle", "Meeks", "24/7", "Pool Party", "Diva"]
        transition2 = random.choices(jaclyn_mattes)
        crease2 = random.choices(jaclyn_mattes)
        outer_v2 = random.choices(jaclyn_mattes)
        lid2 = random.choices(jaclyn_shimmers)
        lower_lash_line2 = random.choices(jaclyn_mattes)
        print("Transition color: " + str(transition2) + ", Crease color: " + str(crease2) + ", Outer-V color: " + str(outer_v2) + ", Lid Color: " + str(lid2) + ", Lower Lash Line Color: " + str(lower_lash_line2))

def type():
    types = ["Halo", "Cut Crease", "Half Cut Crease", "Smokey Eye"]
    type = random.choices(types)
    print("Eyeshadow type: " + str(type))

def liner():
    eyeliner = ["Winged", "Smudged", "Fox Eye"]
    style = random.choices(eyeliner)
    print("Eyeliner style: " + str(style))

palettes()
type()
liner()
