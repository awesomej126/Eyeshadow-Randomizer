import random
import tkinter
from PIL import ImageTk, Image

# GUI Stuff
window = tkinter.Tk()
window.title("Eyeshadow Randomizer")
window.geometry("1000x500")

# Palette Images
try:
    jh_image = ImageTk.PhotoImage(Image.open('jh_palette.jpg').resize((350, 200)))
    jc_image = ImageTk.PhotoImage(Image.open('jc_palette.jpg').resize((250, 200)))
    mickey_image = ImageTk.PhotoImage(Image.open('mickey_mouse.jpg').resize((250, 200)))
    q_image = ImageTk.PhotoImage(Image.open('9Q.jpg').resize((250, 200)))
except FileNotFoundError:
    raise Exception("File cannot be found")

# Palette and shade names
JC_MATTES = ["Canvas", "518", "Rusted", "Tea", "Punch Me", "Mary", "You're Kidding", "Boutique", "Benny", "Flashback", "Tune", "Code James", "10% Off", "No Beans", "Spooky", "Bee", "Playground", "Brother", "Love That", "Pinkity Drinkity", "Social Blade", "Daddy", "Cola", "Escape", "Single", "Skip"]
JC_SHIMMERS = ["Ringlight", "So Good", "Halloween", "Wig", "Sister", "Literally", "Shook", "Face", "Guac", "Hello", "Artistry", "Cape Cod", "A Capella"]
JH_MATTES = ["Silk Creme", "M.F.E.O.", "Creamsicle", "Butter", "Pooter", "Pukey", "Hunts", "Roxanne", "Jacz", "Chip", "Mocha", "Jada", "Enchanted", "Central Park", "Soda Pop", "Abyss"]
JH_SHIMMERS = ["Enlight", "Beam", "Faint", "Sissy", "Little Lady", "Firework", "Queen", "Obsessed", "S.B.N.", "Hillster", "Buns", "Cranapple", "Royalty", "Twerk", "Hustle", "Meeks", "24/7", "Pool Party", "Diva"]
MICKEY_MATTES = ["Head Out", "Life's Short", "So Fearless", "Big Dreamer", "Play by Ear", "Stop & Stare", "Big Bows", "Coy Toy", "On the Dot", "Bat Those Lashes", "Awe-Dascious", "Awe Goody", "Out Loud", "Very Vixen", "Thumbs Up", "Stun & Games", "Street Beats", "Major Edge", "Secret Weapon", "Original Artist", "Push It", "Max Power", "Wild One", "Instigator", "Total Rebel"]
MICKEY_SHIMMERS = ["Own It", "Creative Collision", "Made Ya Look", "Extra Sparkle", "Staring Contest", "Super Sassy", "Talk Flirty", "Iconic Vibes", "Troublemaker", "Into Mischief"]
Q_MATTES = ["Life", "Healing", "Sun", "Spirit", "Fluidity", "Nature", "Representation", "Serenity", "Visibilty"]
Q_SHIMMERS = []
NAMES = ["James Charles Palette", "Jaclyn Hill Palette", "Mickey & Friends Palette", "9Q Love Matters Palette"]
IMAGES = [jc_image, jh_image, mickey_image, q_image]
MATTES_LIST = [JC_MATTES, JH_MATTES, MICKEY_MATTES, Q_MATTES]
SHIMMERS_LIST = [JC_SHIMMERS, JH_SHIMMERS, MICKEY_SHIMMERS, Q_SHIMMERS]
STYLES = ["Halo", "Cut Crease", "Half Cut Crease", "Smokey Eye"]
LINERS = ["Winged", "Smudged", "None"]

# Functions
# Chooses shades, adds them onto GUI
def shade_selector(mattes, shimmers):

    # Chooses number of matte and shimmer eyeshadows
    m_num = random.randint(2, 4)
    s_num = random.randint(0, 2) if shimmers != [] else 0

    # Chooses random mattes and shimmers
    selected_mattes = ", ".join(random.sample(mattes, k=m_num))
    selected_shimmers = ", ".join(random.sample(shimmers, k=s_num)) if s_num > 0 else "None"

    # Adds selected shades onto GUI
    shades_result.configure(text=f"Matte Shades: {selected_mattes}; Shimmer Shades: {selected_shimmers}")

# Chooses palette and its shades
def palettes():

    # Disables palette button, changes main text 
    palette_button.configure(state=tkinter.DISABLED)
    main_text.configure(text="Now choose your eyeshadow style...")

    # Chooses random palette
    index = random.randint(0, len(NAMES)-1)
    palette_result.configure(text=NAMES[index])
    palette_image_label.configure(image=IMAGES[index])

    # Selects shades
    shade_selector(MATTES_LIST[index], SHIMMERS_LIST[index])

# Chooses the style of eyeshadow
def eyeshadow_style():
    type_button.configure(state=tkinter.DISABLED)
    main_text.configure(text="Finally, choose your liner...")

    style = random.choice(STYLES)
    type_result.configure(text=f"Eyeshadow type: {style}")

# Chooses the liner
def liner():
    liner_button.configure(state=tkinter.DISABLED)
    main_text.configure(text="Here's your final look!")

    liner = random.choice(LINERS)
    liner_result.configure(text=f"Eyeliner style: {liner}")

# Resets program
def reset():

    # Enables buttons
    palette_button.configure(state=tkinter.NORMAL)
    type_button.configure(state=tkinter.NORMAL)
    liner_button.configure(state=tkinter.NORMAL)

    # Clears result labels, restores main_text label
    main_text.configure(text="Choose your palette...")
    liner_result.configure(text="")
    type_result.configure(text="")
    shades_result.configure(text="")
    palette_result.configure(text="")
    palette_image_label.configure(image="")

# Buttons
main_text = tkinter.Label(window, text="Choose your palette...")
main_text.pack()

palette_button = tkinter.Button(window, text="Palette", command=palettes)
palette_button.pack()

palette_image_label = tkinter.Label(window, image="")
palette_image_label.pack()

palette_result = tkinter.Label(window, text="")
palette_result.pack()

shades_result = tkinter.Label(window, text="")
shades_result.pack()

type_button = tkinter.Button(window, text="Style", command=eyeshadow_style)
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
