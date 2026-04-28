from pyscript import document # type: ignore
from js import document  # type: ignore
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return (
            f"Hello! My name is {self.name}. "
            f"I am from 10 {self.section}, "
            f"and my favorite subject is {self.favorite_subject}."
        )


classmates = [
    Classmate("Lauren Villafuerte", "Ruby", "English"),
    Classmate("Jaiyanah Baring", "Ruby", "Mathematics"),
    Classmate("Amanda Yao", "Ruby", "Music & Arts"),
    Classmate("Aisha Ledesma", "Ruby", "Science"),
    Classmate("Shalanie Garabiles", "Ruby", "Music & Arts"),
]


def show_list(event=None):
    output = document.getElementById("output")

    introductions = []
    for number, classmate in enumerate(classmates, start=1):
        introductions.append(f"{number}. {classmate.introduce()}")

    output.innerHTML = "<br><br>".join(introductions)


def add_classmate(event=None):
    name_input = document.getElementById("name")
    section_input = document.getElementById("section")
    subject_input = document.getElementById("subject")
    output = document.getElementById("output")

    name = name_input.value.strip()
    section = section_input.value.strip()
    favorite_subject = subject_input.value.strip()

    if not name or not section or not favorite_subject:
        output.innerHTML = "Please complete the name, section, and favorite subject first."
        return

    new_classmate = Classmate(name, section, favorite_subject)
    classmates.append(new_classmate)

    output.innerHTML = (
        "New classmate added successfully!<br><br>"
        f"{new_classmate.introduce()}<br><br>"
        f"There are now {len(classmates)} classmates in the list."
    )

    name_input.value = ""
    section_input.value = ""
    subject_input.value = ""



days = ["ᴍᴏɴᴅᴀʏ", "ᴛᴜᴇꜱᴅᴀʏ", "ᴡᴇᴅɴᴇꜱᴅᴀʏ", "ᴛʜᴜʀꜱᴅᴀʏ", "ꜰʀɪᴅᴀʏ"]
absence_counts = np.array([0, 0, 0, 0, 0])

def generate_plot():
    plt.close('all')
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(days, absence_counts,  # type: ignore
            marker='o', 
            color="#000000", 
            linewidth=3, 
            markersize=8)
    
    ax.set_title("♡˚⋆ ᴡᴇᴇᴋʟʏ ᴀᴛᴛᴇɴᴅᴀɴᴄᴇ (ᴀʙꜱᴇɴᴄᴇꜱ) ⋆˚♡")
    ax.set_ylabel("✦. ɴᴜᴍʙᴇʀ ᴏꜰ ᴀʙꜱᴇɴᴄᴇꜱ .✦")
    ax.grid(True, linestyle='--', alpha=0.7)
    
    display(fig, target="graph-output", append=False)

def update_graph(event):
    day_index = int(document.getElementById("day-select").value)
    new_value = int(document.getElementById("absence-input").value)
    
    absence_counts[day_index] = new_value
    
    generate_plot()

generate_plot()
