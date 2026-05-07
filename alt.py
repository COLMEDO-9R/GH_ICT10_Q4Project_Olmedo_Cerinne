from pyscript import document # type: ignore

Olmedo = [
    {
        "img": "tkam.jpg", 
        "caption": "my favorite memory is the Mockingbird Challenge in English class <br> - Cerinne Olmedo"
    },
    {
        "img": "image.jpg",
        "caption": "my favorite memory is the 2025-2026 Campout <br> - Lauren Villafuerte"
    },
    {
        "img": "Preziosa Farms_Camping.webp",
        "caption": "my favorite memory is the 2025-2026 Campout <br> - Jaiyanah Baring"
    }
]


Baring = [
    {
        "img": "day.jpg",
        "caption": "my favorite memory is the 2025-2026 President's Day <br> - Aisha Ledesma"
    },
    {
        "img": "Camping_Obstacle Course.webp",
        "caption": "my favorite memory is 2025-2026 Campout <br> - Shalanie Garabiles"
    },
    {
        "img": "obmc_fair.jpg",
        "caption": "my favorite memory is the Food Fair <br> - Amanda Yao"
    }
]

def create_cards(data, container_id):
    container = document.getElementById(container_id)

    for item in data:
        card = document.createElement("div")
        card.className = "flip-card"

        card.innerHTML = f"""
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <img src="{item['img']}">
            </div>
            <div class="flip-card-back">
                <p>{item['caption']}</p>
            </div>
        </div>
        """

        container.appendChild(card)

create_cards(Olmedo, "Olmedo-gallery")
create_cards(Baring, "Baring-gallery")
