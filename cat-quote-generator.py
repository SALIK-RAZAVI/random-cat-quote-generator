import tkinter as tk
from tkinter import messagebox
import random

# Lists of components for generating funny cat videos
cat_actions = [
    "Falls off a sofa",
    "Chases a laser pointer",
    "Tries to catch a bug on a screen",
    "Meows at a mirror",
    "Knocks over a plant",
    "Gets scared by its own tail",
    "Plays with a cardboard box",
    "Stares at nothing for 10 minutes",
    "Steals food from another pet",
    "Sleeps in an awkward position"
]

ridiculous_features = [
    "while wearing a tiny hat",
    "in slow motion",
    "with dramatic music",
    "using special effects",
    "narrated by Morgan Freeman",
    "with subtitles in cat language",
    "with guest appearance by a squirrel",
    "in outer space",
    "with a romantic theme",
    "with intense zoom-ins"
]

# Function to generate a funny cat video description
def generate_cat_video():
    cat_action = random.choice(cat_actions)
    feature = random.choice(ridiculous_features)
    video_description = f"Watch this hilarious quote of a cat {cat_action} {feature}!"
    messagebox.showinfo("Funny Cat quote Generator", video_description)

# Creating main window
root = tk.Tk()
root.title("Funny Random Cat quote Generator")

# Adding widgets
tk.Label(root, text="Click below to generate a funny cat quote:").pack(pady=10)
generate_button = tk.Button(root, text="Generate Cat quote", command=generate_cat_video)
generate_button.pack(pady=20)

# Running the GUI loop
root.mainloop()