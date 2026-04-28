from pyscript import display  # type: ignore
from js import document  # type: ignore
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

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
