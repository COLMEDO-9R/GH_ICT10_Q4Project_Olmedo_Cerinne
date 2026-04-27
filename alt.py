from pyscript import document # type: ignore

Olmedo = [
    {
        "img": "tkam.jpg", 
        "caption": "my favorite memory is the mockingbird challenge in English class <br> - Cerinne"
    },
    {
        "img": "image.jpg",
        "caption": "my favorite memory is the 2025-2026 campout <br> - Lauren"
    },
    {
        "img": "",
        "caption": "my favorite memory is  <br> - Jai"
    }
]


Baring = [
    {
        "img": "day.jpg",
        "caption": "my favorite memory is the 2025-2026 president's day <br> - Aisha"
    },
    {
        "img": "",
        "caption": "Shalanie's description"
    },
    {
        "img": "",
        "caption": "Amanda's description"
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
